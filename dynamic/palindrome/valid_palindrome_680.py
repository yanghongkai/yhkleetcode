
# 680 验证回文字符串 II https://leetcode-cn.com/problems/valid-palindrome-ii/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 最多删除一个字符，能否成为回文字符串 等效于 字符串中最长回文子序列的长度>=n-1
        # dp[i][j]  在子串s[i..j]中，最长回文子序列的长度为 dp[i][j]
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        # 反向遍历
        for i in range(n-1, -1, -1):
            for j in range(i+1, n, 1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        if dp[0][n-1] >= n-1:
            return True
        return False


class Solution2:
    def validPalindrome(self, s: str) -> bool:
        # 使用左右双指针
        def checkPalinrome(low, high):
            while low < high:
                if s[low] == s[high]:
                    low += 1
                    high -= 1
                else:
                    return False
            return True

        low = 0
        high = len(s)-1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalinrome(low+1, high) or checkPalinrome(low, high-1)
        return True

s = "abca"
print(Solution2().validPalindrome(s))







