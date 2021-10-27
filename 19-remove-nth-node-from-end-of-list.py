# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current_next = head.next
        counter = 1
        
        while current_next != None:
            current_next = current_next.next
            counter += 1
        
        if counter == n:
            return head.next
        
        current_node = head
        for i in range(counter - n - 1):
            current_node = current_node.next
        
        node_before = current_node
        node_after = current_node.next.next
        node_before.next = node_after
        
        return head