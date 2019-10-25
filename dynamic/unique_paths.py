
# 62 不同路径 https://leetcode-cn.com/problems/unique-paths/


class Solution:
    def uniquePaths(self, m, n):
        """
        cell[i][j] = cell[i-1][j] 向下走 + cell[i][j-1] 向右走
        m 表示列， n表示行
        :param m:
        :param n:
        :return:
        """
        cell = [[0]*m for i in range(n)]
        cell[0][0] = 1
        for i in range(n):
            for j in range(m):
                if not (i==0 and j==0):
                    cell[i][j] = (cell[i-1][j] if i>=1 else 0)  + (cell[i][j-1] if j>=1 else 0)
        return cell[n-1][m-1]


m = 7
n =3
# 28
s = Solution()
print(s.uniquePaths(m, n))











