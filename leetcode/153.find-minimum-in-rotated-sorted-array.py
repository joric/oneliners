from lc import *

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]

class Solution:
    def findMin(self, a: List[int]) -> int:
        return min(a)

# one of the shortest

class Solution:findMin=min

test('''
153. Find Minimum in Rotated Sorted Array
Solved
Medium
Topics
premium lock icon
Companies
Hint
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,881,400/5.4M
Acceptance Rate
53.8%
Topics
Array
Binary Search
icon
Companies
Hint 1
Array was originally in ascending order. Now that the array is rotated, there would be a point in the array where there is a small deflection from the increasing sequence. eg. The array would be something like [4, 5, 6, 7, 0, 1, 2].
Hint 2
You can divide the search space into two and see which direction to go. Can you think of an algorithm which has O(logN) search complexity?
Hint 3
All the elements to the left of inflection point > first element of the array.
All the elements to the right of inflection point < first element of the array.
Similar Questions
Search in Rotated Sorted Array
Medium
Find Minimum in Rotated Sorted Array II
Hard
''')
