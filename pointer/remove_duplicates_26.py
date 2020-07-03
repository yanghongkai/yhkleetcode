# 26 删除排序数组中的重复项  https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slow, fast
        slow = 0
        fast = 1

        if len(nums) < 2:
            return len(nums)
        if len(nums) == 2:
            if nums[0] != nums[1]:
                return 2
            else:
                return 1

        while fast < len(nums):
            if nums[fast] == nums[slow]:
                fast += 1
            else:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(Solution().removeDuplicates(nums))
