
# 215 数组中的第K个最大元素  https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # partition 每次都能排定一个元素，并且还能够知道这个元素它最终所在的位置

        def partition(nums, left, right):
            # 取随机pivot
            random_idx = random.randint(left, right)
            nums[left], nums[random_idx] = nums[random_idx], nums[left]
            pivot = nums[left]

            while left < right:
                while left < right and nums[right] > pivot:
                    right -= 1
                nums[left] = nums[right]

                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]

            nums[left] = pivot
            return left

        target = len(nums) - k
        # print("target:", target)
        left = 0
        right = len(nums) - 1

        while True:
            index = partition(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                left = index + 1
            elif index > target:
                right = index - 1


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(Solution().findKthLargest(nums, k))


