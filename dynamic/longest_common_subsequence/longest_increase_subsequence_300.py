
# 最长上升子序列 300

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in len(nums)]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # base case
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j], dp[j]+1)
        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
s = Solution1()
print(s.lengthOfLIS(nums))









