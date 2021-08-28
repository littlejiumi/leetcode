# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: head = head.next #正好是头节点
        cur = head.next
        pre = head
        while cur != None and cur.val != val:
            pre = cur
            cur = cur.next
        if cur: pre.next = cur.next # 没有这个节点时，cur==None
        return head
