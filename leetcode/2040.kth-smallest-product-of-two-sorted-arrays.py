from lc import *

# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/solutions/1524159/python-binary-search-solution-explained/

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def check(x):
            total = 0
            for n1 in nums1:
                if n1 > 0: total += bisect.bisect(nums2, x//n1)
                if n1 < 0: total += len(nums2) - bisect_left(nums2, ceil(x/n1))
                if n1 == 0 and x >= 0: total += len(nums2)
            return total
        beg, end = -10**10 - 1, 10**10 + 1
        while beg + 1 < end:
            mid = (beg + end)//2
            if check(mid) >= k:
                end = mid
            else:
                beg = mid
        return beg + 1

class Solution:
    def kthSmallestProduct(self, a: List[int], b: List[int], k: int) -> int:
        f=lambda x:sum(bisect_right(b,x//y)if y>0 else len(b)-bisect_left(b,ceil(x/y))if y<0 else(x>=0)*len(b)for y in a)
        l,r = -10**10-1, 10**10+1
        while l < r:
            m = (l + r)//2
            if f(m) >= k:
                r = m
            else:
                l = m + 1
        return l

class Solution:
    def kthSmallestProduct(self, a: List[int], b: List[int], k: int) -> int:
        f=lambda x:sum(bisect_right(b,x//y)if y>0 else len(b)-bisect_left(b,ceil(x/y))if y<0 else(x>=0)*len(b)for y in a);return bisect_left(range(2*(r:=10**10)),k,key=lambda i:f(i-r))-r

# POTD 2025-06-25

class Solution:
    def kthSmallestProduct(self, a: List[int], b: List[int], k: int) -> int:
        l,t,f=bisect_left,10**10,lambda x:sum(bisect_right(b,x//y)if y>0 else len(b)-l(b,-(-x//y))if y<0 else(x>=0)*len(b)for y in a);return l(range(2*t),k,key=lambda i:f(i-t))-t

test('''
2040. Kth Smallest Product of Two Sorted Arrays
Hard

684

37

Add to List

Share
Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, return the kth (1-based) smallest product of nums1[i] * nums2[j] where 0 <= i < nums1.length and 0 <= j < nums2.length.
 

Example 1:

Input: nums1 = [2,5], nums2 = [3,4], k = 2
Output: 8
Explanation: The 2 smallest products are:
- nums1[0] * nums2[0] = 2 * 3 = 6
- nums1[0] * nums2[1] = 2 * 4 = 8
The 2nd smallest product is 8.
Example 2:

Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
Output: 0
Explanation: The 6 smallest products are:
- nums1[0] * nums2[1] = (-4) * 4 = -16
- nums1[0] * nums2[0] = (-4) * 2 = -8
- nums1[1] * nums2[1] = (-2) * 4 = -8
- nums1[1] * nums2[0] = (-2) * 2 = -4
- nums1[2] * nums2[0] = 0 * 2 = 0
- nums1[2] * nums2[1] = 0 * 4 = 0
The 6th smallest product is 0.
Example 3:

Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
Output: -6
Explanation: The 3 smallest products are:
- nums1[0] * nums2[4] = (-2) * 5 = -10
- nums1[0] * nums2[3] = (-2) * 4 = -8
- nums1[4] * nums2[0] = 2 * (-3) = -6
The 3rd smallest product is -6.
 

Constraints:

1 <= nums1.length, nums2.length <= 5 * 104
-105 <= nums1[i], nums2[j] <= 105
1 <= k <= nums1.length * nums2.length
nums1 and nums2 are sorted.
Accepted
11,804
Submissions
40,683
''')