
# 19 删除链表的倒数第N个节点  https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head

        while n > 0:
            fast = fast.next
            n -= 1

        if fast == None:
            head = head.next
            return head

        while fast != None:
            fast = fast.next
            slow_prev = slow
            slow = slow.next

        # print(slow_prev.val)
        # print(slow.val)
        # slow.next = slow.next.next
        slow_prev.next = slow.next

        return head


head = ListNode(0)
# node2 = ListNode(1)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node5 = ListNode(5)
# head.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
print(Solution().removeNthFromEnd(head, 1))







