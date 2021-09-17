/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {   // stack放链表节点再弹出
    public int[] reversePrint(ListNode head) {
        Stack<ListNode> stackNode = new Stack<ListNode>();
        ListNode temp = head;
        while(temp != null){
            stackNode.push(temp);
            temp = temp.next;
        }
        int size = stackNode.size();
        int[] listAns = new int[size];
        for(int i = 0; i < size; i++){
            listAns[i]=stackNode.pop().val;
        }
        return listAns;
    }
}
