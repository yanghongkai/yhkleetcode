
# 763 划分字母区间  https://leetcode-cn.com/problems/partition-labels/

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c:i for i, c in enumerate(S)}
        # print(last)
        left = 0
        right = 0
        ans = []

        for i, c in enumerate(S):
            right = max(right, last[c])
            if i == right:
                ans.append(i - left + 1)
                left = i + 1
            # print("{}, {}".format(c, right))

        return ans


S = "ababcbacadefegdehijhklij"
print(Solution().partitionLabels(S))





