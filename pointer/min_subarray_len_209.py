# 209 长度最小的子数组  https://leetcode-cn.com/problems/minimum-size-subarray-sum/

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 滑动窗口
        left = 0
        right = 0
        valid = 0
        length = float("inf")
        start = 0

        while right < len(nums):
            c = nums[right]
            right += 1
            valid += c

            while valid >= s:
                if right - left < length:
                    start = left
                    length = right - left

                d = nums[left]
                left += 1
                valid -= d

        if length != float("inf"):
            return length
        else:
            return 0


nums = [2, 3, 1, 2, 4, 3]
print(Solution().minSubArrayLen(7, nums))



