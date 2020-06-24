
# 216 组合总和III  https://leetcode-cn.com/problems/combination-sum-iii/

from typing import List
import copy


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # 回溯法遍历

        track = []
        res = []

        def backtrack(start, track):
            # n, start 决定选择列表
            # 终止条件
            if sum(track) == n and len(track) == k:
                res.append(copy.copy(track))
                return

            if sum(track) > n or len(track) > k:
                return

            for i in range(start, 9+1, 1):
                track.append(i)
                backtrack(i+1, track)
                track.pop()

        backtrack(1, track)
        return res


print(Solution().combinationSum3(3, 9))









