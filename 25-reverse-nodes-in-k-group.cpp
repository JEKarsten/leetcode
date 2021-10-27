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
    ListNode* reverseKGroup(ListNode* head, int k) {
        int counter = 0;
        ListNode* currentNode = head;
        while (currentNode != nullptr) {
            counter++;
            currentNode = currentNode->next;
        }
        
        ListNode* result = head;
        currentNode = result;
        bool firstLoop = true;
        ListNode* previousEnd = new ListNode();
        while (counter >= k) {
            ListNode** batch = new ListNode*[k];
            
            for (int i = 0; i < k; i++) {
                batch[i] = currentNode;
                currentNode = currentNode->next;
            }
            
            for (int i = k-1; i > 0; i--) {
                batch[i]->next = batch[i-1];
            }
            batch[0]->next = currentNode;
            
            if (firstLoop) {
                result = batch[k-1];
                previousEnd = batch[0];
                firstLoop = false;
            } else {
                previousEnd->next = batch[k-1];
                previousEnd = batch[0];
            }
            counter -= k;
        }
        
        return result;
    }
};