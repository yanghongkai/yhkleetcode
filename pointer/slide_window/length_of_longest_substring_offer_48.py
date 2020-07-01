
# 剑指offer 48 最长不含重复字符的子字符串  https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/

import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)

        left = 0
        right = 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1

            # print("window: [{},{})".format(left, right))

            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1

            # print("[{}, {})".format(left, right))
            res = max(res, right-left)

        return res


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))



