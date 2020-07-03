# 524 通过删除字母匹配到字典里最长单词  https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/

from typing import List
import collections


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        # 求 s 和 d 中每个单词的最小覆盖子串

        # s 是否能覆盖s1, 不同点在于得保持顺序
        def is_cover(s, s1):
            # left -> s
            # right -> s1
            left = 0
            right = 0

            while right < len(s1) and left < len(s):
                if s[left] == s1[right]:
                    right += 1
                    left += 1
                else:
                    left += 1

            if right == len(s1):
                return len(s1)
            else:
                return -1

        word_len = [is_cover(s, w) for w in d]
        # print("word_len:", word_len)
        max_len = 0
        max_w = ""
        for idx, wl in enumerate(word_len):
            if wl > max_len:
                max_len = wl
                max_w = d[idx]
            elif wl == max_len:
                if len(d[idx]) > len(max_w):
                    max_w = d[idx]
                elif len(d[idx]) == len(max_w):
                    if d[idx] < max_w:
                        max_w = d[idx]
        # print("max_w:", max_w)
        return max_w


# s = "abpcplea"
# d = ["ale", "apple", "monkey", "plea"]

s = "aewfafwafjlwajflwajflwafj"
d = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]

s = "apple"
d = ["zxc","vbn"]
print(Solution().findLongestWord(s, d))


