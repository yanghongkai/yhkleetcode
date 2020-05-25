
# 144 二叉树的前序遍历 https://leetcode-cn.com/problems/binary-tree-preorder-traversal/


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def add_left(self, x):
        self.left = Node(x)

    def add_right(self, x):
        self.right = Node(x)


class Solution:
    def preorderTraversal(self, root):
        """

        :param root:
        :return:
        """
        visited = []
        stack = []
        while True:
            if root:
                visited.append(root.val)
                stack.append(root)
                root = root.left
            else:
                if len(stack)>0:
                    root = stack.pop()
                    root = root.right
                else:
                    return visited


root = Node(1)
root.add_right(2)
root.right.add_left(3)

s = Solution()
print(s.preorderTraversal(root))




