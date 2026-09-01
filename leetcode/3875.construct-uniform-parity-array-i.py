from lc import *
 
# https://leetcode.com/problems/construct-uniform-parity-array-i/solutions/7680267/python-one-line-by-ante-8v22/?envType=daily-question&envId=2026-09-02

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True

class Solution:uniformArray=truth

test('''
3875. Construct Uniform Parity Array I
Easy
Topics
premium lock icon
Companies
Hint
You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

nums2[i] = nums1[i]
nums2[i] = nums1[i] - nums1[j], for an index j != i
Return true if it is possible to construct such an array, otherwise, return false.

 

Example 1:

Input: nums1 = [2,3]

Output: true

Explanation:

Choose nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1.
Choose nums2[1] = nums1[1] = 3.
nums2 = [-1, 3], and both elements are odd. Thus, the answer is true​​​​​​​.
Example 2:

Input: nums1 = [4,6]

Output: true

Explanation:​​​​​​​

Choose nums2[0] = nums1[0] = 4.
Choose nums2[1] = nums1[1] = 6.
nums2 = [4, 6], and all elements are even. Thus, the answer is true.
 

Constraints:

1 <= n == nums1.length <= 100
1 <= nums1[i] <= 100
nums1 consists of distinct integers.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
56,976/74.2K
Acceptance Rate
76.8%
Topics
Mid Level
Array
Math
Weekly Contest 494
icon
Companies
Hint 1
There is only one possible answer.
''')
