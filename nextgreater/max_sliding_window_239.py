# 239 滑动窗口最大值  https://leetcode-cn.com/problems/sliding-window-maximum/

from typing import List


class Queue:
    def push(self, n):
        """ enqueue, 在队尾加入元素n"""
        pass

    def pop(self):
        """dequeue, 删出队头元素"""
        pass


class Deque:
    def push_front(self, n):
        """在队头插入元素 n"""
        pass

    def push_back(self, n):
        """在队尾插入元素 n"""
        pass

    def pop_front(self):
        """在队头删除元素"""
        pass

    def pop_back(self):
        """在队尾删除元素"""
        pass

    def front(self):
        """返回队头元素"""
        pass

    def back(self):
        """返回队尾元素"""
        pass


class MonotonicQueue:
    def push(self, n):
        """在队尾添加元素n"""
        pass

    def max(self):
        """返回当前队列中的最大值"""
        pass

    def pop(self, n):
        """队头元素如果是 n，删除它"""
        pass


class Solution:
    window = MonotonicQueue()
    res = []

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        for i in range(len(nums)):
            if i < k - 1:
                self.window.push(nums[i])
            else:
                # 滑动窗口向前滑动
                self.window.push(nums[i])
                self.res.append(self.window.max())
                # nums[i-k+1] 就是窗口最后的元素
                self.window.pop(nums[i-k+1])

                pass
        pass


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(Solution().maxSlidingWindow(nums, k))


