# 56 合并区间 https://leetcode-cn.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals):
        """

        :param intervals:
        :return:
        """
        # 先按左边界进行排序
        list.sort(intervals, key=lambda x: x[0])
        # print(intervals)
        res = []
        i = 0
        # 排序之后，只用考虑相邻的能不能合并，如果相邻的不能合并，那么其他的肯定不能合并
        while i <= len(intervals)-1:
            # print("i:", i)
            # 如果能合并, 需要将将合并后的元素继续和后续进行比较
            if i+1 <=len(intervals)-1 and intervals[i][-1] >= intervals[i+1][0]:
                tmp = []
                tmp.append(intervals[i][0])
                # 考虑到包含关系 [1,4], [2,3]
                tmp.append(max(intervals[i][-1], intervals[i+1][-1]))
                i += 2
                while i <= len(intervals)-1 and tmp[-1] >= intervals[i][0]:
                    tmp[-1] = max(tmp[-1], intervals[i][-1])
                    i += 1
                res.append(tmp)
            else:  # 不能合并
                res.append(intervals[i])
                i += 1
        return res




s = Solution()
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[1, 3], [8, 10], [2, 6], [15, 18]]
# intervals = [[1,4],[4,5]]
# 包含关系
intervals = [[1,4],[2,3]]
intervals = [[1,4],[0,2],[3,5]]
print(s.merge(intervals))
