from lc import *

# https://leetcode.com/problems/binary-number-with-alternating-bits/solutions/108427/oneliners-c-java-ruby-python-by-stefanpo-2blp/?envType=daily-question&envId=2026-02-18

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n^=n//4;return n&n-1<1

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n^=n//2;return n&n+1<1

test('''
693. Binary Number with Alternating Bits
Solved
Easy
Topics
premium lock icon
Companies
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

 

Example 1:

Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
Example 2:

Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
Example 3:

Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
 

Constraints:

1 <= n <= 231 - 1
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
173,288/270.5K
Acceptance Rate
64.1%
Topics
Mid Level
Bit Manipulation
icon
Companies
Similar Questions
Number of 1 Bits
Easy
''')

