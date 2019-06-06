"""
Given a sorted array and a target value, return the index if the target is found.
if not, return the indexwhere it would be if it were inserted in order.

You may assume no duplicates in the array.
"""
# Runtime: 32 ms (faster than 96.19% of Python3 submissions)
# Memory Usage: 13.6 MB (less than 82.30% of Python3 submissions)

class Solution
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)
