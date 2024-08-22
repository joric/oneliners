from lc import *

# https://leetcode.com/problems/number-complement/discuss/3896397/Python.-One-line-solution.

class Solution:
    def findComplement(self, n: int) -> int:
        return~n+2**len(f'{n:b}')

test('''
476. Number Complement
Easy

2677

124

Add to List

Share
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Constraints:

1 <= num < 231
 

Note: This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/

Accepted
342,474
Submissions
505,794
''')

