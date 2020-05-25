
# 714 买卖股票的最佳时机含手续费 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # 相当于买入股票的价格上升了
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i] - fee)

        return dp_i_0


prices = [1, 3, 2, 8, 4, 9]
fee = 2
s = Solution()
print(s.maxProfit(prices, fee))



