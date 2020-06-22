
# 718 最长重复子数组  https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/

from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        # dp[i][j] 子串A[:i]和B[:j]的最长子数组的长度
        dp = [[0 for j in range(len(B)+1)]for i in range(len(A)+1)]
        # base case
        # dp[...][0] = 0 dp[0][..] = 0
        res = 0
        for i in range(1, len(A)+1, 1):
            for j in range(1, len(B)+1, 1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > res:
                        res = dp[i][j]
                else:
                    dp[i][j] = 0

        return res


A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]
print(Solution().findLength(A, B))


