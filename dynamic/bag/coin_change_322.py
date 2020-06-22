
# 322 零钱兑换  https://leetcode-cn.com/problems/coin-change/

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        # dp[i] 凑成金额为 i 需要的最少的硬币个数
        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float("inf")
            for coin in coins:
                sub_problem = dp(n-coin)
                if sub_problem == -1:
                    continue
                res = min(res, sub_problem+1)

            memo[n] = res if res!= float("inf") else -1

            return memo[n]

        return dp(amount)


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] 凑成金额为 i 需要的最少的硬币个数
        # amount + 1 相当于正无穷
        dp = [amount+1 for i in range(amount+1)]
        # base case
        dp[0] = 0
        for i in range(1, amount+1, 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                else:
                    dp[i] = min(dp[i], dp[i-coin]+1)

        return -1 if dp[amount] == amount+1 else dp[amount]


coins = [1, 2, 5]
amout = 11
coins = [2]
amout = 3
coins = [1]
amout = 0
coins = [2, 5, 10, 1]
amout = 27
coins = [186, 419, 83, 408]
amout = 6249
print(Solution2().coinChange(coins, amout))




