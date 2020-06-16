
# 877 石子游戏  https://leetcode-cn.com/problems/stone-game/

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # (dp[i][j].first, dp[i][j].sec) 从i到j first, 先手的得分, sec后手的得分
        dp = [[[0, 0] for j in range(len(piles))] for i in range(len(piles))]
        # print(dp)
        for i in range(len(piles)):
            dp[i][i][0] = piles[i]
            dp[i][i][1] = 0

        for i in range(len(piles)):
            for j in range(i+1, len(piles)):
                left = piles[i] + dp[i+1][j][1]
                right = piles[j] + dp[i][j-1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i+1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j-1][0]

        minus = dp[len(piles)-1][len(piles)-1][0] - dp[len(piles)-1][len(piles)-1][1]
        if minus > 0:
            return True
        else:
            return False


piles = [5, 3, 4, 5]
s = Solution()
print(s.stoneGame(piles))



