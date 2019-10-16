
# 第k个语法符号
# 799 https://leetcode-cn.com/problems/k-th-symbol-in-grammar/


class Solution:
    def kthGrammar(self, N:int, K:int) -> int:
        """
        1. 先计算出第N行的序列，然后再计算第K个
        :param N:
        :param k:
        :return:
        """
        res = self.grammar(N)
        # print(res)
        return res[K-1]

    def grammar(self, N):
        """
        base case:
        if N == 1:
            return [0]
        :param N:
        :return:
        """
        if N == 1:
            return [0]
        else:
            return self.convert(self.grammar(N-1))

    def convert(self, nums):
        """
        将0->01 1->10
        :param nums:
        :return:
        """
        res = []
        for item in nums:
            if item == 0:
                res.extend([0, 1])
            else:
                res.extend([1, 0])
        return res


s = Solution()
s.kthGrammar(1, 0)
s.kthGrammar(2, 0)
s.kthGrammar(3, 0)
s.kthGrammar(4, 0)


### method2
import math

class Solution1:
    def kthGrammar(self, N:int, K:int) -> int:
        """
        base case:

        recursive case:

        :param N:
        :param K:
        :return:
        """
        if N == 1:
            return 0
        else:
            return self.encode(self.kthGrammar(N-1, math.ceil(K/2)), K)

    def encode(self, num, K):
        """

        :param num:
        :return:
        """
        res = []
        if num == 0:
            res = [0, 1]
        else:
            res = [1, 0]
        if K % 2 == 0:
            return res[-1]
        else:
            return res[0]

s = Solution1()
print(s.kthGrammar(1, 1))
print(s.kthGrammar(4, 4))
print(s.kthGrammar(4, 5))



