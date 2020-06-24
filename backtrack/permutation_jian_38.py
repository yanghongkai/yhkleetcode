
# 剑指offer 38 字符串的排列  https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/

from typing import List
import copy


class Solution:
    def permutation(self, s: str) -> List[str]:
        # 回溯法遍历
        track = []  # 存储索引，避免有重复元素
        res = {}

        def backtrack(s, track):
            # s 和 track 共同决定 选择列表
            # 终止条件
            if len(track) == len(s):
                tmp_arr = [s[i] for i in copy.copy(track)]
                tmp_str = "".join(tmp_arr)
                res[tmp_str] = 1
                # if tmp_str not in res:
                #     res.append(tmp_str)
                return

            for idx, c in enumerate(s):
                if idx in track:
                    continue
                track.append(idx)
                backtrack(s, track)
                track.pop()

        backtrack(s, track)
        return list(res.keys())


print(Solution().permutation("abc"))


