"""
Implement strStr().

Return the index of the first occurrence of 'needle' in 'haystack', or -1 if 'needle' 
is not part of 'haystack'.

Clarification:
what should we return when 'needle' is an empty string? This is a great question to
ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
"""
# Runtime: 32ms (faster than 96.88% of Python3 submissions)
# Memory Usage: 13.1MB (less than 95.65% of Python3 submissions)

class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		return haystack.find(needle)

"""
This is another one of those situations where there's a very simple, Pythonic answer.
Which reveals just how simple Python makes some things.
So I'm going to write a less Pythonic answer, just to see what sort of algorithm-esque
solution I come up with.
"""

class Solution
	def strStr(self, haystack: str, needle: str) -> int:
		# First thought - I'd like to keep my loop code clean, so 
		# I'll grab the length of both strings.
		hlen = len(haystack)
		nlen = len(needle)

		# Next, I'll want to check if needle is an empty string.
		if nlen == 0 or haystack == needle:
			return 0

		# I'll need a pointer to move through haystack, starting at 0. 
		# I'll initiate the pointer for needle in the main loop.
		hp = 0

		# I'll move through haystack, comparing each letter to the first 
		# letter of needle. If there's a match, I'll keep comparing until 
		# we reach the end of needle or there's not a match, in which case 
		# I'll continue looking through haystack. If we've reached 
		# hlen - nlen without finding a match, return -1.
		
		while hp < hlen - nlen:
			np = 0
			if haystack[hp] == needle[np]:
				while np < nlen:
					if haystack[hp + np] != needle[np]:
						break
					np += 1
				if np == nlen:
					return hp
			hp += 1

		return -1
						
				

		
