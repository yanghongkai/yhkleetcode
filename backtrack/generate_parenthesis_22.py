
# 22. 括号生成  https://leetcode-cn.com/problems/generate-parentheses/

from typing import List
import copy


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 在2n 个位置上进行遍历

        res = []
        track = []

        def backtrack(left, right, track):
            # left 剩余的数量
            # right 剩余的数量
            # track 路径
            # "(", ")"选择列表

            # 剪枝

            if left <0 or right < 0:
                return

            # 左括号 < 右括号, 不合法
            if left > right:
                return

            # 终止条件
            if left == 0 and right == 0:
                res.append("".join(copy.copy(track)))
                return

            # 选择 "("
            track.append("(")
            backtrack(left-1, right, track)
            track.pop()

            # 选择 ")"
            track.append(")")
            backtrack(left, right-1, track)
            track.pop()

        backtrack(n, n, track)
        return res


print(Solution().generateParenthesis(3))







