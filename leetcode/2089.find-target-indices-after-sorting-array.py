from lc import *

# https://leetcode.com/problems/find-target-indices-after-sorting-array/description/?envType=daily-question&envId=2026-10-19

class Solution:
    def targetIndices(self, a: list[int], t: int) -> list[int]:
        return[i for i,x in enumerate(sorted(a))if x==t]

test('''
2089. Find Target Indices After Sorting Array
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

 

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.
Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i], target <= 100
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
301,838/385K
Acceptance Rate
78.4%
Topics
Mid Level
Array
Binary Search
Sorting
Weekly Contest 269
icon
Companies
Hint 1
Try "sorting" the array first.
Hint 2
Now find all indices in the array whose values are equal to target.
Similar Questions
Find First and Last Position of Element in Sorted Array
Medium
Rank Transform of an Array
Easy
Find Words Containing Character
Easy
''')
