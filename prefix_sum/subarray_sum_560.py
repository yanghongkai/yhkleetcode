
# 560 和为K的子数组  https://leetcode-cn.com/problems/subarray-sum-equals-k/

from typing import List
import collections


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
        # print(pre_sum)

        count = 0
        for j in range(1, len(nums)+1, 1):
            for i in range(0, j, 1):
                # print("[{},{}]={}".format(i, j-1, pre_sum[j] - pre_sum[i]))
                if pre_sum[j] - pre_sum[i] == k:
                    count += 1

        return count

    def subarraySum1(self, nums: List[int], k: int) -> int:
        pre_sum = collections.defaultdict(int)
        # base case
        pre_sum[0] = 1
        cur_sum = 0
        count = 0
        for j in range(len(nums)):
            cur_sum += nums[j]
            sum_i = cur_sum - k
            if sum_i in pre_sum:
                count += pre_sum[sum_i]
            pre_sum[cur_sum] += 1

        return count


nums = [1, 1, 1]
# nums = [3, 5, 2, -2, 4, 1]
k = 2
# print(Solution().subarraySum(nums, k))
print(Solution().subarraySum1(nums, k))



