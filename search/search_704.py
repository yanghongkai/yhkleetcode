
# 704 二分查找  https://leetcode-cn.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1

        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(Solution().search(nums, target))



class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        pass

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


nums = [5, 7, 7, 8, 8, 10]
target = 6
print(Solution1().left_bound(nums, target))






