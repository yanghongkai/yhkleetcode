
# 701 二叉搜索树中的插入操作  https://leetcode-cn.com/problems/insert-into-a-binary-search-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 找到空位置插入新节点
        if not root:
            return TreeNode(val=val)
        # if root.val == val:
        #     pass  BST中一般不会插入已存在的元素
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)

        return root











