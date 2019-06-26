"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guarenteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer
part of the result is returned.
"""
# Runtime: 28 ms (faster than 99.61% of Python3 submissions)
# Memory Usage: 13.1 MB (less than 81.62% of Python3 submissions)

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**.5)
