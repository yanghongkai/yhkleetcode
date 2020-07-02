# 344 反转字符串  https://leetcode-cn.com/problems/reverse-string/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left right
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s


s = ["h", "e", "l", "l", "o"]
print(Solution().reverseString(s))

