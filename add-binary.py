"""
Given twobinary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.
"""
# Runtime: 32 ms (faster than 98.28% of Python3 submissions)
# Memory Usage: 13 MB (less than 93.39% of Python3 submissions)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
