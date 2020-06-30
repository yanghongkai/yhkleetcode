
# 503 下一个更大元素 II  https://leetcode-cn.com/problems/next-greater-element-ii/

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # 环形 用循环数组解决
        n = len(nums)
        ans = [-1 for i in range(n)]
        stack = []
        for i in range(2*n-1, -1, -1):
            while len(stack) > 0 and stack[-1] <= nums[i%n]:
                stack.pop()
            if len(stack) > 0:
                ans[i%n] = stack[-1]

            stack.append(nums[i%n])

        return ans


nums = [1, 2, 1]
print(Solution().nextGreaterElements(nums))






