"""
Given a string s consists of upper/lower-case alphabets and empty characters
' ', return the length of the last word in the string.

If the last word does not exist, return 0.
"""
# Runtime: 24 ms (faster than 99.75% of Python3 submissions)
# Memory Usage: 13.2 MB (less than 42.27% of Python3 submissions)

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for c in s[::-1].strip():
            if c == " ":
                break
            count += 1
        return count
