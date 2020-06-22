
# 516 最长回文子序列  https://leetcode-cn.com/problems/longest-palindromic-subsequence/


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] = dp[i+1][j-1] + 2 a = b
        # dp[i][j] = max(dp[i][j-1], dp[i+1][j] a!=b
        # 反着遍历
        dp = [[0 for j in range(len(s))] for i in range(len(s))]
        # base case dp[i][i] = 1
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s), 1):
                # print("i:{}, j:{}".format(i, j))
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

        return dp[0][len(s)-1]


s = "bbbab"
print(Solution().longestPalindromeSubseq(s))






