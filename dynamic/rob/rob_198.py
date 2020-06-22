
# 198 打家劫舍 https://leetcode-cn.com/problems/house-robber/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        # dp[i] 前i间房做多偷多少钱
        dp = [0] * (len(nums) + 1)
        # base case
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(2, len(nums)+1):
            dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])

        return dp[len(nums)]


# nums = [2, 7, 9, 3, 1]
# print(Solution().rob(nums))


class Solution1:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        # dp[i] 从第i间房开始抢，最多可以抢多少钱
        dp = [0] * (len(nums)+1)
        dp[len(nums)] = 0  # 最后一个的下一个开始抢为0，因为没有房间了
        dp[len(nums)-1] = nums[len(nums)-1]  # 最后一个开始抢，
        for i in range(len(nums)-1-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])

        return dp[0]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        """
        推荐
        Args:
            nums:

        Returns:

        """
        if len(nums) < 1:
            return 0
        # dp[i] 从第i间房开始抢，最多可以抢多少钱
        dp = [0] * (len(nums)+2)
        dp[len(nums)] = 0  # 最后2个开始抢为0，因为没有房间了
        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])

        return dp[0]


nums = [2, 7, 9, 3, 1]
print(Solution2().rob(nums))





