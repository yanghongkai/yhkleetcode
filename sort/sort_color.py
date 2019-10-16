
# 75 颜色分类 https://leetcode-cn.com/problems/sort-colors/submissions/


class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        三个指针
        p0: 0的最右边界
        p2: 2的最左边界
        cur: 当前元素

        """
        p0 = 0
        cur = 0
        p2 = len(nums) - 1

        while cur <= p2:
            # cur 指向元素2，交换元素
            if nums[cur] == 2:
                nums[p2], nums[cur] = nums[cur], nums[p2]
                p2 -= 1
            elif nums[cur] == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                cur += 1
                p0 += 1
            else:
                cur += 1



nums = [2, 0, 2, 1, 1, 0]
# nums = [2, 0, 1]
nums = [1, 2, 1]
# nums = [1, 0, 1]
# output [0,0,1,1,2,2]
s = Solution()
s.sortColors(nums)
print(nums)






