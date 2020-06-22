
# 213 打家劫舍II https://leetcode-cn.com/problems/house-robber-ii/

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 房屋是一个圈
        # 首尾房间不能同时被抢，三种情况: 1）要么都不被抢 2）要么第一间房子被抢最后一间不抢 3）要么最后一间房子被抢第一间不抢
        if len(nums) == 1:
            return nums[0]
        nums_first = nums[0:len(nums)-1]
        nums_last = nums[1:len(nums)]
        return max(self._rob_house(nums_first), self._rob_house(nums_last))

    def _rob_house(self, nums):
        """从某个房间开始抢"""
        # dp[i] 从第i间房开始抢，最多可以抢多少钱
        dp = [0] * (len(nums)+2)
        dp[len(nums)] = 0  # 最后2个开始抢为0，因为没有房间了
        for i in range(len(nums)-1, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])

        return dp[0]


nums = [1, 2, 3, 1]
print(Solution().rob(nums))




