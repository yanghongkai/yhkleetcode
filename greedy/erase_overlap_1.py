# 435 无重叠区间 https://leetcode-cn.com/problems/non-overlapping-intervals/

# 贪心算法: 每次确保留下最多的可用空间


class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        先对list进行排序，每次确保留下最多的空间即可
        :param intervals:
        :return:
        """
        list.sort(intervals, key=lambda x: x[0])
        print(intervals)
        prev = 0
        used = []
        i = 1
        while i < len(intervals):
            # case [1,2] [2,3]
            if intervals[i][0] >= intervals[prev][-1]:
                prev = i
            # case [1,100], [11,12]
            elif max(intervals[i][0], intervals[i][-1]) <= intervals[prev][-1]:
                # delete i
                used.append(intervals[prev])
                prev = i
            # case [1,11], [2,12]
            elif intervals[i][0] < intervals[prev][-1] and intervals[i][-1] > intervals[prev][-1]:
                used.append(intervals[i])
            i += 1
        print("used:", used)
        return len(used)

intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
# intervals = [[1, 2], [1, 2], [1, 2]]
# intervals = [[1, 2], [2, 3]]
# intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
s = Solution()
print(s.eraseOverlapIntervals(intervals))
