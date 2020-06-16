

# 暴力解法

def search(txt, pattern):
    M = len(pattern)
    N = len(txt)
    for i in range(N-M + 1):
        j = 0
        while j < M:
            if txt[i+j] != pattern[j]:
                break
            else:
                j += 1
        if j == M:
            return i

    return -1


txt = "aaacaaab"
pattern = "aaab"
print(search(txt, pattern))

# char(65) = "A"
# ord("A") = 65


class KMP(object):
    def __init__(self, pattern):
        self.M = len(pattern)
        self.dp = self._kmp(pattern)

    def _kmp(self, pattern):
        # 通过 pattern 构建 dp 数组， 需要 O(M)时间
        # 定义初始状态
        dp = [[0 for j in range(256)] for i in range(len(pattern))]
        # base
        dp[0][ord(pattern[0])] = 1
        # 影子状态
        X = 0
        for i in range(1, len(pattern)):
            for c in range(256):
                if chr(c) == pattern[i]:
                    dp[i][c] = i + 1
                else:
                    dp[i][c] = dp[X][c]
            X = dp[X][ord(pattern[i])]
        return dp

    def search(self, txt):
        # 借助 dp 数组 去匹配txt， 只需要 O(N)时间
        # 当前所处状态
        j = 0
        for i in range(len(txt)):
            j = self.dp[j][ord(txt[i])]  # 下一个状态

            if j == self.M:  # 如果是终止状态，即找到匹配字符串
                return i - self.M + 1

        return -1


kmp = KMP("aaab")
print(kmp.search("aaacaaab"))



