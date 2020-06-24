
# 47 全排列II https://leetcode-cn.com/problems/permutations-ii/

from typing import List
import copy


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 回溯法遍历
        track = []  # track 存储索引, 索引不会重复
        res = []

        def backtrack(nums, track):
            # track 路径
            # nums 和 track 共同决定选择列表

            # 终止条件
            if len(track) == len(nums):
                tmp_arr = [nums[i] for i in copy.copy(track)]
                if tmp_arr not in res:
                    res.append(tmp_arr)
                return

            for idx, item in enumerate(nums):
                if idx in track:
                    continue
                track.append(idx)
                backtrack(nums, track)
                track.pop()

        backtrack(nums, track)
        return res


nums = [1, 1, 2]
print(Solution().permuteUnique(nums))



