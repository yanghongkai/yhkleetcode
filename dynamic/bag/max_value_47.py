
# 剑指offer47 礼物的最大价值 https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/

from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)  # 行
        n = len(grid[0])  # 列
        # dp[i][j] 到达i,j位置时的最大价值
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        # base case dp[0][..] = 0 dp[..][0] = 0
        for i in range(1, m+1, 1):
            for j in range(1, n+1, 1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

        return dp[m][n]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(Solution().maxValue(grid))





