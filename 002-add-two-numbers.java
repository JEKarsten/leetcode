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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode outputHead = new ListNode();
        ListNode i = l1;
        ListNode j = l2;
        ListNode curr = outputHead;
        int carry = 0;
        while (i != null || j != null) {
            int sum = carry + ((i != null) ? i.val : 0) + ((j != null) ? j.val : 0);
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (i != null) i = i.next;
            if (j != null) j = j.next;
        }
        if (carry > 0) {
            curr.next = new ListNode(carry);
        }
        return outputHead.next;
    }
}