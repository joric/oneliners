from lc import *

# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/solutions/1357692/bisect-whenever-you-can-99-speed-by-evge-hg1s/?envType=daily-question&envId=2026-04-19

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        nums2.reverse()
        max_dist = 0
        len1 = len(nums2) - 1
        for i, n in enumerate(nums1):
            max_dist = max(max_dist, len1 - bisect_left(nums2, n) - i)
            if len1 - i <= max_dist:
                break
        return max_dist

class Solution:
    def maxDistance(self, a: List[int], b: List[int]) -> int:
        b.reverse();
        m = 0
        for i,x in enumerate(a):
            m = max(m, len(b)-i+~bisect_left(b,x))
            if len(b)-i<=m:
                return m
        return m

class Solution:
    def maxDistance(self, a: List[int], b: List[int]) -> int:
        b.sort();return max([0]+[len(b)-i+~bisect_left(b,x)for i,x in enumerate(a)])

class Solution:
    def maxDistance(self, a: List[int], b: List[int]) -> int:
        return max([j:=0]+[i-(j:=j+(j>=len(a)or a[j]>x))for i,x in enumerate(b)])

class Solution:
    def maxDistance(self, a: List[int], b: List[int]) -> int:
        return max(j:=0,*[i-(j:=j+(j>=len(a)or a[j]>x))for i,x in enumerate(b)])

test('''
1855. Maximum Distance Between a Pair of Values
Medium
Topics
premium lock icon
Companies
Hint
You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.

 

Example 1:

Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
Output: 2
Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).
Example 2:

Input: nums1 = [2,2,2], nums2 = [10,10,1]
Output: 1
Explanation: The valid pairs are (0,0), (0,1), and (1,1).
The maximum distance is 1 with pair (0,1).
Example 3:

Input: nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
Output: 2
Explanation: The valid pairs are (2,2), (2,3), (2,4), (3,3), and (3,4).
The maximum distance is 2 with pair (2,4).


Other examples:

Input: nums1 = [5,4], nums2 = [3,2]
Output: 0

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 105
Both nums1 and nums2 are non-increasing.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
62,750/115.6K
Acceptance Rate
54.3%
Topics
Senior
Array
Two Pointers
Binary Search
Weekly Contest 240
icon
Companies
Hint 1
Since both arrays are sorted in a non-increasing way this means that for each value in the first array. We can find the farthest value smaller than it using binary search.
Hint 2
There is another solution using a two pointers approach since the first array is non-increasing the farthest j such that nums2[j] ≥ nums1[i] is at least as far as the farthest j such that nums2[j] ≥ nums1[i-1]
Similar Questions
Two Furthest Houses With Different Colors
Easy
''')
