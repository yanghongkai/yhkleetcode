

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solutions:
    def addTwoNumbers(self, l1, l2):
        """

        :param l1: listNode
        :param l2: listNode
        :return: listNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.next

        if carry ==1:
            current.next = ListNode(1)

        return dummy.next









