# 930 和相同的二元子数组  https://leetcode-cn.com/problems/binary-subarrays-with-sum/

from typing import List
import collections


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        # 前缀和
        pre_sum = [0] * (len(A) + 1)
        for i in range(len(A)):
            pre_sum[i+1] = pre_sum[i] + A[i]

        # print(pre_sum)
        count = 0

        for j in range(1, len(A)+1, 1):
            for i in range(0, j, 1):
                if pre_sum[j] - pre_sum[i] == S:
                    count += 1

        return count

    def numSubarraysWithSum1(self, A: List[int], S: int) -> int:
        # 前缀和
        pre_sum = collections.defaultdict(int)
        pre_sum[0] = 1
        cur_sum = 0
        count = 0
        for j in range(len(A)):
            cur_sum += A[j]
            sum_i = cur_sum - S
            if sum_i in pre_sum:
                count += pre_sum[sum_i]
            pre_sum[cur_sum] += 1

        # print(pre_sum)

        return count


A = [1, 0, 1, 0, 1]
S = 2
print(Solution().numSubarraysWithSum1(A, S))


