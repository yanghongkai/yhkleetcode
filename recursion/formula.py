
# 原子的数量

# 726 https://leetcode-cn.com/problems/number-of-atoms/

import string
from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        大写字母和括号都是一个新的原子的开始
        :param formula:
        :return:
        """
        # tmp 存储当前括号里的内容
        tmp = defaultdict(int)
        n = len(formula)
        atom = ""
        stack = []
        # 数字
        i = 0
        # H2O
        while i < n:
            s = formula[i]
            # print("i:", i)
            # print("s:", s)
            # print("tmp:", tmp)
            # 大写
            if s in string.ascii_uppercase:
                # 大写字母一定是一个新的元素的开始
                atom = s
                # MggH
                # Mg2
                # Mg(
                # Mg)
                while i+1 <= n-1 and formula[i+1] in string.ascii_lowercase:
                    atom += formula[i+1]
                    i += 1
                # 默认是1
                tmp[atom] += 1
                i += 1
            # 数字
            # B7
            elif s in string.digits:
                repeated = s
                while i+1 <= n-1 and formula[i+1] in string.digits:
                    repeated += formula[i+1]
                    i += 1
                # 非")2"这种情况，只当前atom翻倍
                tmp[atom] = tmp[atom] + int(repeated) - 1
                i += 1
            # 小写
            # (
            elif s == "(":
                stack.append(tmp)
                # 清空tmp
                tmp = defaultdict(int)
                atom = ""
                i += 1
            # )
            elif s == ")":
                repeated = ""
                while i+1 <= n-1 and formula[i+1] in string.digits:
                    repeated += formula[i+1]
                    i += 1
                # 计算括号里边的 Mg(O(SN)2)3
                if repeated:
                    for k in tmp:
                        tmp[k] *= int(repeated)
                # 再加上同一级的
                cur_level = stack.pop()
                for k in cur_level:
                    if k in tmp:
                        tmp[k] += cur_level[k]
                    else:
                        tmp[k] = cur_level[k]
                i += 1
        res = ""
        tmp = sorted(tmp.items(), key=lambda x: x[0])
        for k,v in tmp:
            res += k
            if v > 1:
                res += str(v)
        return res



s = Solution()
formula = "H2O"
# formula = "MgO12"
# formula = "Mg(OH)2"
# formula = "K4(ON(SO3)2)2"
# formula = "((N42)24(OB40Li30CHe3O48LiNN26)33(C12Li48N30H13HBe31)21(BHN30Li26BCBe47N40)15(H5)16)14"
# formula = "((N2)3(SO)3)2"
formula = "H11He49NO35B7N46Li20"
# formula = "HO"
# formula = "B7"
print(s.countOfAtoms(formula))




