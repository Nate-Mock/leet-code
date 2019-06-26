"""
Given an integer, convert it to a roman numeral. Input is guaranteed to be
within the range from 1 to 3999.
"""
# Runtime: 44 ms (less than 98.57% of Python3 submissions)
# Memory Usage: 13.3 MB (less than 51.31% of Python3 submissions)

class Solution:
    def intToRoman(self, num: int) -> str:
        i2r = [(1000, "M"),(900, "CM"),(500, "D"),(400,"CD"),(100, "C"),\
                (90,"XC"),(50, "L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),\
                (4,"IV"),(1, "I")]
        r = ""
        for l in i2r:
            c = num // t[0]
            num = num % t[0]
            r += c * l[1]
        return r
