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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* p = l1;
        ListNode* q = l2;
        ListNode* result = new ListNode(0);
        ListNode* r = result;
        while(p&&q){
            if(p->val < q->val){
                r->next = p;
                r = r->next;
                p = p->next;
            }else{
                r->next = q;
                r = r->next;
                q = q->next;
            }
        }
        if(p) r->next = p;
        if(q) r->next = q;
        return result->next;
    }
};
