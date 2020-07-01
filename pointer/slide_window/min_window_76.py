
# 76 最小覆盖子串  https://leetcode-cn.com/problems/minimum-window-substring/
import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 初始化 window 和 need ，记录窗口中的字符和需要凑齐的字符
        window = collections.defaultdict(int)
        need = collections.defaultdict(int)
        for c in t:
            need[c] += 1

        # print("need:", need)

        # 使用 left, right 初始化窗口的两端，区间[left, right) 是左闭右开，所以初始情况下窗口没有包含任何元素
        left = 0
        right = 0
        # valid 表示窗口中满足 need 条件的字符个数，如果 valid == need.size，说明窗口已满足条件，已经完全覆盖了串 T
        valid = 0

        # 记录最小覆盖子串的起始索引及长度
        start = 0
        length = float("inf")

        while right < len(s):
            # c 是将移入窗口的字符
            c = s[right]
            # 右移窗口
            right += 1
            # 进行窗口内数据的一系列更新
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # print("window: [{}, {})".format(left, right))

            # 判断左侧窗口是否要收缩
            while valid == len(need):
                # 在这里更新最小覆盖子串
                if right - left < length:
                    start = left
                    length = right - left

                # print("[{}:{}]".format(start, start+length))

                # d 是将移出窗口的字符
                d = s[left]
                # 左移窗口
                left += 1
                # 进行窗口内数据的一系列更新
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1

        # 返回最小覆盖子串
        if length == float("inf"):
            return ""
        else:
            return s[start: start+length]


s = "EBBANCF"
t = "ABC"
print(Solution().minWindow(s, t))



