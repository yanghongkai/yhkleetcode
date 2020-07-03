# 80 删除排序数组中的重复项目 II  https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slow 指向要覆盖的元素, slow_pre,
        # fast 指向要遍历的元素
        if len(nums) <= 2:
            return len(nums)
        slow_pre = 0
        slow = 1
        fast = 2
        while fast < len(nums):
            if nums[fast] == nums[slow_pre]:
                fast += 1
            else:
                slow += 1
                slow_pre += 1
                nums[slow] = nums[fast]
                fast += 1

        return slow + 1


# nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
nums = [1,1,1,2,2,3]
print(Solution().removeDuplicates(nums))


