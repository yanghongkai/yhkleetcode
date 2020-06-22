
# 5 最长回文子串 https://leetcode-cn.com/problems/longest-palindromic-substring/

# 回文串是一个正读和反读都一样的字符串，"level", "noon"


class Solution:
    def longestPalindrome(self, s):
        """
        babad 和 dabab (正序和倒序的字符串) 形成网格，网格中的值为最长公共子串长度
        正序为行，返回值， a[i-n:i+1]
        if a[i] = b[j]:
            cell[i][j] = cell[i-1][j-1] +1
        else:
            cell[i][j]= 0
        aacdefcaa
        需要进一步判断子串的索引和逆序子串中的原始索引是否是同一个
        :param s:
        :return:
        """
        if not s:
            return ""
        a = s
        # 逆序
        b = s[::-1]
        cell = [[0]*len(s) for i in range(len(s))]

        for i in range(len(a)):
            for j in range(len(b)):
                if a[i] == b[j]:
                    if i>=1 and j>=1:
                        cell[i][j] = cell[i-1][j-1] + 1
                    else:
                        cell[i][j] = 1
                else:
                    cell[i][j] = 0
        max_value = 0
        idx_arr = [0, 0]
        for i in range(len(cell)):
            for j in range(len(cell[i])):
                if cell[i][j] > max_value:
                    n = cell[i][j]
                    sub_str_s = i - n +1
                    re_sub_str_s = len(s) - j -1
                    # 子串的原始索引和逆序子串中的原始索引是同一个，才是回文子串
                    if sub_str_s == re_sub_str_s:
                        idx_arr = [i, j]
                        max_value = cell[i][j]
        n = cell[idx_arr[0]][idx_arr[-1]]
        res = a[idx_arr[0]-n+1: idx_arr[0]+1]
        return res


s = "babad"
# s = "cbbd"
# s = "aacdefcaa"
sl = Solution()
print(sl.longestPalindrome(s))










