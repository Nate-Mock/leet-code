"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log(m+n)).

You may assume nums1 and nums2 cannot be both empty.
"""
# Runtime: 48 ms (faster than 99.15% of Python3 submissions)
# Memory Usage: 13.3 MB (less than 81.30% of Python3 submissions)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ma = sorted(nums1 + nums2)
        if len(ma) % 2 != 0:
            return ma[len(ma)//2]
        else:
            i = len(ma) // 2
            return (ma[i - 1] + ma[i] / 2
