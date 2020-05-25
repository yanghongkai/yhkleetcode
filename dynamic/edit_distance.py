
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
        ops = []
        cell = [[0]*len(word2) for i in range(len(word1))]
        if word1[0]!=word2[0]:
            cell[0][0] = 1
            ops.append("replace: {}->{}".format(word1[0], word2[0]))
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] != word2[j]:
                    if i==0 and j==0:
                        continue
                    tmp_dict = {}
                    # 比较插入，删除，替换操作
                    insert = cell[i][j-1] if j>=1 else 100
                    delete = cell[i-1][j] if i>=1 else 100
                    replace = cell[i-1][j-1] if i>=1 and j>=1 else 100
                    tmp_dict["insert"] = insert
                    tmp_dict["delete"] = delete
                    tmp_dict["replace"] = replace
                    # sorted_select = sorted(tmp_dict.items(), key=lambda x: x[1])
                    # print(sorted_select)
                    # exit()
                    select, num = sorted(tmp_dict.items(), key=lambda x: x[1])[0]
                    # print("num:", num)
                    if select == "insert":
                        ops.append("insert: {}".format(word2[j]))
                    elif select == "delete":
                        ops.append("delete: {}".format(word1[i]))
                    else:
                        ops.append("replace: {}->{}".format(word1[i], word2[j]))
                    cell[i][j] = num + 1
                else:
                    ops.append("no op")
                    # print("i:{}, j:{}".format(i, j))
                    # print("i:{}, j:{}".format(i, j))
                    # print(cell[i-1][j-1])
                    if i>=1 and j>=1:
                        cell[i][j] = cell[i-1][j-1]
                    elif i <= 1 and j>=1:
                        cell[i][j] = cell[i][j-1]
                    elif j <=1 and i>=1:
                        cell[i][j] = cell[i-1][j]
        # print(ops)
        print(cell)
        return cell[len(word1)-1][len(word2)-1]


word1 = "horse"
word2 = "ros"
# word1 = "sea"
# word2 = "eat"
# word1 = "ab"
# word2 = "a"
s = Solution()
print(s.minDistance(word1, word2))



