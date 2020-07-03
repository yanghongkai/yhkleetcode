
# 面试题 16.06 最小差  https://leetcode-cn.com/problems/smallest-difference-lcci/

from typing import List


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        # 排序 + 双指针
        # a: left, b: right if [left] < [right], left++ 每次比较小数加，直到一个数组遍历完毕
        a.sort()
        b.sort()
        left = 0
        right = 0
        res = float("inf")
        while left < len(a) and right < len(b):
            if a[left] > b[right]:
                ans = a[left] - b[right]
                if ans < res:
                    res = ans
                right += 1
            elif a[left] < b[right]:
                ans = b[right] - a[left]
                if ans < res:
                    res = ans
                left += 1
            elif a[left] == b[right]:
                return 0

        return res


a = [1, 3, 15, 11, 2]
b = [23, 127, 235, 19, 8]
print(Solution().smallestDifference(a, b))


