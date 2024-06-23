from lc import *

# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/discuss/609771/JavaC%2B%2BPython-Deques-O(N)

class Solution:
    def longestSubarray(self, a: List[int], l: int) -> int:
        i,q=0,[];[(insort(q,x),l<q[-1]-q[0]and(q.pop(bisect_left(q,a[i])),i:=i+1))for x in a];return len(q)

class Solution:
    def longestSubarray(self, a: List[int], l: int) -> int:
        q=[];[(insort(q,x),l<q[-1]-q[0]and q.pop(bisect_left(q,a.pop())))for x in a[::-1]];return len(q)

class Solution:
    def longestSubarray(self, a: List[int], l: int) -> int:
        q=[];[(insort(q,x),l<q[-1]-q[0]and q.pop(bisect_left(q,a.pop(0))))for x in a[:]];return len(q)

test('''
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
Medium

3312

138

Add to List

Share
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

 

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2 
Explanation: All subarrays are: 
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4. 
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4. 
Therefore, the size of the longest subarray is 2.
Example 2:

Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4 
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.
Example 3:

Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= limit <= 109
Accepted
132,230
Submissions
266,450
''')

