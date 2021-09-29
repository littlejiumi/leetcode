# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pse = ListNode(0, head)  # 设定一个虚拟节点，指向head
        l, r = pse, pse # l,r首先指向pse节点，这样可以不用单独处理删除的是头节点的情况
        while n+1: # 想要得到欲删除节点的上一个节点，n多走1
            r = r.next
            n -= 1
        while r != None:
            l = l.next
            r = r.next
        l.next = l.next.next
        return pse.next  # 记得最后返回pse.next，即头节点





/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode pre = new ListNode(0, head);
        ListNode pse = pre;
        ListNode l = head, r = head;
        while(n--!=0){
            r = r.next;
        }
        while(r!=null){
            l = l.next;
            r = r.next;
            pre = pre.next;
        }
        pre.next = l.next;
        return pse.next;
    }
}
