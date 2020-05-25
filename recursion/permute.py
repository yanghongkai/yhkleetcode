
# 46 全排列 https://leetcode-cn.com/problems/permutations/


class Solution:
    def permute(self, nums):
        """

        :param nums:
        :return:
        """
        if len(nums) == 1:
            return [nums]
        if len(nums) == 0:
            return [[]]
        return self.insert(self.permute(nums[:len(nums)-1]), nums[-1])

    def insert(self, nums, item):
        """
        在nums组合中插入一个元素
        :param nums:
        :param item:
        :return:
        """
        res = []
        for num in nums:
            for j in range(len(nums)+1):
                tmp = num[:]
                tmp.insert(j, item)
                if tmp not in res:
                    res.append(tmp)
        return res





nums = [1, 2, 3, 4]
# nums = [5, 4, 6, 2]
s = Solution()
print(s.permute(nums))
print(len(s.permute(nums)))
# print(s.insert([[1, 2], [2, 1]], 3))






