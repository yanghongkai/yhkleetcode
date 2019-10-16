#!/usr/bin/env python
# coding=utf-8

class Solution:
    def twoSum_ugly(self, nums, target):
        """

        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        res = []
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(nums[i])
                    res.append(nums[j])

        return res

    def twoSum(self, nums, target):
        """

        :param nums:
        :param target:
        :return:
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target-num in lookup:
                return [lookup[target-num], i]
            lookup[num] = i







