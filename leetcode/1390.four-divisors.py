from lc import *

# https://leetcode.com/problems/four-divisors/solutions/1434020/python3-dynamic-programming-7-lines-by-r-7fwh/?envType=daily-question&envId=2026-01-04

class Solution:
    def sumFourDivisors(self, a: List[int]) -> int:
        n=max(a)+1;p,q=[1]*n,[1]*n;[setitem(p,j,p[j]+i)or setitem(q,j,q[j]+1)for i in range(2,n)for j in range(i,n,i)];return sum(p[x]*(q[x]==4)for x in a)

test('''
1390. Four Divisors
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
Example 2:

Input: nums = [21,21]
Output: 64
Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
 

Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
52,557/114K
Acceptance Rate
46.1%
Topics
Array
Math
Weekly Contest 181
icon
Companies
Hint 1
Find the divisors of each element in the array.
Hint 2
You only need to loop to the square root of a number to find its divisors.
''')
