
# 零钱兑换II 518  https://leetcode-cn.com/problems/coin-change-2/

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 背包问题，dp[i][j] 前i个硬币，amount=j 的组合数
        dp = [[0 for j in range(amount+1)] for i in range(len(coins)+1)]
        # base case
        # dp[0][..] = 0 dp[..][0] = 1
        for item in dp:
            item[0] = 1
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                # 硬币放不进来
                if j - coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    # 选择不放进来 或放进来
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]

        return dp[len(coins)][amount]


amount = 5
coins = [1, 2, 5]
s = Solution()
print(s.change(amount, coins))







