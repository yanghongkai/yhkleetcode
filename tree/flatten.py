
# 114 二叉树展开为链表 https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/

class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        1. 将左子树插入到右子树的地方
        2. 将原来的右子树接到左子树的最右节点
        3. 考虑新的右子树的根节点，一直重复上边的过程，直到新的右子树为null
        """
        stack = []
        visited = []
        head = root
        while True:
            if root:
                visited.append(root.val)
                stack.append(root)
                root = root.left


            else:
                if len(stack) > 0:
                    root = stack.pop()
                    root = root.right
                else:
                    return visited

        pass







