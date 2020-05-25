
# 72 编辑距离 https://leetcode-cn.com/problems/edit-distance/


class Solution:
    def minDistance(self, word1, word2) -> int:
        """
        a[i]!=b[j]:
            cell[i][j] = cell[i][j-1] + 1 插入 b[j]
            cell[i][j] = cell[i-1][j] +1 删除 a[i]
            cell[i][j] = cell[i-1][j-1] +1 a[i]->b[j]
        a[i] = b[j]:
            cell[i][j] = cell[i-1][j-1]
            if cell[i-1][j-1]不存在，从 cell[i][j-1] cell[i-1][j], cell[i-1][j-1]中找一个最小的
        :param word1:
        :param word2:
        :return:
        """
        if not len(word1) or not len(word2):
            return max(len(word1), len(word2))
        # 操作
        ops = [[""]*len(word2) for i in range(len(word1))]
        cell = [[0]*len(word2) for i in range(len(word1))]
        # 第一行
        for j in range(len(word2)):
            if j == 0:
                if word1[0] != word2[0]:
                    op_str = "<{}->{}>".format(word1[0], word2[j])
                    cell[0][0] = 1
            else:
                if word2[j] == word1[0]:

                    cell[0][j] = j + 1 - 1
                    op_str = "".join(["<+ {}>".format(word2[idx]) for idx in range(j)])
                else:
                    # add
                    cell[0][j] = j + 1
                    op_str = " <+ {}>".format(word2[j])
                    op_str = ops[0][j-1] + op_str
            ops[0][j] = op_str


        # 第一列
        for i in range(1, len(word1), 1):
            if word1[i] == word2[0]:
                cell[i][0] = i + 1 -1
                op_str = "".join(["<- {}> ".format(word1[idx]) for idx in range(i)])
            else:
                cell[i][0] = i + 1
                # delete
                op_str = " <- {}>".format(word1[i])
                op_str = ops[i-1][0] + op_str
            ops[i][0] = op_str

        for i in range(1, len(word1), 1):
            for j in range(1, len(word2), 1):
                add = cell[i][j-1]
                delete = cell[i-1][j]
                replace = cell[i-1][j-1]
                min_val = min([add, delete, replace])
                prev_op = ""
                if min_val == add:
                    op_str = "<+ {}>".format(word1[i])
                    prev_op = ops[i][j-1]
                if min_val == delete:
                    op_str = "<- {}".format(word1[i])
                    prev_op = ops[i-1][j]
                if min_val == replace:
                    op_str = "<{} -> {}>".format(word1[i], word2[j])
                    prev_op = ops[i-1][j-1]

                if word1[i] == word2[j]:
                    cell[i][j] = min_val
                    op_str = ""
                else:
                    cell[i][j] = min_val + 1
                ops[i][j] = prev_op + op_str

        print(ops)
        print(cell)
        return cell[len(word1)-1][len(word2)-1]






# word1 = "horse"
# word2 = "ros"
word1 = "intention"
word2 = "execution"
# word1 = "sea"
# word2 = "eat"
# word1 = "ab"
# word2 = "a"
s = Solution()
print(s.minDistance(word1, word2))



