
# 509 斐波那契数列  https://leetcode-cn.com/problems/fibonacci-number/


class Solution:
    memo = {}

    def fib(self, N: int) -> int:
        # base case
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N in self.memo:
            return self.memo[N]
        else:
            res = self.fib(N-1) + self.fib(N-2)
            if N not in self.memo:
                self.memo[N] = res
            return res


class Solution1:
    def fib(self, N: int) -> int:
        # dp[i] 表示 i 时的值
        dp = [0 for i in range(N+1)]
        # base case
        # dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, N+1, 1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[N]


class Solution2:
    def fib(self, N: int) -> int:
        # dp[i] 表示 i 时的值
        dp = [0 for i in range(N+1)]
        # base case
        # dp[0] = 0
        prev_1 = 1
        prev_2 = 1
        for i in range(3, N+1, 1):
            dp[i] = dp[i-1] + dp[i-2]
            sum = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = sum

        return sum


print(Solution2().fib(4))



