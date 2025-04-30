from lc import *

# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/solutions/6700493/most-easy-just-one-line-code-in-python/?envType=daily-question&envId=2025-04-30

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for i in nums if len(str(i))&1==0)

class Solution:
    def findNumbers(self, a: List[int]) -> int:
        return sum(1>1&len(str(x))for x in a)

# Kerninghan

class Solution:
    def findNumbers(self, a: List[int]) -> int:
        return sum(1&~len(str(x))for x in a)

test('''
1295. Find Numbers with Even Number of Digits
Solved
Easy
Topics
Companies
Hint
Given an array nums of integers, return how many of them contain an even number of digits.

 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 

Constraints:

1 <= nums.length <= 500
1 <= nums[i] <= 105
Seen this question in a real interview before?
1/5
Yes
No
Accepted
808.3K
Submissions
1M
Acceptance Rate
78.1%
Topics
Array
Math
Companies
Hint 1
How to compute the number of digits of a number ?
Hint 2
Divide the number by 10 again and again to get the number of digits.
Similar Questions
Finding 3-Digit Even Numbers
Easy
Number of Even and Odd Bits
Easy
Find if Digit Game Can Be Won
Easy
''')
