# 40 组合总和II https://leetcode-cn.com/problems/combination-sum-ii/

from typing import List
import copy


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 回溯遍历
        track = set()  # track 中存储索引，不同位置的相同数字可以使用
        res = []

        def backtrack(candidates, start, track):
            # track 路径
            # candidates, start 决定选择列表
            # 每个数字在组合中只能使用一次
            # 终止条件
            # 1) 遍历完  2) 满足条件
            if sum([candidates[i] for i in track]) == target:
                if track not in res:
                    res.append(copy.copy(track))
                # res.append([candidates[i] for i in copy.copy(track)])
                return
            if start == len(candidates):
                return

            for i in range(start, len(candidates), 1):
                if i in track:
                    continue
                track.add(i)
                backtrack(candidates, i + 1, track)
                track.remove(i)

        backtrack(candidates, 0, track)
        return res


# 重点方法 同层去重
class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 回溯遍历
        # 重点 同层去重
        # 每一层针对排序后的数组，如果以当前节点为头节点的所有组合都照完了，那么下一个与他相同的头结点就不用去找了
        list.sort(candidates)
        print(candidates)
        track = []  # track 中存储索引，不同位置的相同数字可以使用
        res = []

        def backtrack(candidates, start, track):
            # track 路径
            # candidates, start 决定选择列表
            # 每个数字在组合中只能使用一次
            # 终止条件
            # 1) 遍历完  2) 满足条件
            if sum(track) == target:
                res.append(copy.copy(track))
                return
            if sum(track) > target:
                return

            for i in range(start, len(candidates), 1):
                # 同层去重
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                track.append(candidates[i])
                backtrack(candidates, i + 1, track)
                track.pop()

        backtrack(candidates, 0, track)
        return res


candidates = [2, 5, 2, 1, 2]
target = 5

candidates = [3, 1, 3, 5, 1, 1]
target = 8
# print(Solution().combinationSum2(candidates, target))
print(Solution2().combinationSum2(candidates, target))
