from lc import *

# https://leetcode.com/problems/maximum-difference-between-increasing-elements/solutions/1490061/python-3-three-ways-one-line/

class Solution:
    def maximumDifference(self, a: List[int]) -> int:
        return max(-min(starmap(sub,combinations(a,2))),0)or-1

# https://leetcode.com/problems/maximum-difference-between-increasing-elements/solutions/1489195/1-line-python/?envType=daily-question&envId=2025-06-16

class Solution:
    def maximumDifference(self, a: List[int]) -> int:
        return max(x-y for x,y in zip(a,accumulate(a,min)))or-1

class Solution:
    def maximumDifference(self, a: List[int]) -> int:
        t=inf;return max(x-(t:=min(t,x))for x in a)or-1

test('''
2016. Maximum Difference Between Increasing Elements
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.

 

Example 1:

Input: nums = [7,1,5,4]
Output: 4
Explanation:
The maximum difference occurs with i = 1 and j = 2, nums[j] - nums[i] = 5 - 1 = 4.
Note that with i = 1 and j = 0, the difference nums[j] - nums[i] = 7 - 1 = 6, but i > j, so it is not valid.
Example 2:

Input: nums = [9,4,3,2]
Output: -1
Explanation:
There is no i and j such that i < j and nums[i] < nums[j].
Example 3:

Input: nums = [1,5,2,10]
Output: 9
Explanation:
The maximum difference occurs with i = 0 and j = 3, nums[j] - nums[i] = 10 - 1 = 9.
 

Constraints:

n == nums.length
2 <= n <= 1000
1 <= nums[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
118,328/199.6K
Acceptance Rate
59.3%
Topics
Array
icon
Companies
Hint 1
Could you keep track of the minimum element visited while traversing?
Hint 2
We have a potential candidate for the answer if the prefix min is lesser than nums[i].
Similar Questions
Best Time to Buy and Sell Stock
Easy
Two Furthest Houses With Different Colors
Easy
''')
