
# 53 最大子序和 https://leetcode-cn.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp[i] 定义为以nums[i]结尾的最大子数组之和
        dp = [0 for i in range(len(nums))]
        # base case
        dp[0] = nums[0]
        # 选择 1) 和相邻数组结合 2)独自作为一个子数组
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])

        return max(dp)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-1]
s = Solution()
print(s.maxSubArray(nums))




