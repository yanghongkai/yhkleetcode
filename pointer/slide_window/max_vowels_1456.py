
# 1456 定长子串中元音的最大数目  https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

import collections


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        arr = ["a", "e", "i", "o", "u"]
        left = 0
        right = 0
        res = 0
        window = collections.defaultdict(int)

        while right < len(s):
            c = s[right]
            right += 1
            if c in arr:
                window[c] += 1

            # print("window: [{},{})".format(left, right))

            while right - left > k:
                d = s[left]
                left += 1
                if d in arr:
                    window[d] -= 1

            count = sum([v for k, v in window.items()])
            res = max(res, count)

        return res


s = "leetcode"
k = 3
print(Solution().maxVowels(s, k))




