from lc import *

# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2755/6-lines-O(log(min(mn)))-Python

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        i = bisect_left(range(m), True, key=lambda i: after-i-1 < 0 or a[i] >= b[after-i-1])
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0

class Solution(object):
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        return(n:=len(a+b))and(sum(sorted(a+b)[n//2-1:n//2+1])/2.0,sorted(a+b)[n//2])[n%2]

class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        return median(a+b)

test('''
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
''')
