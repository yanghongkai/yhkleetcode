
# 95 不同的二叉搜索树 II https://leetcode-cn.com/problems/unique-binary-search-trees-ii/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def _put(self, val):
        """

        :param node:
        :return:
        """
        if val < self.val:
            if self.left:
                self.left._put(val)
            else:
                self.left = TreeNode(val)
        else:
            if self.right:
                self.right._put(val)
            else:
                self.right = TreeNode(val)

    def print_all(self):
        """
        宽度优先遍历
        :return:
        """
        import queue
        q = queue.Queue()
        visited = []
        q.put(self)
        while not q.empty():
            node = q.get()
            if node:
                print("node.val:", node.val)
            else:
                print("node.val:null")
            if node:
                visited.append(node.val)
                if node.left or node.right:
                    q.put(node.left)
                    q.put(node.right)
            else:
                visited.append("null")
        return visited




root = TreeNode(1)
root._put(2)
root._put(3)
print(root)
print(root.print_all())



class Solution:
    def generateTrees(self, n):
        """

        :param n:
        :return:
        """
        import itertools
        nums = [i for i in range(1, n+1)]
        nums = itertools.permutations([nums])
        pass













