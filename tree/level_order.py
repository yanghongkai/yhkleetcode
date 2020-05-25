
# 102 二叉树的层次遍历 https://leetcode-cn.com/problems/binary-tree-level-order-traversal/ 


# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert_left(self, child):
        if self.left is None:
            self.left = child
        else:
            child.left = self.left
            self.left = child

    def insert_right(self, child):
        if self.right is None:
            self.right = child
        else:
            child.right = child


class Solution:
    def levelOrder(self, root):
        """

        :param root:
        :return:
        """
        from collections import deque
        visited = []
        if not root:
            return visited
        search_queue = deque()
        search_queue.append([root])
        while search_queue:
            node_lis = search_queue.popleft()
            tmp = []
            childs = []
            for node in node_lis:
                if node:
                    tmp.append(node.val)
                    if node.left:
                        childs.append(node.left)
                    if node.right:
                        childs.append(node.right)
            if childs:
                search_queue.append(childs)
            visited.append(tmp)
        return visited




right_child = Node(20)
right_child.insert_left(Node(16))
right_child.insert_right(Node(7))
root = Node(3)
root.insert_left(Node(9))
root.insert_right(right_child)

s = Solution()
print(s.levelOrder(root))







