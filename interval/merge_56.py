# 56 合并区间  https://leetcode-cn.com/problems/merge-intervals/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 1:
            return intervals
        # 先进行排序,按照start
        intervals.sort(key=lambda x: x[0])
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            cur = intervals[i]
            last = res[-1]
            if cur[0] <= last[1]:
                last[1] = max(last[1], cur[1])
            else:
                res.append(cur)

        return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = []
print(Solution().merge(intervals))

