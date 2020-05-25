
# 94 二叉树的中序遍历 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
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
    def inorderTraversal_re(self, root):
        """
        retcursive
        :param root:
        :return:
        """
        if not root:
            return
        self.inorderTraversal_re(root.left)
        print(root.val)
        self.inorderTraversal_re(root.right)

    def inorderTraversal(self, root):
        """
        stack
        :param root:
        :return:
        """
        visited = []
        stack = []
        while True:
            if root:
                stack.append(root)
                root = root.left
            else:
                if len(stack) > 0:
                    root = stack.pop()
                    visited.append(root.val)
                    root = root.right
                else:
                    return visited




root = Node(1)
root.add_right(2)
root.right.add_left(3)

s = Solution()
print(s.inorderTraversal(root))


