
# 287 寻找重复数  https://leetcode-cn.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 使用二分查找
        left = 1
        right = len(nums) - 1

        # 终止条件 left = right, [left, right]相等也就是重复的那个数
        while left < right:
            mid = int((left + right) / 2)
            cnt = 0
            for item in nums:
                if item <= mid:
                    cnt += 1

            if cnt > mid:
                right = mid
            elif cnt == mid:
                left = mid + 1
            elif cnt < mid:
                left = mid + 1

        return left


nums = [1, 3, 4, 2, 2]
print(Solution().findDuplicate(nums))





