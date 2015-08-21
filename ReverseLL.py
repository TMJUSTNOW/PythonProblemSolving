# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        reversed = self.reverseNodes(head, None)
        return reversed
    
    def reverseNodes(self, forward_head, backward_head):
        if not forward_head:
            return backward_head
        forward_head_next = forward_head.next
        backward_head_next = forward_head
        backward_head_next.next = backward_head
        return self.reverseNodes(forward_head_next, backward_head_next)
        