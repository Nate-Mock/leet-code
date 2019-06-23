"""
Given a non-empty array of digits representing a non-negative integer, plus
one to the integer.

The digits are stored such that the most significant digit is at the head of 
the list, and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the
number 0 itself.
"""
# Runtime: 32 ms (faster than 95.05% of Python3 submissions)
# Memory Usage: 13.1 MB (less than 79.98% of Python3 submissions)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] == 0
            else:
                digits[i] = digits[i] + 1
                return digits
            i -= 1
        return [1] + digits
