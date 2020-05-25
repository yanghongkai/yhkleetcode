# 309 最佳买卖股票时机含冷冻期  https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        dp_pre_0 = 0
        for i in range(len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
            dp_pre_0 = tmp

        return dp_i_0


prices = [1, 2, 3, 0, 2]
s = Solution()
print(s.maxProfit(prices))
