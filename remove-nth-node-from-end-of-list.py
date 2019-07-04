"""
Givena linked list, remove the n-th node from the end of list and
return its head.

Note: given n will always be valid
"""
# I struggled with this one quite a bit. While I was able to pass
# almost all of the test cases, the test case of removing the 
# one and only list element proved difficult to reconcile (with any
# kind of elegance) with the non-edge cases.
# In particular, double next-ing at the end wasn't an option, but
# removing it broke the rest of the program.
# After a while, I realized that adding a wrapper-node of sorts
# would fix it. Hooray!

# Runtime: 32 ms (faster than 96.77% of Python3 submissions)
# Memory Usage: 31.1 MB (less than 85.12% of Python3 submissions)

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, x):
#       self.val = x
#       self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        h = ListNode(None)
        h.next = head
        nd1 = nd2 = h
        for _ in range(n):
            nd2 = nd2.next
        while nd2.next:
            nd1 = nd1.next
            nd2 = nd2.next
        nd1.next = nd1.next.next
        return h.next
