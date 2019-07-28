/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode head(0), *h = &head;
        int carry = 0;
        while( l1 != NULL || l2 != NULL ){
            int x = ( l1 == NULL ) ? 0 : l1->val;
            int y = ( l2 == NULL ) ? 0 : l2->val;
            int sum = x + y + carry;
            carry = sum / 10;
            h->next = new ListNode( sum % 10 );
            h = h->next;
            if( l1 != NULL ) l1 = l1->next;
            if( l2 != NULL ) l2 = l2->next;
        }
        if( carry > 0 ){
            h->next = new ListNode( carry );
        }
        return head.next;
    }
};
