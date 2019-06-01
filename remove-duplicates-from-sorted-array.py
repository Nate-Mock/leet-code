"""
Given a sorted array nums, remove the duplicates in-place such that each
element appears only once and return the new length.
Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.
"""
# Runtime: 72ms (better than 45.22% of Python3 submissions)
# Memory Usage: 14.8 MB (better than 50.79% of Python3 submissions)

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		l = 0
		while l < len(nums) - 1:
			if nums[l] == nums[l+1]:
				del(nums[l+1)
				continue
			l += 1
		return len(nums)
