# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: # 递归
    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []
        return self.reversePrint(head.next) + [head.val]

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        ans = []
        while head is not None:
            stack.append(head.val)
            head = head.next
        ans= stack[::-1]
        return ans
