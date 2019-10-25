# 385 迷你语法分析器 https://leetcode-cn.com/problems/mini-parser/


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.val = ""
        # nested_list 中并不一定只有一个元素(有n个同级元素)，每个都是 NestedInteger instance
        self.nested_list = []
        if value:
            self.val = value

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        if self.val and not self.nested_list:
            return True
        else:
            return False

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if isinstance(elem, NestedInteger):
            self.nested_list.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.val = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger():
            return self.val
        else:
            return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if not self.isInteger():
            return self.nested_list
        else:
            return None

import string

class Solution:
    def deserialize(self, s):
        """

        :param s:
        :return:
        """
        print("s:", s)
        i = 0
        atom = ""
        op_stack = []
        level_stack = []
        while i < len(s):
            # 先得到第一层的嵌套结构
            c = s[i]
            if c == "[":
                op_stack.append(i)
            elif c == "]":
                if op_stack:
                    start = op_stack.pop()
                    level_stack.append([start, i])
            i += 1
        print("level_stack:", level_stack)
        if level_stack:
            level_stack = self.merge_section(level_stack)
            print("after merge:", level_stack)
            # 元素
            start, end = level_stack[0][0], level_stack[0][-1]
            atom_str = ""
            if start == 0:
                atom_str = s[end+1:]
            elif end == len(s) -1:
                atom_str = s[:start]
            j = 0
            print("atom_str:", atom_str)
            while j< len(atom_str):
                if atom_str[j] in string.digits:
                    atom += atom_str[j]
                j += 1
            print("atom:", atom)
            if atom:
                elem = NestedInteger(atom)
            else:
                elem = NestedInteger()
            if len(s[start+1:end]) > 0:
                # 嵌套列表
                elem.add(self.deserialize(s[start+1:end]))
            return elem
        else:
            return NestedInteger(s)

    def merge_section(self, stack):
        """

        :param stack:
        :return:
        """
        list.sort(stack, key=lambda x: x[0])
        i = 0
        res = []
        while i <= len(stack)-1:
            if i+1 <= len(stack)-1 and stack[i+1][0] <= stack[i][-1] and stack[i+1][-1] <= stack[i][-1]:
                tmp = stack[i]
                # 合并
                # 第一次合并就应该+2
                i += 2
                while i <= len(stack)-1 and stack[i][0] <= tmp[-1] and stack[i][-1] <= tmp[-1]:
                    i += 1
                res.append(tmp)
            else:
                res.append(stack[i])
                i += 1
        return res


s = "324"
# s = "324,[1,[2],3]"
# s = "[123,[456,[789]]]"
# s = "[123,456,[788,799,833],[[]],10,[]]"
# s = "[[]]"
s = "[123,456,[788,799,833],[[]],10,[]]"
# s = "[]"
S = Solution()
print(S.deserialize(s))