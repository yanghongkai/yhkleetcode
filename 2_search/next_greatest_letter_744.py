
# 744 寻找比目标字母达的最小字母  https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target/

from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # 类似最有边界 返回left， 考虑left的越界问题
        left = 0
        right = len(letters) - 1

        # 终止条件: left = right + 1
        while left <= right:
            mid = int((left + right) / 2)
            if ord(letters[mid]) == ord(target):
                left = mid + 1
            elif ord(letters[mid]) < ord(target):
                left = mid + 1
            elif ord(letters[mid]) > ord(target):
                right = mid - 1

        if left >= len(letters):
            return letters[0]
        if ord(letters[left]) > ord(target):
            return letters[left]
        else:
            return letters[0]


letters = ["c", "f", "j"]
target = "c"
print(Solution().nextGreatestLetter(letters, target))





