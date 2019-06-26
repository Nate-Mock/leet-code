"""
You are climbing a stair case. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?
"""
# Runtime: 32 ms (faster than 88.97% of Python3 submissions)
# Memory Usage: 13.1 MB (less than 84.66% of Python3 submissions)

# This problem follows a fibonacci sequence! After realizing that, the solution is pretty simple.

class Solution:
    def climbStairs(self, n: int) -> int:
        i, j = 0, 1
        for _ in range(n):
            i, j = j, i + j
        return j
