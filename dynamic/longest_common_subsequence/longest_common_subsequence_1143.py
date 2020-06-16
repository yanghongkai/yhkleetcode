
# 最长公共子序列  https://leetcode-cn.com/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """

        """
        # dp 多一行一列，不用考虑边界条件
        dp = [[0 for j in range(len(text2)+1)]for i in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text1)][len(text2)]


text1 = "abcde"
text2 = "ace"
s = Solution()
print(s.longestCommonSubsequence(text1, text2))










