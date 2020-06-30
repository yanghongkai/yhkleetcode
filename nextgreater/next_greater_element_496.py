
# 496 下一个更大元素 I https://leetcode-cn.com/problems/next-greater-element-i/
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 是 nums2的子集，寻找nums2中的下一个元素
        stack = []
        ans = [-1 for i in range(len(nums2))]
        # 倒序遍历
        for i in range(len(nums2)-1, -1, -1):
            # 将当前元素和比当前元素高的元素之间的矮个去掉
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()
            if len(stack) > 0:
                ans[i] = stack[-1]

            stack.append(nums2[i])

        return [ans[nums2.index(v)] for v in nums1]


nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(Solution().nextGreaterElement(nums1, nums2))





