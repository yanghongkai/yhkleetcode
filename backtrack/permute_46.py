
# 46 全排列  https://leetcode-cn.com/problems/permutations/

from typing import List
import copy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        track = []

        # 使用回溯法
        def backtrack(nums, track):
            if len(track) == len(nums):
                # print("add track:", track)
                res.append(copy.copy(track))
                return
            for item in nums:
                # 选择列表
                if item in track:
                    continue
                # 做选择
                track.append(item)
                # 进入下一层决策树
                backtrack(nums, track)
                # 取消选择
                track.pop()

        backtrack(nums, track)
        return res


nums = [1, 2, 3]
print(Solution().permute(nums))








