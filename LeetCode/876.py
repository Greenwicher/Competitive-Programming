# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cnt = 0
        listNode = []
        while head:
            listNode.append(head)
            head = head.next
        return listNode[len(listNode)//2]