
# 剑指offer 16 数值的整数次方  https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def f(x, n):
            if n == 0:
                return 1

            # 如果是奇数
            if n % 2 != 0:
                return f(x, n-1) * x
            else:
                return f(x*x, n//2)
        if n > 0:
            return f(x, n)
        elif n == 0:
            return f(x, n)
        elif n < 0:
            return 1. / f(x, -n)


print(Solution().myPow(2.0, 10))
print(Solution().myPow(2.0, -2))

