# 1423 可获得的最大点数  https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # 滑动窗口
        # 逆向 求连续N 个窗口中的最小值
        if len(cardPoints) == k:
            return sum(cardPoints)
        left = 0
        right = 0
        # 窗口是固定大小的N
        N = len(cardPoints) - k
        total = sum(cardPoints)
        window = []
        res = total

        while right < len(cardPoints):
            c = cardPoints[right]
            right += 1
            window.append(c)

            while right - left > N:
                d = cardPoints[left]
                left += 1
                window.pop(0)

            if right - left == N:
                res = min(res, sum(window))

        return total - res

    def maxScore1(self, cardPoints: List[int], k: int) -> int:
        # 滑动窗口
        # 逆向 求连续N 个窗口中的最小值
        if len(cardPoints) == k:
            return sum(cardPoints)
        left = 0
        right = 0
        # 窗口是固定大小的N
        N = len(cardPoints) - k
        total = sum(cardPoints)
        window = []
        res = total
        cur_sum = 0

        while right < len(cardPoints):
            c = cardPoints[right]
            right += 1
            window.append(c)
            cur_sum += c

            # print("window: [{},{})".format(left, right))

            while right - left > N:
                d = cardPoints[left]
                left += 1
                window.pop(0)
                cur_sum -= d

            if right - left == N:
                res = min(res, cur_sum)

        return total - res


cardPoints = [1, 79, 80, 1, 1, 1, 200, 1]
k = 3
cardPoints = [11, 49, 100, 20, 86, 29, 72]
k = 4
print(Solution().maxScore(cardPoints, k))
