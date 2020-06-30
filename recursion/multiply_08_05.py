
# 面试题 08.05 递归乘法  https://leetcode-cn.com/problems/recursive-mulitply-lcci/


class Solution:
    def multiply(self, A: int, B: int) -> int:

        n = min(A, B)
        factor = max(A, B)

        def f(n):
            if n == 0:
                return 0
            return f(n-1) + factor

        return f(n)


A = 3
B = 4
print(Solution().multiply(A, B))










