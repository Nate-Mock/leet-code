"""
Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai), n vertical lines aredrawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with the
x-axis forms a container, such that the container contains the most water.

Note: you may not slantthe container and n is at least 2.
"""
# My first submission had a lackluster performance...
# Runtime: 84 ms (faster than 13.5% of Python3 submissions)
# Memory Usage: 14.3 MB (less than 93.32% of Python3 submissions)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = 0
        l = 0
        r = len(height) - 1
        while l != r:
            if height[l] > height[r]:
                max_ = max(max_, height[r] * (r - l))
                r -= 1
            else:
                max_ = max(max_, height[r] * (r - l))
                l += 1
        return max_

# With a working solution in hand, I went about refactoring.
# Focusing on skipping unnessecary calculations, I got the following results:
# Runtime: 36 ms (faster than 100% of Python3 submissions)
# Memory Usage: 14.3 MB (better than 88.23% of Python3 submissions)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, = 0, len(height) - 1
        maxl, maxr = height[l], height[r]
        max_ = (r - l) * min(maxl, maxr)

        while l < r:
            if height[l] > height[r]:
                r -= 1
                if height[r]> maxr:
                    maxr = height[r]
                    a = (r - l) * min(maxl, maxr)
                    max_ = a if a > max_ else max_
            else:
                l += 1
                if height[l] > maxl:
                    maxl = height[l]
                    a = (r - l) * min(maxl, maxr)
                    max_ = a if a > max_ else max_
        return max_


