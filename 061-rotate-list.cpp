/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        int length = 0;
        ListNode* current = head;
        ListNode* last = head;
        while (current != nullptr) {
            last = current;
            length++;
            current = current->next;
        }
        if (length < 2) return head;
        k = k % length;
        if (!k) return head;
        current = head;
        for (int i = 1; i < length - k; i++) {
            current = current->next;
        }
        ListNode* new_head = current->next;
        current->next = nullptr;
        last->next = head;
        return new_head;
    }
};