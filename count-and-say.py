"""
The count and saysequence is the sequence of integers with the first
five terms as following:

    1.  1
    2.  11
    3.  21
    4.  1221
    5.  111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read offas "one 2" then "one 1" or 1211.

Given an integer n where 1 <= n <= 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.
"""
# Runtime: 40ms (faster than 88.24% of Python3 submissions)
# Memory Usage: 13.2 MB (less than 56.76% of Python3 submissions)

class Solution:
    def countAndSay(self, n: int) -> str:
        say = '1'
        if n == 1:
            return say
        for i in range(n - 1):
            hold = ''
            idx= 0
            while idx < len(say):
                l = 0
                c = say[idx]
                while idx < len(say) and say[idx] == c:
                    l += 1
                    idx += 1
                hold = hold + str(l) + c
                l = 1
            say, hold = hold, ''
        return say

# While this solution worked, it's not particularly Pythonic.
# So I looked through the discussion section and found an answer that worked
# alot like mine, but did it using some neato Python itertools.
# The performance, it turns out, was identical to mine, although the code
# is /much/ more succinct.

class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit for digit, group in itertools.groupby(s))
        return s

