
# 面试题 0804 幂集  https://leetcode-cn.com/problems/power-set-lcci/

from typing import List
import copy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 子集问题 用 start 指针

        res = []
        track = []

        def backtrack(nums, start, track):
            # nums 和 start 决定选择列表
            res.append(copy.copy(track))
            for i in range(start, len(nums), 1):
                track.append(nums[i])
                backtrack(nums, i+1, track)
                track.pop()

        backtrack(nums, 0, track)
        return res


nums = [1, 2, 3]
print(Solution().subsets(nums))




