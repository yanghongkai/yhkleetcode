
# 剑指 Offer 10-1 斐波那契数列  https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/


class Solution:
    memo = {}

    def fib(self, n: int) -> int:

        # base case
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n in self.memo:
            return self.memo[n]
        else:
            res = self.fib(n-1) + self.fib(n-2)
            res = res % 1000000007
            if n not in self.memo:
                self.memo[n] = res
            return res


print(Solution().fib(45))
exit()


class Solution1:
    def fib(self, n: int) -> int:
        # base case
        if n <= 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)

n = 45
print(Solution1().fib(n))






