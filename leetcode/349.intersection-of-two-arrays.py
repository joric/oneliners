from lc import *

# https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        i=j=0
        a.sort()
        b.sort()
        r = []
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                i += 1
            elif a[i]>b[j]:
                j += 1
            else:
                if not r or a[i]!=r[-1]:
                    r.append(a[i])
                i += 1
                j += 1
        return r

class Solution:
    def intersection(self, a: List[int], b: List[int]) -> List[int]:
        return{*a}&{*b}

test('''
349. Intersection of Two Arrays
Easy

5560

2240

Add to List

Share
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
Accepted
1,019,623
Submissions
1,407,756
''', sort=True)
