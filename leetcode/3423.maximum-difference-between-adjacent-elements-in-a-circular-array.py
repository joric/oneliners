from lc import *

# https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/solutions/6299571/python-one-line/?envType=daily-question&envId=2025-06-12

class Solution:
    def maxAdjacentDistance(self, a: List[int]) -> int:
        return max(abs(x-y)for x,y in pairwise(a+[a[0]]))

class Solution:
    def maxAdjacentDistance(self, a: List[int]) -> int:
        return max(abs(x-a[i-1])for i,x in enumerate(a))

class Solution:
    def maxAdjacentDistance(self, a: List[int]) -> int:
        return max(abs(x-y)for x,y in zip(a,a[1:]+a))

class Solution:
    def maxAdjacentDistance(self, a: List[int]) -> int:
        return max(abs(x-y)for x,y in pairwise(2*a))

test('''
3423. Maximum Difference Between Adjacent Elements in a Circular Array
Easy
Topics
premium lock icon
Companies
Hint
Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.

 

Example 1:

Input: nums = [1,2,4]

Output: 3

Explanation:

Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.

Example 2:

Input: nums = [-5,-10,-5]

Output: 5

Explanation:

The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.


Other examples:

Input: nums = [2,1,0]
Output: 2

Constraints:

2 <= nums.length <= 100
-100 <= nums[i] <= 100
Seen this question in a real interview before?
1/5
Yes
No
Accepted
38,584/57.8K
Acceptance Rate
66.8%
Topics
Array
icon
Companies
Hint 1
Traverse from the second element to the last element and check the difference of every adjacent pair.
Hint 2
The edge case is to check the difference between the first and last elements.
''')
