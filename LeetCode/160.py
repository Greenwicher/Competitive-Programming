# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not(headA) or not(headB):
            return None
        a, b = [], []
        while headA:
            a.append(headA)
            headA = headA.next
        while headB:
            b.append(headB)
            headB = headB.next
        a = a[::-1]
        b = b[::-1]
        for i in range(min(len(a), len(b))):
            if a[i].val != b[i].val:
                break
        if a[i].val != b[i].val:
            if i == 0:
                return None
            else:
                return a[i-1]
        else:
            return a[i]