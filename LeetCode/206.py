# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Version 1, Iteration
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        a, b = head, head.next
        head.next = None
        while b:
            c = b.next
            b.next = a
            a, b = b, c
        return a

# Version 2, Recursion
class Solution(object):
    def reverseList(self, head, last=None):
        if not head:
            return last
        next = head.next
        head.next = last
        return self.reverseList(next, head)