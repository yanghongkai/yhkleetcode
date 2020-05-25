
# 145 二叉树的后序遍历 https://leetcode-cn.com/problems/binary-tree-postorder-traversal/


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
    def postorderTraversal(self, root):
        """
        left -> right -> visited
        preorder: visited -> left -> right
        改进后的preorder: visited -> right -> left
        :param root:
        :return:
        """
        visited = []
        stack = []
        stack_res = []
        if not root:
            return stack_res
        stack.append(root)
        while len(stack) > 0:
            root = stack.pop()
            stack_res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        stack_res.reverse()
        return stack_res


root = Node(1)
root.add_right(2)
root.right.add_left(3)

s = Solution()
print(s.postorderTraversal(root))




