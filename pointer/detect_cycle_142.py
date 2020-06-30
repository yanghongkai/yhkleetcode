
# 142 环形链表 II  https://leetcode-cn.com/problems/linked-list-cycle-ii/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or head.next == None:
            return None
        # 快慢指针，找到相遇的位置
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                break

        if fast != slow:
            return None

        # 相遇之后
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow


node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

print(Solution().detectCycle(node1))




