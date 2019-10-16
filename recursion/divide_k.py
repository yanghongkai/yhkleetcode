# 给定一个整数组 nums 和一个正整数k， 找出是否有可能把这个数组分成k个非空子集，其总和相等

# 分割等和子集
# 698 https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/submissions/


class Solution:
    def backtracking(self, nums, k, target, start, cur, used, ans):
        """
        使用回溯法对所有可能的情况进行遍历,但不满足条件时可以马上进行剪枝
        基线条件:
        if k == 0:
            return True
        if cur == target:
            backtracking(nums, k-1, target, start=0, cur=0, used)
        :param nums:
        :param k:
        :param target: 需要凑的和
        :param start: 起始位置索引
        :param cur: 当前的值
        :param used: 搜索路径中已经使用的值
        :return:
        """
        if k == 0:
            return True
        if cur == target:
            return self.backtracking(nums, k - 1, target, 0, 0, used, ans)
        # 需要对所有可能的路径都进行遍历，但有一条路径可以完全走完时即返回
        for i in range(start, len(nums)):
            if (not used[i]) and (cur + nums[i] <= target):
                used[i] = True
                ans[len(ans) - k].append(nums[i])
                if self.backtracking(nums, k, target, i + 1, cur + nums[i], used, ans):
                    return True
                ans[len(ans) - k].remove(nums[i])
                used[i] = False
        return False

    def canPartitionKSubsets(self, nums, k) -> bool:
        """
        剪枝条件:
        1. 不能被整除一定不能被分割
        2. 最大值大于target一定不能满足条件
        :param nums:
        :param k:
        :return:
        """
        # 不能被整除一定不能被分割
        if sum(nums) % k != 0:
            return False
        target = sum(nums) / k
        # 最大值大于target一定不能满足条件
        if max(nums) > target:
            return False
        # 用于记录哪些元素被访问过了
        used = [False] * len(nums)
        # ans用来存储分割后的结果
        self.ans = [[] for i in range(k)]
        return self.backtracking(nums, k, target, 0, 0, used, self.ans)


nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
# nums = [10,10,10,7,7,7,7,7,7,6,6,6]
# k = 3
s = Solution()
print(s.canPartitionKSubsets(nums, k))
print(s.ans)
