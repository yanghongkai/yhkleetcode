
# 279. 完全数平方  https://leetcode-cn.com/problems/perfect-squares/

# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

# solution
# 1. 状态
# 2. dp dp(n)
# 3. 选择 1+dp(n-coin)
# 4. base dp(0)=0
# dp[i] = min(dp[i], 1+dp[i-coin])

import math


class Solution:
    def numSquares(self, n: int) -> int:
        # 初始化为n+1, 最大值理论上是n, 因此n+1相当于初始为无穷大
        dp = [n+1] * (n+1)
        dp[0] = 0
        for i in range(1, len(dp), 1):
            # i [1,n]
            for coin in range(1, math.ceil(math.sqrt(n))+1, 1):
                if i-coin*coin < 0:
                    continue
                dp[i] = min(dp[i], 1+dp[i-coin*coin])
        return dp[n]

s = Solution()
print("num:", s.numSquares(7168))


