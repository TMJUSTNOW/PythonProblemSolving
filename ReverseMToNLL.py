# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # move the pointers to the m and n position
        start = head
        end = head
        previous  = None
        after = None
        m_copy = m
        n_copy = n
        while m_copy > 1:
            #saving trailing pointer
            previous = start
            start  = start.next
            m_copy = m_copy -1
        while n_copy > 1:
            end = end.next
            n_copy = n_copy -1
        if previous:
            previous.next = None
        after = end.next
        end.next = None
        self.reverseNodes(start, end)
        if previous:
          previous.next = end
        start.next = after
        if m == 1:
           return end
        else:
            return head
        
    def reverseNodes(self, start, end):
        if not start:
            return end
        forward_next = start.next
        backward_next = start
        backward_next.next = end
        return self.reverseNodes(forward_next, backward_next)
