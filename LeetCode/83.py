# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        res = head
        prev, curr = head, head.next
        while curr:
            while curr and curr.val == prev.val:
                curr = curr.next
            if not curr:
                prev.next = None
                break
            prev.next = curr
            prev, curr = curr, curr.next
        return head