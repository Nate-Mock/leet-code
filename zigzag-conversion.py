"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this:
    P A H N
    APLSIIG
    Y I R
And then read line by line: "PAHNAPLSIIGYIR"

Writecode that will take a string and make this conversion given a number
of rows.
"""
# Runtime: 52ms (faster than 99.52% of Python3 submissions)
# Memory Usage: 13.2 MB (less than 61.54% of Python3 submissions)

class Solution:
    def convert(self, s:str, numRows: int) -> str:
        
        if numRows == 1 or len(s) <= numRows:
            return s
        
        ret = ['' for i in range(numRows)]
        g, d = 0, 1

        for c in s:
            ret[g] += c
            if g == numRows - 1:
                d = -1
            elif g == 0:
                d = 1
            g += d

        return ''.join(ret)
