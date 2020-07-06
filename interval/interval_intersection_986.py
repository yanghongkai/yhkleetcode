# 986 区间列表的交集  https://leetcode-cn.com/problems/interval-list-intersections/

from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(A) and j < len(B):
            a1, a2 = A[i][0], A[i][1]
            b1, b2 = B[j][0], B[j][1]
            # 有交集
            if b2 >= a1 and a2 >= b1:
                c1 = max(a1, b1)
                c2 = min(a2, b2)
                res.append([c1, c2])

            # 指针前进
            if b2 < a2:
                j += 1
            else:
                i += 1

        return res


A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(Solution().intervalIntersection(A, B))


