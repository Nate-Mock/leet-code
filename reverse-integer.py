"""
Given a 32 bit signed integer, reverse the digits of an integer.
"""
# My first solution was to change the int to a string, then 
# use the [::-1] pattern to reverse the string:
# Runtime: 32 ms (better than 98.22% of submissions)
# Memory Usage: 13.4 MB (better than 6.9% of submissions)
class Solution:
	def reverse(self, x: int) -> int:
		isneg = False
		if x < 0:
			x = abs(x)
			isneg = True
		r = int(str(x)[::-1])
		r = r if isneg == False else r * -1
		if r >= 2**31 -1 or r <= -2**31:
			return 0
		return r

# I wondered if the memory usage was due to the type conversions,
# so I tried again, this time keeping 'x' as an int.
# Runtime: 24 ms (better than 99.96% of submissions)
# Memory Usage: 13.3 MB (better than 23.47% of submissions)
class Solution:
	def reverse(self, x: int) -> int:
		isneg = False
		if x < 0:
			x = abs(x)
			isneg = True
		r = 0
		while x != 0:
			r = r * 10 + x % 10
			x = x // 10
		r = r if isneg == False else r * -1
		if r <= -2**31 or r >= 2**31 - 1:
			return 0
		return r
