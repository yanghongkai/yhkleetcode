
# 用最少数量的箭引爆气球 452  https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) < 1:
            return 0
        # 根据end元素进行递增排序
        points = sorted(points, key=lambda x: x[1])
        # 取区间x中结束最早的
        x_end = points[0][1]
        count = 1
        for item in points:
            if item[0] > x_end:
                x_end = item[1]
                count += 1

        return count


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
s = Solution()
print(s.findMinArrowShots(points))







