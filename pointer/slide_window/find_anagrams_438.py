
# 438 找到字符串中所有字母异位词

from typing import List
import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口
        window = collections.defaultdict(int)
        need = collections.defaultdict(int)
        for c in p:
            need[c] += 1

        left = 0
        right = 0
        valid = 0
        length = float("inf")
        res = []

        while right < len(s):
            c = s[right]
            right += 1
            # 进行窗口内的更新操作
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # print("window: [{},{})".format(left, right))

            while valid == len(need):
                if right - left <= length:
                    start = left
                    length = right - start
                    if length == len(p):
                        res.append(start)
                    # print("start:", start)

                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        return res


s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))

