
# 90 子集II https://leetcode-cn.com/problems/subsets-ii/

from typing import List
import copy


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 子集 回溯
        track = []
        res = []

        def backtrack(nums, start, track):
            # nums, start 共同决定 选择列表
            res.append(copy.copy(track))

            # res.append(copy.copy(track))
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i+1, track)
                track.pop()

        backtrack(nums, 0, track)
        for item in res:
            list.sort(item)
        list.sort(res)
        tmp_res = []
        pre = None
        for idx in range(len(res)):
            if res[idx] != pre:
                tmp_res.append(res[idx])
            pre = res[idx]
        return tmp_res


nums = [1, 2, 2]
nums = [4,4,4,1,4]
print(Solution().subsetsWithDup(nums))








