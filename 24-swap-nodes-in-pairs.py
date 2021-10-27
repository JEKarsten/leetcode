# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head
        
        node1 = head
        node2 = head.next
        node3 = head.next.next
        
        head = node2
        head.next = node1
        head.next.next = self.swapPairs(node3)
        
        return head