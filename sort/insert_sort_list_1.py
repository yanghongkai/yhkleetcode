
# 148 排序链表 https://leetcode-cn.com/problems/sort-list/
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def add(self, node):
        self.next = node

    def __repr__(self):
        p = self
        res = []
        while p:
            res.append(str(p.val))
            p = p.next
        return "->".join(res)

    __str__ = __repr__

class List():
    def __init__(self, nums):
        self.head = ListNode(nums[0])
        p = self.head
        for i in range(1, len(nums)):
            node = ListNode(nums[i])
            p.next = node
            p = p.next

    def __repr__(self):
        res = []
        p = self.head
        while p:
            res.append(str(p.val))
            p = p.next
        return "->".join(res)

    __str__ = __repr__


class Solution:
    def sortList(self, head):
        """
        使用快慢指针进行分割
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        # head->slow, mid->fast 分割成2个子链表
        left, right = self.sortList(head), self.sortList(mid)
        # 合并
        h = p = ListNode(0)
        while left and right:
            if left.val <= right.val:
                p.next = left
                p = p.next
                left = left.next
            else:
                p.next = right
                p = p.next
                right = right.next
        if left:
            p.next = left
        if right:
            p.next = right
        return h.next




nums = [4, 2, 1, 3]
root = List(nums)
print(root)

s = Solution()
node = s.sortList(root.head)
print(node)









