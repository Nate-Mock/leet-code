"""
Determine whether an integer is a palindrome.
An integer is a palindrome when it reads the same way backward as forward.
"""
# Runtime: 60 ms (better than 98.41% of Python3 submissions)
# Memory Usage: 13.3 MB (better than 43.31% of Python3 submissions)

class Solution:
	def isPalindrome(self, x: int) -> bool:
		return True if str(x)[::-1] = str(x) else False
