
# 162 寻找峰值  https://leetcode-cn.com/problems/find-peak-element/

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 沿着数值大的一侧一定有峰值 [mid] [mid+1]

        left = 0
        right = len(nums) - 1
        nums.append(float("-inf"))

        while left <= right:
            mid = int((left + right)/2)
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            elif nums[mid] == nums[mid+1]:
                right = mid - 1
            elif nums[mid] > nums[mid+1]:
                right = mid - 1

        return left


nums = [1, 2, 3, 1]
nums = [1]
print(Solution().findPeakElement(nums))





