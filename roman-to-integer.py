"""
Roman numerals are represented by seven different symbols: I, V, X, L,
C, D, and M.

Symbol  |   Value
    I       1
    V       5
    X       10
    L       50
    C       100
    D       500
    M       1000

For example, two is writtenas II in Roman numeral, just two one's added 
together. Twelve is written as XII, which is simply X + II. The number
twenty seven is writeen as XVII, whichis XX + V + II.

Roman numerals are usually written from largest to smallest from left
to right. However,the numeral four is not IIII. Instead,the number
four is written as IV. Because the one is before the five we subtract
it making four. The same principle applies to the number nine, which is
written asIX. There are six instances where subtraction is used:
    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a Roman numeral, convert it to an integer. Input is guarenteed to
be within therange from 1 to 3999.
"""
# Runtime: 48 ms (faster than 99.40% of Python3 submissions)
# Memory Usage: 13.2 MB (less than 74.66% of Python3 submissions)

class Solution:
    def romanToInt(self, s: str) -> int:
        r2i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        nums = [r2i[r] for r in s]
        i = 0
        for ix, n in enumerate(nums):
            if (ix + 1) < len(nums) and nums[ix] < nums[ix+ 1]:
                i -= n
                continue
            i += n
        return i
