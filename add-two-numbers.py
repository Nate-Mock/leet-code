"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the twonumbers do not contain any leading zero, except the number 0 itself.
"""
# Runtime: 80 ms (better than 81% of Python3 submissions)
# Memory Usage: 13.1 MB (better than 80.28% of Python3 submissions)

class Solution:
	def addTwoNumbers(self, l1: listNode, l2: listNode) -> ListNode:
		s = 0
		e = 1
		while l1 or l2:
			if l1:
				s += l1.val * e
				l1 = l1.next
			if l2:
				s += l2.val * e
				l2 = l2.next
			e *= 10

		r = n = ListNode(0)

		if s == 0:
			return r

		while s:
			n.next = ListNode(s % 10)
			s = s // 10
			n = n.next

		return r.next
