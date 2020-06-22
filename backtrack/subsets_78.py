
# 78 子集  https://leetcode-cn.com/problems/subsets/

from typing import List
import copy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯法
        res = []
        track = []
        def trackback(nums, start, track):
            # track表示路径，nums 和 start 决定选择列表
            res.append(copy.copy(track))
            for i in range(start, len(nums), 1):
                track.append(nums[i])
                trackback(nums, i+1, track)
                track.pop()

        trackback(nums, 0, track)
        return res


nums = [1, 2, 3]
print(Solution().subsets(nums))








