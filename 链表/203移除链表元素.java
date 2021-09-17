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
    public ListNode removeElements(ListNode head, int val) {
        ListNode pse = new ListNode(0); //伪节点val==0，不是空节点
        pse.next = head;  //伪节点指向head节点

        ListNode pre = pse,curr = head; //两个指针，但是其实定义了三个位置关系，pre，curr（待删除的元素）、curr.next(删除后被指的元素)
        while (curr != null){  // curr指针前进推动循环以及退出
            if (curr.val == val){
                pre.next = curr.next;  // 删掉直接变指向，但是此时curr仍然指着被删除的元素，curr.next 依然可以访问到被下一个元素
            }else {
                pre = curr;  // 哨兵节点 不变next指向，就变一下元素位置
            }
            curr = curr.next; // 当前元素，任何时候都要前进1
        }

        return pse.next;   // 重要哦
    }
}
