# 385 迷你语法分析器 https://leetcode-cn.com/problems/mini-parser/


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        # nested_list 中并不一定只有一个元素(有n个同级元素)，每个都是 NestedInteger instance
        if value:
            self.val = value
        else:
            self.val = []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        if not isinstance(self.val, list):
            return True
        else:
            return False

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if isinstance(elem, NestedInteger):
            self.val.append(elem)

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
            return self.val
        else:
            return None

import string

class Solution:
    def deserialize(self, s):
        """

        :param s:
        :return:
        """
        i = 0
        st = 0
        stack = []
        while i < len(s):
            c = s[i]
            print("i:", i)
            print("c:", c)
            if c == "[":
                stack.append(NestedInteger())
                st = i + 1
            elif c == "," or c == "]":
                if i > st:
                    print("st:", st)
                    print("str:", s[st:i])
                    num = int(s[st:i])
                    stack[-1].add(NestedInteger(num))
                if c == "]":
                    item = stack.pop()
                    if stack:
                        stack[-1].add(item)
                    else:
                        stack.append(item)
                st = i + 1
            elif c in string.digits and i == len(s)-1:
                if i >= st:
                    print("st:", st)
                    print("str:", s[st:i+1])
                    num = int(s[st:i+1])
                    if stack:
                        stack[-1].add(NestedInteger(num))
                    else:
                        stack.append(NestedInteger(num))

            i += 1
        return stack[-1]



s = "324"
# s = "324,[1,[2],3]"
# s = "[123,[456,[789]]]"
# s = "[123,456,[788,799,833],[[]],10,[]]"
# s = "[[]]"
# s = "[123,456,[788,799,833],[[]],10,[]]"
# s = "[]"
s = "1"
S = Solution()
print(S.deserialize(s))