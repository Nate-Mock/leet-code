"""
Given an inter array nums, find the congifuous subarray (containing at
least one number) which has the largest sum and return its sum."
"""
# Runtime: 44 ms (faster than 77.72% of Python3 submissions)
# Memory Usage: 13.3 MB (less than 98.75% of Python3 submissions)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = -2**31
        tmp = 0
        for n in nums:
            tmp += n
            m = max(mx, tmp)
            if t < 0:
                t = 0
        return mx
