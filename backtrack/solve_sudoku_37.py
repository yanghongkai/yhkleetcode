# 37 解数独  https://leetcode-cn.com/problems/sudoku-solver/

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 回溯法
        chs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

        def is_valid(board, r, c, n):
            # r: row, c: col, n: character
            for k in range(9):
                # 行
                if board[r][k] == n:
                    return False
                # 列
                if board[k][c] == n:
                    return False
                # 3*3
                # row = int((r / 3) * 3 + k / 3)
                # col = int(c / 3) * 3 + k % 3
                # print("{}-{}-{}, row:{}, col:{}".format(r, c, k, row, col))
                # print("row:{}, col:{}, {}".format(row, col, board[row][col]))
                if board[int(r / 3) * 3 + int(k / 3)][int(c / 3) * 3 + k % 3] == n:
                    return False

            return True

        def trackback(board, i, j):
            # i: row, j: col
            M = 9  # 行数
            N = 9  # 列数

            # 如果到最后一列换行
            if j == N:
                return trackback(board, i + 1, 0)

            if i == M:
                return True

            # 如果该位置是预设数字，不需要我们操心
            if board[i][j] != ".":
                return trackback(board, i, j + 1)

            # 遍历9个数字
            for n in chs:
                if not is_valid(board, i, j, n):
                    continue
                board[i][j] = n
                if trackback(board, i, j + 1):
                    return True
                board[i][j] = "."

            return False

        trackback(board, 0, 0)
        # print(board)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

Solution().solveSudoku(board)