
# 分割等和子集 416  https://leetcode-cn.com/problems/partition-equal-subset-sum/

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 背包问题，背包重量 sum/2, 物品1-n
        if sum(nums)%2 != 0:
            return False
        m = int(sum(nums) / 2)
        # base case
        # dp[..][0] = True, dp[0][..] = False
        dp = [[False for j in range(m+1)] for i in range(len(nums)+1)]
        for item in dp:
            item[0] = True
        # print(dp)
        for i in range(1, len(nums)+1):
            for j in range(1, m+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    # 选择: 不放进去 和 放进去 两种情况
                    dp[i][j] = dp[i-1][j] | dp[i-1][j - nums[i-1]]

        return dp[len(nums)][m]


nums = [1, 5, 11, 5]
s = Solution()
print(s.canPartition(nums))











