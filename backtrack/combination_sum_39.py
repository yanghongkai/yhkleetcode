
# 39 组合总和 https://leetcode-cn.com/problems/combination-sum/

from typing import List
import copy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates 中的数字可以无限制重复地被选取 相当于 选择列表是 candidates

        track = []
        res = []

        def backtrack(candidates, track, start):
            # 选择列表 从当前位置开始向后遍历，包含当前位置
            # 终止条件
            if sum(track) == target:
                res.append(copy.copy(track))
                return
            if sum(track) > target:
                return

            for i in range(start, len(candidates), 1):
                track.append(candidates[i])
                backtrack(candidates, track, i)
                track.pop()

        backtrack(candidates,  track, 0)
        return res


candidates = [2, 3, 5]
target = 8
print(Solution().combinationSum(candidates, target))











