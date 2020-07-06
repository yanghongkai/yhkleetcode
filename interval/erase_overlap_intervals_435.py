# 无重叠区间 435  https://leetcode-cn.com/problems/non-overlapping-intervals/

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 1:
            return 0
        # 对二维数组按照end进行排序
        intervals = sorted(intervals, key=lambda x: x[-1])
        # print(intervals)
        # 取出某个区间中最早结束的end
        x_end = intervals[0][1]
        count = 1
        for item in intervals:
            # start大于end的才不会重叠
            if item[0] >= x_end:
                x_end = item[1]
                count += 1
        # print(len(intervals) - count)
        return len(intervals) - count


inters = [[1, 2], [2, 3], [3, 4], [1, 3]]
s = Solution()
s.eraseOverlapIntervals(inters)