
# 567 字符串的排列  https://leetcode-cn.com/problems/permutation-in-string/
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 滑动窗口
        window = collections.defaultdict(int)
        need = collections.defaultdict(int)
        for c in s1:
            need[c] += 1

        left = 0
        right = 0
        start = 0
        valid = 0
        length = float("inf")

        while right < len(s2):
            c = s2[right]
            right += 1
            # 进行窗口内的数据更新操作
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # print("window: [{}, {})".format(left, right))

            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left

                    # print("candidate: [{}, {})".format(start, start + length))
                    # print("s:{}".format(s2[start:start+length]))

                d = s2[left]
                left += 1
                # 进行窗口内的数据更新操作
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        # print("length:", length)

        if length == float("inf"):
            return False
        elif length == len(s1):
            return True
        else:
            return False


s1 = "ab"
s2 = "eibaooo"
s1 = "abcdxabcde"
s2 = "abcdeabcdx"
print(Solution().checkInclusion(s1, s2))


