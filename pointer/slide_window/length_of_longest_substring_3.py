
# 3 无重复字符的最长子串

import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = collections.defaultdict(int)

        left = 0
        right = 0
        res = 0

        while right < len(s):
            c = s[right]
            # print("c:", c)
            right += 1
            window[c] += 1

            # print("window: [{},{})".format(left, right))

            # 判断窗口是否要进行收缩
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1

            # print("window: [{},{})".format(left, right))
            res = max(res, right-left)
        return res


s = "abcabcbb"
s = "pwwkew"
s = " "
s = "dvdf"
print(Solution().lengthOfLongestSubstring(s))


