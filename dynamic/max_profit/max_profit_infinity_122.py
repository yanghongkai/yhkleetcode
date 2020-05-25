# 122. 买卖股票的最佳时机 k=+infinity https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0


prices = [7, 1, 5, 3, 6, 4]
s = Solution()
print(s.maxProfit(prices))
