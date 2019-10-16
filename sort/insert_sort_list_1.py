
# 147 对链表进行插入排序 https://leetcode-cn.com/problems/insertion-sort-list/

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
    def insertionSortList(self, head):
        p = head

        while hasattr(p, "next") and p.next:
            # p前一个node
            cur = p.next
            # 当前节点的值大于等于前一个节点的值不需要做插入操作
            if cur.val >= p.val:
                p = p.next
            else:
                # 先将后边节点接上
                p.next = cur.next
                # cur.value <= head.value 直接插在首部
                if cur.val <= head.val:
                    cur.next = head
                    head = cur
                else:
                    q = head
                    while q.next:
                        if q.next.val >= cur.val:
                            cur.next = q.next
                            q.next = cur
                            break
                        q = q.next
                # 插入的时候，p.next本身就自动指向了下一个节点，不需要再操作
                # p = p.next
        # print("head:", head)
        return head


nums = [4, 2, 1, 3]
root =  List(nums)
print(root)

s = Solution()
s.insertionSortList(root.head)
print("root:", root)
# 4->2->1->3









