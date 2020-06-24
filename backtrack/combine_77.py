
# 77 组合  https://leetcode-cn.com/problems/combinations/

from typing import List
import copy


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        track = []
        def backtrack(n, start, track):
            if len(track) == k:
                res.append(copy.copy(track))
                return
            for i in range(start, n+1, 1):
                track.append(i)
                backtrack(n, i+1, track)
                track.pop()

        backtrack(n, 1, track)
        return res


print(Solution().combine(4, 2))








