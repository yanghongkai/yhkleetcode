# 72 编辑距离 https://leetcode-cn.com/problems/edit-distance/


class Node:
    def __init__(self, val=0, op=0):
        self.val = val
        # 0: no op skip a[i]==b[j]
        # 1: add  cell[i][j-1]
        # 2: delete left cell[i-1][j]
        # 3: replace cell[i-1][j-1]
        self.op = op


class Solution:
    def minDistance(self, word1, word2) -> int:
        """
        a[i]!=b[j]:
            cell[i][j] = cell[i][j-1] + 1 插入 b[j]
            cell[i][j] = cell[i-1][j] +1 删除 a[i]
            cell[i][j] = cell[i-1][j-1] +1 a[i]->b[j]
        a[i] = b[j]:
            cell[i][j] = cell[i-1][j-1]
            if cell[i-1][j-1]不存在，从 cell[i][j-1] cell[i-1][j], cell[i-1][j-1]中找一个最小的
        base: cell[m+1][n+1]
        :param word1:
        :param word2:
        :return:
        """
        if not len(word1) or not len(word2):
            return max(len(word1), len(word2))
        # 操作
        m = len(word1)
        n = len(word2)
        cell = [[Node() for j in range(n + 1)] for i in range(m + 1)]
        # base
        # 第一行
        for j in range(1, n + 1, 1):
            cell[0][j].val = j
            cell[0][j].op = 1  # add

        # 第一列
        for i in range(1, m + 1, 1):
            cell[i][0].val = i
            cell[i][0].op = 2  # delete

        for i in range(1, m + 1, 1):
            for j in range(1, n + 1, 1):
                op = 0
                add = cell[i][j - 1].val
                delete = cell[i - 1][j].val
                replace = cell[i - 1][j - 1].val
                min_val = min([add, delete, replace])
                if add == min_val:
                    op = 1
                if delete == min_val:
                    op = 2
                if replace == min_val:
                    op = 3
                if word1[i - 1] == word2[j - 1]:
                    cell[i][j].val = min_val
                    op = 0  # no op
                else:
                    cell[i][j].val = min_val + 1
                cell[i][j].op = op

        path = []
        i = m
        j = n
        while i != 0 and j != 0:
            op = cell[i][j].op
            op_str = ""
            if op == 0:
                i = i-1
                j = j-1
            if op == 1:
                op_str = "add {}".format(word2[j-1])
                j = j-1
            if op == 2:
                op_str = "delete {}".format(word1[i-1])
                i = i-1
            if op == 3:
                op_str = "replace {} -> {}".format(word1[i-1], word2[j-1])
                i = i - 1
                j = j - 1
            if op_str:
                path.insert(0, op_str)

        print("path:", path)

        return cell[m][n].val


word1 = "horse"
word2 = "ros"
word1 = "intention"
word2 = "execution"
# word1 = "sea"
# word2 = "eat"
# word1 = "ab"
# word2 = "a"
s = Solution()
print(s.minDistance(word1, word2))
