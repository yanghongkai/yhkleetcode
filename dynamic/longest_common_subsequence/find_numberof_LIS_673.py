# 673 最长递增子序列的个数  https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/

from typing import List
import copy


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # nums = [1, 3, 5, 4, 7] -> [1, 2, 3, 3, 4]
        # dp[i] 表示以nums[i]结尾的最大长度 dp[i] = (x, [prev_idx])
        dp = [[1, [i]] for i in range(len(nums))]
        max_val = 0
        max_idx = 0
        max_idx_arr = []
        for i in range(0, len(nums), 1):
            for j in range(0, i, 1):
                if nums[j] < nums[i]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = [j]
                    if dp[j][0] + 1 == dp[i][0]:
                        if j not in dp[i][1]:
                            dp[i][1].append(j)
            if dp[i][0] > max_val:
                max_val = dp[i][0]
                max_idx = i
                max_idx_arr = [i]
            if dp[i][0] == max_val:
                if i not in max_idx_arr:
                    max_idx_arr.append(i)

        # print(dp)
        # print(max_idx)
        # print(max_idx_arr)

        # 遍历路径
        res = []
        track = []

        def backtrack(dp,  start, track):
            # print("start:", start)
            # 终止条件 len(track) == max_val
            if len(track) == max_val-1:
                res.append(copy.copy(track))
                return

            arr = dp[start][1]
            for i in arr:
                track.append(i)
                backtrack(dp, i, track)
                track.pop()
        for idx in max_idx_arr:
            backtrack(dp, idx, track)
        return len(res)




# nums = [1, 3, 5, 4, 7]
nums = [1, 2, 4, 3, 5, 4, 7, 2]
print(Solution().findNumberOfLIS(nums))
