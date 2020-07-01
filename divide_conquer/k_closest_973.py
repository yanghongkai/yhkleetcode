
# 973 最接近原点的K个点  https://leetcode-cn.com/problems/k-closest-points-to-origin/

from typing import List
import random
import math


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        def cac_distance(a, b=[0., 0.]):
            return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

        # 先计算距离
        nums = [[cac_distance(item), idx] for idx, item in enumerate(points)]
        # print(nums)

        # partition 每次能排定一个元素，并且还能够知道这个元素它最终所在的位置
        def partition(nums, left, right):
            random_idx = random.randint(left, right)
            nums[left], nums[random_idx] = nums[random_idx], nums[left]

            pivot = nums[left][0]
            pivot_idx = nums[left][1]
            while left < right:
                while left < right and nums[right][0] > pivot:
                    right -= 1
                nums[left] = nums[right]

                while left < right and nums[left][0] <= pivot:
                    left += 1
                nums[right] = nums[left]

            nums[left] = [pivot, pivot_idx]
            return left

        if K == 0:
            return []

        target = K - 1
        left = 0
        right = len(nums) - 1

        while True:
            index = partition(nums, left, right)
            if index == target:
                return [points[item[1]] for item in nums[:index+1]]
            elif index < target:
                left = index + 1
            elif index > target:
                right = index - 1


points = [[1, 3], [-2, 2]]
K = 1
print(Solution().kClosest(points, K))






