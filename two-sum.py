"""
Given an array of integers, return indicies of the two numbers such that they add up to a specific target.
You may assume each input would have exactly one solution, and you may not use the same element twice.
"""
# This was my first solution - a simple for loop
# Runtime: 796 ms (faster than 35.6% of python3 submissions)
# Memory Usage: 13.7 MB (better than 75.68% of solutions)
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums)):
			comp = target - nums[i]
			if search in nums and nums.index(comp) != i:
				return [i, nums.index(comp)]


# After submitting my solution, I read through some of the discussions and found a /much/ more ingenious solution using a dictionary with the keys as the compliment and the values as the original list index. 
# Runtime: 32 ms (faster than 99.12% of python3 submissions)
# Memory Usage 14.5 MB (better than 23.17% of python3 submissions)
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		m = {}
		for i, x in enumerate(nums):
			if x in m:
				return [m[x], i]
			m[target - x] = i
