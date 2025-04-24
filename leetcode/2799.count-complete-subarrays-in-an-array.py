from lc import *

# https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, a: List[int]) -> int:
        t=len({*a});n=len(a);return sum((c:=set())or n-next((j for j in range(i,n)if c.add(a[j])or t==len(c)),n)for i in range(n))

test('''
2799. Count Complete Subarrays in an Array
Solved
Medium
Topics
Companies
Hint
You are given an array nums consisting of positive integers.

We call a subarray of an array complete if the following condition is satisfied:

The number of distinct elements in the subarray is equal to the number of distinct elements in the whole array.
Return the number of complete subarrays.

A subarray is a contiguous non-empty part of an array.

 

Example 1:

Input: nums = [1,3,1,2,2]
Output: 4
Explanation: The complete subarrays are the following: [1,3,1,2], [1,3,1,2,2], [3,1,2] and [3,1,2,2].
Example 2:

Input: nums = [5,5,5,5]
Output: 10
Explanation: The array consists only of the integer 5, so any subarray is complete. The number of subarrays that we can choose is 10.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2000
Seen this question in a real interview before?
1/5
Yes
No
Accepted
89.4K
Submissions
124.5K
Acceptance Rate
71.8%
Topics
Companies
Hint 1
Let’s say k is the number of distinct elements in the array. Our goal is to find the number of subarrays with k distinct elements.
Hint 2
Since the constraints are small, you can check every subarray.
Similar Questions
Longest Substring Without Repeating Characters
Medium
Subarrays with K Different Integers
Hard
''')


