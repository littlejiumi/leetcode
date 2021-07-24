/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {  //双指针，两指针相差k
    public ListNode getKthFromEnd(ListNode head, int k) {
        ListNode former = head, latter = head;
        for(int i = 0; i < k; i++) former = former.next;
        while(former!=null) {
            latter= latter.next;
            former = former.next;
        }
        return latter;
    }
}
