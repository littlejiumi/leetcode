# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre= None
        cur=head
        while cur != None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
