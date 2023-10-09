from lc import *

class Solution:
    def searchRange(self, v: List[int], t: int) -> List[int]:
        return(v.index(t),len(v)-1-v[::-1].index(t))if v.count(t)else(-1,-1)

class Solution:
    def searchRange(self, v: List[int], t: int) -> List[int]:
        a,b=bisect_left(v,t),bisect_right(v,t);return([-1]*2,(a,b-1))[a<b]

test('''
34. Find First and Last Position of Element in Sorted Array
Medium

18723

449

Add to List

Share
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
''')

