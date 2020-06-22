
# 面试题 08.11 硬币  https://leetcode-cn.com/problems/coin-lcci/


class Solution:
    def waysToChange(self, n: int) -> int:
        # 硬币无限 完全背包问题
        # dp[i][j] 前i个硬币金额为j最多有多少种表示法
        coins = [1, 5, 10, 25]
        dp = [[0 for j in range(n+1)] for i in range(len(coins)+1)]
        # base case
        # dp[0][...] = 0  dp[...][0] = 1
        for i in range(len(coins)+1):
            dp[i][0] = 1
        for i in range(1, len(coins)+1, 1):
            for j in range(1, n+1, 1):
                if j - coins[i-1] >= 0:  # 能装得下硬币i
                    dp[i][j] = dp[i][j - coins[i-1]] + dp[i-1][j]
                else:  # 装不下
                    dp[i][j] = dp[i-1][j]

        return dp[len(coins)][n]


n = 6
print(Solution().waysToChange(n))






