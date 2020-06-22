# 51 N皇后 https://leetcode-cn.com/problems/n-queens/

from typing import List
import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for j in range(n)] for i in range(n)]

        def is_valid(board, row, col):
            # 该值还未放进去
            # 列
            for i in range(len(board)):
                if board[i][col] == "Q":
                    return False
            # 左上
            # i = row-1 j = col-1
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                else:
                    i -= 1
                    j -= 1

            # 右上
            i = row - 1
            j = col + 1
            while i >= 0 and j < len(board[0]):
                if board[i][j] == "Q":
                    return False
                else:
                    i -= 1
                    j += 1

            return True

        def backtrack(board, row):
            # 结束条件 row == board的最后一行
            if row == len(board):
                tmp_board = copy.deepcopy(board)
                res_board = ["".join(tmp_board[i]) for i in range(len(tmp_board))]
                res.append(res_board)
                # print("res_board:", res_board)
                return

            n_col = len(board[row])
            # print("row:", row)
            # print("n_col:", n_col)
            # 选择 第row行的所有列
            for i_col in range(n_col):
                # 候选列表
                if not is_valid(board, row, i_col):
                    continue
                # 做选择
                board[row][i_col] = "Q"
                # 递归调用
                backtrack(board, row + 1)
                # 撤销选择
                board[row][i_col] = "."

        backtrack(board, 0)
        return res


print(Solution().solveNQueens(4))
