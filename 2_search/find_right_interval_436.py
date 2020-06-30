
# 436 寻找右区间  https://leetcode-cn.com/problems/find-right-interval/

from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # 排序，再二分查找
        arr = []
        for i, item in enumerate(intervals):
            arr.append([item[0], i])
        arr.sort(key=lambda x: x[0])

        def binary_search(left, right, target):
            while left <= right:
                mid = int((left + right)/2)
                if arr[mid][0] == target:
                    left = mid
                    break
                elif arr[mid][0] < target:
                    left = mid + 1
                elif arr[mid][0] > target:
                    right = mid - 1

            if left >= len(arr):
                return -1
            if arr[left][0] >= target:
                return arr[left][1]
            else:
                return -1

        res = []
        for item in intervals:
            res.append(binary_search(0, len(arr)-1, item[1]))

        return res


intervals = [[3, 4], [2, 3], [1, 2]]
# intervals = [[1, 4], [2, 3], [3, 4]]
print(Solution().findRightInterval(intervals))








