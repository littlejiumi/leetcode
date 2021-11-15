# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = cur = ListNode()
        c = 0
        while l1 and l2:
            S = c + l1.val + l2.val
            cur.next = ListNode(S%10)
            c = S // 10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        while l1:
            S = c + l1.val
            cur.next = ListNode(S%10)
            c = S // 10
            l1 = l1.next
            cur = cur.next
        while l2:
            S = c + l2.val
            cur.next = ListNode(S%10)
            c = S // 10
            l2 = l2.next
            cur = cur.next
        if c:
            temp = ListNode(c)
            cur.next = temp
        return res.next
