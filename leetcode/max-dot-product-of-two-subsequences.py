from lc import *

# https://leetcode.com/problems/max-dot-product-of-two-subsequences/discuss/1093527/Python-simple-recursive-solution-with-lru-not-efficient.

class Solution:
    def maxDotProduct(self, a: List[int], b: List[int]) -> int:
        return(f:=cache(lambda i,j,k:max(a[i]*b[j]+f(i+1,j+1,1),f(i+1,j,k),f(i,j+1,k))if i<len(a)and j<len(b)else not k and-inf))(0,0,0)

class Solution:
    def maxDotProduct(self, a: List[int], b: List[int]) -> int:
        return(f:=cache(lambda i,j,k:max(a[i]*b[j]+f(i+1,j+1,1),f(i+1,j,k),f(i,j+1,k))if a[i:]and b[j:]else not k and-inf))(0,0,0)

test('''
1458. Max Dot Product of Two Subsequences
Hard

804

14

Add to List

Share
Given two arrays nums1 and nums2.

Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

 

Example 1:

Input: nums1 = [2,1,-2,5], nums2 = [3,0,-6]
Output: 18
Explanation: Take subsequence [2,-2] from nums1 and subsequence [3,-6] from nums2.
Their dot product is (2*3 + (-2)*(-6)) = 18.
Example 2:

Input: nums1 = [3,-2], nums2 = [2,-6,7]
Output: 21
Explanation: Take subsequence [3] from nums1 and subsequence [7] from nums2.
Their dot product is (3*7) = 21.
Example 3:

Input: nums1 = [-1,-1], nums2 = [1,1]
Output: -1
Explanation: Take subsequence [-1] from nums1 and subsequence [1] from nums2.
Their dot product is -1.
 

Example 4:

Input: nums1 = [-1,0], nums2 = [1,0]
Output: 0

Constraints:

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 1000
''')

