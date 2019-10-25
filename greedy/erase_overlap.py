# 435 无重叠区间 https://leetcode-cn.com/problems/non-overlapping-intervals/

# Q: 耗时太久
from collections import defaultdict


class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        1. 每次找出能使overlap最多的元素删掉
        并不要求有全集的概念
        没有解决以下这种情况:
        # intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
        :param intervals:
        :return:
        """
        overlaps = self.cac_overlaps(intervals)
        print("overlaps:", overlaps)
        # 不需要合并重叠区间
        used = []
        # 每次寻找覆盖最多的重叠区间
        while overlaps:
            # 计算每个item与overlaps交集的数量,找出交集最多的
            # 不能从interval 里筛选，只能从多余的里边筛选
            idx, arrs = self.find_cover_max(overlaps, intervals)
            # 0 和 None 都是False
            if idx < 0:
                break
            used.append(idx)
            print("pop:", intervals[idx])
            intervals.pop(idx)
            overlaps = self.cac_overlaps(intervals)
            # for arr in arrs:
            #     if arr in overlaps:
            #         overlaps.remove(arr)
            print("used:", used)
        if not overlaps:
            return len(used)

    def cac_overlaps(self, intervals):
        """
        计算intervals中的overlaps
        :param intervals:
        :return:
        """
        # overlaps 表示当前重叠的范围
        # cur_scope 表示当前所覆盖的范围
        cur_scope = []
        overlaps = []
        for arr in intervals:
            # 判断item是否与当前的范围有overlap
            for scope in cur_scope:
                if arr[0] <= scope[-1]:
                    overlap_s = max(scope[0], arr[0])
                    overlap_e = min(scope[-1], arr[-1])
                    tmp = [overlap_s, overlap_e]
                    # 多个重复的重叠区域也要
                    if overlap_e > overlap_s:
                        overlaps.append(tmp)
            cur_scope.append(arr)
            if cur_scope:
                cur_scope = self.merge(cur_scope)
        return overlaps

    def find_cover_max(self, overlaps, intervals):
        """

        :param overlaps:
        :param internals:
        :return:
        """
        item_dict = defaultdict(list)
        for idx, item in enumerate(intervals):
            print("idx:", idx)
            print("item:", item)
            for arr in overlaps:
                if arr[0] >= item[0] and arr[-1] <= item[-1]:
                    # 避免相同区域，重复计数，因为一个集合只能覆盖一次
                    if arr not in item_dict[idx]:
                        item_dict[idx].append(arr)
        print("item_dict:", item_dict)
        if item_dict:
            sorted_items = sorted(item_dict.items(), key=lambda x: len(x[1]), reverse=True)
            idx, arrs = sorted_items[0]
            return idx, arrs
        else:
            return -1, None

    def merge(self, arrs):
        """
        合并区间
        :param arrs:
        :return:
        """
        res = []
        list.sort(arrs, key=lambda x: x[0])
        i = 0
        while i < len(arrs):
            if i + 1 <= len(arrs) - 1 and arrs[i + 1][0] <= arrs[i][-1]:
                tmp = [arrs[i][0], max(arrs[i][-1], arrs[i + 1][-1])]
                i += 2
                while i <= len(arrs) - 1 and arrs[i][0] <= tmp[-1]:
                    tmp[-1] = max(arrs[i][-1], tmp[-1])
                    i += 1
                res.append(tmp)
            else:
                res.append(arrs[i])
                i += 1
        return res


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
intervals = [[1, 2], [1, 2], [1, 2]]
# intervals = [[1, 2], [2, 3]]
intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]
s = Solution()
print(s.eraseOverlapIntervals(intervals))
