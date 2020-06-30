
# 1. 两数之和  https://leetcode-cn.com/problems/two-sum/

from typing import List






class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力法
        for i in range(len(nums)):
            for j in range(i+1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        # 通过哈希表减少时间复杂度
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            other = target - nums[i]
            if other in d and d[other] != i:
                return [i, d[other]]

        return [-1, -1]


    def twoSum_9(self, nums: List[int], target: int) -> List[int]:
        # 只有 nums 是个递增序列才可以
        list.sort(nums)
        # left, right 双指针
        left = 0
        right = len(nums) - 1

        while left <= right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left, right]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1

    class TwoSum:
        # 记录 number 出现的次数
        freq = {}

        def add(self, number):
            """向数据结构中添加一个数 number"""
            self.freq[number] = self.freq.get(number, 0) + 1

        def find(self, value):
            """寻找当前数据结构中是否存在两个数的和为 value"""
            for k in self.freq.keys():
                other = value - k
                if other == k and self.freq.get(k) > 1:
                    return True
                if other != k and other in self.freq.keys():
                    return True

            return False


nums = [2, 7, 11, 15]
target = 9
nums = [3, 2, 4]
target = 6
print(Solution().twoSum_1(nums, target))



