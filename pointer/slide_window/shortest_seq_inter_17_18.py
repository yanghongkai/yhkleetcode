# 面试题 17.18 最短超串  https://leetcode-cn.com/problems/shortest-supersequence-lcci/

from typing import List
import collections


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        # 滑动窗口 left, right
        window = collections.defaultdict(int)
        need = collections.defaultdict(int)
        for item in small:
            need[item] += 1

        left = 0
        right = 0
        valid = 0
        length = float("inf")
        start = 0
        while right < len(big):
            c = big[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(small):
                if right - left < length:
                    start = left
                    length = right - left

                d = big[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        if length != float("inf"):
            return [start, start+length-1]
        else:
            return []


big = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
small = [1, 5, 9]
print(Solution().shortestSeq(big, small))
