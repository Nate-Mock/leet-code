"""
Given a sorted linked list, delete all duplicates such that each element
appears only once.
"""
# Runtime: 48 ms (faster than 72.23% of Python3 submissions)
# Memory Usage: 13.1 MB (less than 70.51% of Python3 submissions)

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = ListNode(None)
        x = h
        while head:
            if x.val == head.val:
                head = head.next
                continue
            x.next = ListNode(head.val)
            x, head = x.next, head.next
        return h.next
            

# I didn't think this was a particularly elegant answer, so I looked
# at the discussion section and was inspired to create this:

# Runtime: 48 ms (faster than 72.23% of Python3 submissions)
# Memory Usage: 13 MB (less than 87.64% of Python3 submissions)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        h = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return h
