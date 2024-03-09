from lc import *

class Solution:
    def getCommon(self, a: List[int], b: List[int]) -> int:
        i=j=0
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                i += 1
            elif a[i]>b[j]:
                j += 1
            else:
                return a[i]
        return -1

# https://leetcode.com/problems/minimum-common-value/discuss/3082385/Python-1-line

class Solution:
    def getCommon(self, a: List[int], b: List[int]) -> int:
        return min({*a}&{*b},default=-1)

class Solution:
    def getCommon(self, a: List[int], b: List[int]) -> int:
        return min({*a}&{*b}or[-1])

test('''
2540. Minimum Common Value
Easy

531

15

Add to List

Share
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 

Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.

More examples:

Input: nums1 = [1,2,3], nums2 = [4,5,6]
Output: -1


Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.
Accepted
59,988
Submissions
119,608
''')
