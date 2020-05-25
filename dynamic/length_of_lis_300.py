# 300 lengthOfLIS 最长上升子序列 https://leetcode-cn.com/problems/longest-increasing-subsequence/

# dp[i] 表示以nums[i]这个数结尾的最长递增子序列的长度
# 状态转移方程
# for i in range(n):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], dp[j]+1)
# base dp[i]=1 for i in range(n)


class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) < 1:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
s = Solution()
print(s.lengthOfLIS(nums))
