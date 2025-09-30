from lc import *

# https://leetcode.com/problems/find-triangular-sum-of-an-array/?envType=daily-question&envId=2025-09-30

class Solution:
    def triangularSum(self, a: List[int]) -> int:
        return sum(comb(len(a)-1,i)*a[i]for i in range(len(a)))%10

test('''
2221. Find Triangular Sum of an Array
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.

 

Example 1:


Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.
Example 2:

Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 9
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
109,492/138.7K
Acceptance Rate
78.9%
Topics
Array
Math
Simulation
Combinatorics
Biweekly Contest 75
icon
Companies
Hint 1
Try simulating the entire process.
Hint 2
To reduce space, use a temporary array to update nums in every step instead of creating a new array at each step.
Similar Questions
Pascal's Triangle II
Easy
Calculate Digit Sum of a String
Easy
Min Max Game
Easy
''')
