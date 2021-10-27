# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        
        mega_list = []
        for k in lists:
            current_node = k
            while current_node != None:
                mega_list.append(current_node.val)
                current_node = current_node.next
        
        if mega_list == []: return None
        mega_list.sort()
        
        result_head = ListNode()
        result_current_node = result_head
        for i in range(len(mega_list)):
            result_current_node.val = mega_list[i]
            if i == len(mega_list) - 1: break
            result_current_node.next = ListNode()
            result_current_node = result_current_node.next
        return result_head