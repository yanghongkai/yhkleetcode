
# 98 验证二叉搜索树  https://leetcode-cn.com/problems/validate-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_valid_BST(root, min, max):
            if root is None:
                return True
            if min and root.val <= min.val:
                return False
            if max and root.val >= max.val:
                return False
            return is_valid_BST(root.left, min, root) and is_valid_BST(root.right, root, max)

        return is_valid_BST(root, None, None)








