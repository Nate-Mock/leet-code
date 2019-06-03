"""
Given a string, find the length of the longest substring without repeating characters
"""
# My first inclination was to use two pointers - one to move through the string and another /
# to look forward until a repeated character was found. The performance of this method, /
# however, was awful! 
# Runtime: 560 ms (faster than 15.06% of Python3 submissions)
# Memory Usage: 13.4 MB (less than 23.87% of Python3 submissions)

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		substr = ''
		holdstr = ''
		i = 0
		while i < len(s):
			j = i
			while j < len(s) and s[j] not in holdstr:
				holdstr = holdstr + s[j]
				j += 1
			if len(holdstr) > len(substr):
				substr = holdstr
			holdstr = ''
			i += 1
		return len(substr)

# Clearly, there's a better way. In particular, this function cycles through most of the /
# string multiple times - as the inner loop runs a check every time through the outer loop. /
# So I started thinking: how could I complete this while only looking at each character one /
# time? Here's what I came up with.
# Runtime: 72 ms (faster than 76.86% of Python3 submissions)
# Memory Usage: 13.3 MB (less than 47.49% of Python3 submissions)

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		i = 0
		substr = ''
		maxsub = 0
		while i < len(s):
			if s[i] in substr:
				substr = substr[substr.index(s[i]) + 1 :]
			substr = substr + s[i]
			maxsub = max(maxsub, len(substr))
			i += 1
		return maxsub

# This was a lot better! Still not great, though. So I did a little pythonic refactoring.
# Runtime: 56 ms (faster than 97.81% of Python3 submissions)
# Memory Usage: 13.3 MB (better than 46.25% of Python3 submissions)

class Solution:
	def lengthOgLongestSubstring(self, s: str) -> int:
		substr = ''
		maxsub = 0
		for l in s:
			if l in substr:
				substr = substr[substr.index(l) + 1:]
			substr = substr + l
			if maxsub < len(substr): maxsub = len(substr)
		return maxsub
