from lc import *

# https://leetcode.com/problems/smallest-number-with-all-set-bits/solutions/6098984/python-1-line/

class Solution:
    def smallestNumber(self, n: int) -> int:
        return int('1'*len(bin(n)[2:]),2)

class Solution:
    def smallestNumber(self, n: int) -> int:
        return~-2**(len(bin(n)[2:]))

class Solution:
    def smallestNumber(self, n: int) -> int:
        return~-2**n.bit_length()

test('''
3370. Smallest Number With All Set Bits
Easy
Topics
premium lock icon
Companies
Hint
You are given a positive number n.

Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits

 

Example 1:

Input: n = 5

Output: 7

Explanation:

The binary representation of 7 is "111".

Example 2:

Input: n = 10

Output: 15

Explanation:

The binary representation of 15 is "1111".

Example 3:

Input: n = 3

Output: 3

Explanation:

The binary representation of 3 is "11".

 

Constraints:

1 <= n <= 1000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
43,744/57.4K
Acceptance Rate
76.2%
Topics
Math
Bit Manipulation
Weekly Contest 426
icon
Companies
Hint 1
Find the strictly greater power of 2, and subtract 1 from it.
Similar Questions
Minimum Number of K Consecutive Bit Flips
Hard
Minimum Bit Flips to Convert Number
Easy
Find Sum of Array Product of Magical Sequences
Hard
''')
