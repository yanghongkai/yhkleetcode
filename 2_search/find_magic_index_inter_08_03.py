
# 面试题08.03 魔术索引  https://leetcode-cn.com/problems/magic-index-lcci/

from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        # 考虑数值可能重复
        # mid == nums[mid] 说明mid的位置符合要求，继续查看是否有更下的并且符合要求的索引 [0, mid-1]
        # mid != nums[mid], 需要对mid的两边继续二分查找

        res = [-1]

        def binary_search(nums, left, right, res):
            if res[0] != -1 and res[0] < left:
                return
            if left <= right:
                mid = int((left + right) / 2)
                if nums[mid] == mid:
                    if res[0] == -1:
                        res[0] = mid
                    else:
                        if mid < res[0]:
                            res[0] = mid

                    binary_search(nums, left, mid-1, res)

                elif nums[mid] != mid:
                    binary_search(nums, left, mid-1, res)
                    binary_search(nums, mid+1, right, res)


        binary_search(nums, 0, len(nums)-1, res)
        # print(res)
        return res[0]


nums = [0, 2, 3, 4, 5]
print(Solution().findMagicIndex(nums))





