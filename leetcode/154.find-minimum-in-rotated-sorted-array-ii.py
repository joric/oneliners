from lc import *

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        while i < j:
            mid = (i + j) // 2
            if nums[mid] > nums[j]:
                i = mid+1
            elif nums[mid] < nums[j]:
                j = mid
            else:
                j -= 1
        return nums[j]

class Solution:
    def findMin(self, a: List[int]) -> int:
        return min(a)

test('''
154. Find Minimum in Rotated Sorted Array II
Solved
Hard
Topics
premium lock icon
Companies
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [1,3,5]
Output: 1
Example 2:

Input: nums = [2,2,2,0,1]
Output: 0
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums is sorted and rotated between 1 and n times.
 

Follow up: This problem is similar to Find Minimum in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

 

 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
597,076/1.3M
Acceptance Rate
44.6%
Topics
Array
Binary Search
icon
Companies
Similar Questions
Find Minimum in Rotated Sorted Array
Medium
''')
