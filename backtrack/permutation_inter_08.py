
# 面试题 08.08 有重复字符串的排列组合  https://leetcode-cn.com/problems/permutation-ii-lcci/

from typing import List
import copy


class Solution:
    def permutation(self, S: str) -> List[str]:
        # 带重复数字的全排列问题

        res = []
        track = []

        def backtrack(nums, track):
            # 终止条件
            if len(track) == len(nums):
                tmp_arr = "".join([nums[i] for i in copy.copy(track)])
                if tmp_arr not in res:
                    res.append(tmp_arr)
                return

            for i in range(len(nums)):
                if i in track:
                    continue
                track.append(i)
                backtrack(nums, track)
                track.pop()

        backtrack(S, track)
        return res


S = "qqe"
print(Solution().permutation(S))







