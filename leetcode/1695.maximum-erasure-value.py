from lc import *

# https://leetcode.com/problems/maximum-erasure-value/

class Solution: # MLE
    def maximumUniqueSubarray(self, a: List[int]) -> int:
        return(f:=lambda l,r,s,c,b:b if r>=len(a)else f(l+1,r,s-{a[l]},c-a[l],b)if a[r]in s else f(l,r+1,s|{a[r]},c+a[r],max(b,c+a[r])))(0,0,set(),0,0)

class Solution:
    def maximumUniqueSubarray(self, a: List[int]) -> int:
        return(f:=lambda l,r,s,c,b:b if r>=len(a)else f(l+1,r,s.remove(a[l])or s,c-a[l],b)if a[r]in s else f(l,r+1,s.add(a[r])or s,c+a[r],max(b,c+a[r])))(0,0,set(),0,0)

test('''
1695. Maximum Erasure Value
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 

Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
Seen this question in a real interview before?
1/5
Yes
No
Accepted
151,159/253.9K
Acceptance Rate
59.5%
Topics
Array
Hash Table
Sliding Window
icon
Companies
Hint 1
The main point here is for the subarray to contain unique elements for each index. Only the first subarrays starting from that index have unique elements.
Hint 2
This can be solved using the two pointers technique
Similar Questions
Longest Substring Without Repeating Characters
Medium
''')
