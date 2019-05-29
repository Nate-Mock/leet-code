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

# Looking to the discussion section, I found a golfer! Here was his solution:
Class Solution:
	def reverse(self, x):
		s = cmp(x,0)
		r = int(`s*x`[::-1])
		return s*r * (r < 2**31)

# One thing I notice here - beyond the fact that this code is 1/4 the length
# of my own - is that Stefan (the author) simply checks if r is less than 2**31.
# Initially, I was concerned this would leave out the edge case of when
# r == 2**31 and s*r == -2**31, a valid 32 bit signed integer, 
# however after some consideration I realized that's not possible:
# in order for r to equal -2147483648 (-2**31), x would have to be
# -8463847412, which isn't a valid input given the 32 bit constraint. 
