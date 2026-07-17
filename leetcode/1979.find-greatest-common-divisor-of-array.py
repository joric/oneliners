from lc import *

# https://leetcode.com/problems/find-greatest-common-divisor-of-array/solutions/2716003/one-line-python-by-maary-yafd/?envType=daily-question&envId=2026-07-18

class Solution:
    def findGCD(self, a: List[int]) -> int:
        return gcd(min(a),max(a))

test('''
1979. Find Greatest Common Divisor of Array
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 

Example 1:

Input: nums = [2,5,6,9,10]
Output: 2
Explanation:
The smallest number in nums is 2.
The largest number in nums is 10.
The greatest common divisor of 2 and 10 is 2.
Example 2:

Input: nums = [7,5,6,8,3]
Output: 1
Explanation:
The smallest number in nums is 3.
The largest number in nums is 8.
The greatest common divisor of 3 and 8 is 1.
Example 3:

Input: nums = [3,3]
Output: 3
Explanation:
The smallest number in nums is 3.
The largest number in nums is 3.
The greatest common divisor of 3 and 3 is 3.
 

Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 1000
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
264,923/330.2K
Acceptance Rate
80.2%
Topics
Mid Level
Array
Math
Number Theory
Weekly Contest 255
icon
Companies
Hint 1
Find the minimum and maximum in one iteration. Let them be mn and mx.
Hint 2
Try all the numbers in the range [1, mn] and check the largest number which divides both of them.
Similar Questions
Greatest Common Divisor of Strings
Easy
Number of Different Subsequences GCDs
Hard
Three Divisors
Easy
Smallest Even Multiple
Easy
Number of Subarrays With GCD Equal to K
Medium
Find the Number of Subsequences With Equal GCD
Hard
Maximum Subarray With Equal Products
Easy
''')
