
# 72 编辑距离 https://leetcode-cn.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1, word2) -> int:
        """
        第一行，第一列单独操作
        a[i]!=b[j]:
            cell[i][j] = cell[i][j-1] + 1 插入 b[j]
            cell[i][j] = cell[i-1][j] +1 删除 a[i]
            cell[i][j] = cell[i-1][j-1] +1 a[i]->b[j]
        a[i] = b[j]:
            cell[i][j] = cell[i-1][j-1]
        :param word1:
        :param word2:
        :return:
        """
        if not len(word1) or not len(word2):
            return max(len(word1), len(word2))
        # 操作
        cell = [[0]*(len(word2)+1) for i in range((len(word1)+1))]
        # 第一行
        for j in range(1, len(word2)+1):
            cell[0][j] = cell[0][j-1] + 1
        # 第一列
        for i in range(1, len(word1)+1):
            cell[i][0] = cell[i-1][0] + 1

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] != word2[j-1]:
                    cell[i][j] = min(cell[i][j-1], cell[i-1][j], cell[i-1][j-1]) + 1
                else:
                    cell[i][j] = cell[i-1][j-1]
        # print(ops)
        return cell[-1][-1]


word1 = "horse"
word2 = "ros"
word1 = "sea"
word2 = "eat"
word1 = "ab"
word2 = "a"
s = Solution()
print(s.minDistance(word1, word2))



