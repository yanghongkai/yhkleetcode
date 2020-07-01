
# 面试题 17.14 最小K个数  https://leetcode-cn.com/problems/smallest-k-lcci/

from typing import List
import random


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        # partition 每次能排定一个元素，并且还能够知道这个元素它最终所在的位置

        def partition(arr, left, right):
            random_idx = random.randint(left, right)
            arr[left], arr[random_idx] = arr[random_idx], arr[left]

            pivot = arr[left]

            while left < right:
                while left < right and arr[right] > pivot:
                    right -= 1
                arr[left] = arr[right]

                while left < right and arr[left] <= pivot:
                    left += 1
                arr[right] = arr[left]

            arr[left] = pivot
            return left

        if k == 0:
            return []

        target = k - 1

        left = 0
        right = len(arr) - 1

        while True:
            index = partition(arr, left, right)
            if index == target:
                return arr[:index+1]
            elif index < target:
                left = index + 1
            elif index > target:
                right = index - 1


arr = [1, 3, 5, 7, 2, 4, 6, 8]
k = 4
arr = [1, 2, 3]
k = 1
print(Solution().smallestK(arr, k))


