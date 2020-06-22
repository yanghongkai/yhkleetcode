# 5 最长回文子串   https://leetcode-cn.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 从中间开始向两边扩散来判断回文串
        res = ""
        for i in range(len(s)):
            sl = self._palindrome(s, i, i)
            sr = self._palindrome(s, i, i+1)
            if len(sl) > len(res):
                res = sl
            if len(sr) > len(res):
                res = sr

        return res

    def _palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]


s = "babad"
print(Solution().longestPalindrome(s))
