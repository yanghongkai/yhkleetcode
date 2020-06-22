
# 34 在排序数组中查找元素的第一个和最后一个位置  https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> int:
        left, right = self.left_bound(nums, target), self.right_bound(nums, target)
        return [left, right]

    def left_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        # [left, right) 终止条件 left==right
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        if left == len(nums):
            return -1
        if nums[left] == target:
            return left
        else:
            return -1

    def right_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        if left == 0:
            return -1
        if nums[left - 1] == target:
            return left - 1
        else:
            return -1


class Solution1:
    def searchRange(self, nums: List[int], target: int) -> int:
        left, right = self.left_bound(nums, target), self.right_bound(nums, target)
        return [left, right]

    def left_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # [left, right) 终止条件 left=right + 1
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                right = mid - 1  # [left, mid-1]
            elif nums[mid] < target:
                left = mid + 1  # [mid+1, right]
            elif nums[mid] > target:
                right = mid - 1  # [left, mid-1]

        if left >= len(nums):
            return -1
        if nums[left] == target:
            return left
        else:
            return -1


    def right_bound(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        if right < 0:
            return -1
        if nums[right] == target:
            return right
        else:
            return -1

nums = [5, 7, 7, 8, 8, 10]
target = 8
print(Solution1().searchRange(nums, target))










