# 面试题 17.11 单词距离  https://leetcode-cn.com/problems/find-closest-lcci/

from typing import List
import collections


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        # 滑动窗口 left right
        window = collections.defaultdict(int)
        need = collections.defaultdict(int)
        need[word1] = 1
        need[word2] = 1

        left = 0
        right = 0
        valid = 0
        length = float("inf")
        while right < len(words):
            c = words[right]
            right += 1
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # print("window: [{},{})".format(left, right))

            while valid == 2:
                if right - left < length:
                    start = left
                    length = right - left

                d = words[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        if length != float("inf"):
            return length - 1


words = ["I", "am", "a", "student", "from", "a", "university", "in", "a", "city"]
word1 = "a"
word2 = "student"
print(Solution().findClosest(words, word1, word2))

