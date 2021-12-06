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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode pse = new ListNode(0);
        ListNode head = pse;
        while(l1 != null && l2 != null){
            if(l1.val <= l2.val){
                head.next = l1;
                l1 = l1.next;
            }else{
                head.next = l2;
                l2 = l2.next;
            }
            head = head.next;
        }
        if(l1 != null){
            head.next = l1;
        }
        else if (l2 != null){
            head.next = l2;
        }
        return pse.next;
    }
}

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pse = ListNode()
        res = pse
        while list1 and list2:
            if list1.val <= list2.val: 
                pse.next = list1
                pse = pse.next
                list1 = list1.next
            else:
                pse.next = list2
                pse = pse.next
                list2 = list2.next
        if list1:
            pse.next = list1
        if list2:
            pse.next = list2
        return res.next
