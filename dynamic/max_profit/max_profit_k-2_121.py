# 121 买卖股票的最佳时机  https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_k = 2
        dp = [[[float("-inf") for s in range(2)] for k in range(max_k + 1)] for i in range(len(prices))]
        # for i in range(len(prices)):
        #     for k in range(max_k + 1):  # k 0, 1, ...k 方便直接返回k的索引，而非k-1的索引
        #         for s in range(2):
        #             dp[i][k][s] = float("-inf")
        for i in range(len(prices)):  # n
            for k in range(max_k, 0, -1):  # k
                if i-1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                else:
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        # print(dp)
        return dp[len(prices)-1][max_k][0]


prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
s = Solution()
print(s.maxProfit(prices))
