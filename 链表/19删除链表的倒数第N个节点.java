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
