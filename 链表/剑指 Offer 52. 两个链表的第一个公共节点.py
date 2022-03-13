# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s = set()
        while headA:
            s.add(headA)
            headA = headA.next
        while headB:
            if headB in s:
                return headB
            headB = headB.next
        return None
    
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        两个链表遍历完自己的再遍历另一个到相交节点时，走过的节点数目相同

        那么，只要其中一个链表走完了，就去走另一条链表的路。如果有交点，他们最终一定会在同一个
        位置相遇
        """
        cur_a, cur_b = headA, headB     # 用两个指针代替a和b

        
        while cur_a != cur_b:
            cur_a = cur_a.next if cur_a else headB      # 如果a走完了，那么就切换到b走
            cur_b = cur_b.next if cur_b else headA      # 同理，b走完了就切换到a
        
        return cur_a
