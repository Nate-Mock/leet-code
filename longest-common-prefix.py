"""
Write a function to find the longest common prefix amongst an array of strings.

If there is no common prefix, return an empty string "".
"""
# Runtime: 28 ms (faster than 99.64% of Python3 solutions)
# Memory Usage: 13.3 MB (better than 41.66% of Python3 solutions)

class Solution:
    def longestCommonPrefix(self, strs: List[str])-> str:
        if not strs: return ''
        i = 0
        for c in zip(*strs):
            if len(set(c)) > 1:
                break
            i += 1
        return strs[0][:i]
