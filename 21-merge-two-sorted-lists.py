# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        current_node = result
        while l1 != None and l2 != None:
            current_node.next = ListNode()
            current_node = current_node.next
            if l1.val <  l2.val:
                current_node.val = l1.val
                l1 = l1.next
            else:
                current_node.val = l2.val
                l2 = l2.next
        if l1 != None:
            current_node.next = l1
        elif l2 != None:
            current_node.next = l2
        return result.next