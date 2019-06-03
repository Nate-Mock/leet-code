"""
Given an array nums and value val, remove all instances of that value in-place
and return the new length.

Do not allocate extras space for another array, you must do this by modifying the input
array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
# Runtime: 32 ms (better than 97.37% of Python3 submissions)
# Memory Usage: 13.2 MB (better than 40.13% of Python3 submissions)

class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		while val in nums:
			nums.remove(val)
		return len(nums)

"""
This one felt like cheating - it's just so simple in Python.
The next language I'd like to tackle is C. I'll certainly need a more
algorithmic answer when I get there.
"""
