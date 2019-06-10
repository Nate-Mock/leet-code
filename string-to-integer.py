"""
Implement 'atoi' which converts a string to an ingeter.

The function first discards as many whitespace characters as nessecary
until the first non-whitespace character is found. Then, starting at this
character, takes an optional initial plus or minus sign followed by as
many numerical digits as possible, and intreprets them as a numerical value.

The string can contain additional characters after those that form the
integralnumber, which are ignored and have no effect on the behavior
of this function.

If the first sequence of non-whitespace characters is not a valid integral
number, or if no such sequence exists because either str is empty or it
contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:
    - Only the whitespace character ' ' is considered as a whitespace character.
    - Assume we are dealing with an environment which could only store 
      integers within the 32-bit signed integer range: [-2**31, 2**31 - 1].
      If the numerical value is out of the range of representable values,
      INT_MAX (2**31 - 1) or INT_MIN (-2**31) is returned.
"""
# Runtime: 40 ms (faster than 90.76% of Python3 submissions)
# Memory Usage: 13 MB (less than 95.63% of Python3 submissions)

class Solution:
    def myAtoi(self, str: str) -> int:
        nums = '0123456789'
        flag = '+-'
        n = ''

        for c in str:
            if c == ' ' and len(n) == 0:
                continue
            if c not in nums and c not in flag or len(n) > 0 and c in flag:
                if len(n) == 0:
                    return 0
                break
            if c in nums or c in flag:
                n += c

            s = 1

            try:
                if n[0] in flag:
                    d = n[0]
                    n = n[1:]
                    if d == '-':
                        s = -1

                n = int(n) * s

                if n < -2**32:
                    return -2**32
                if n > 2**31 - 1:
                    return 2**31 - 1
                return n
            
            except:
                return 0
