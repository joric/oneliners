from lc import *

# https://leetcode.com/problems/bitwise-and-of-numbers-range

class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        return-2**(l^r).bit_length()&l

class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        return-1<<(l^r).bit_length()&l

test('''
201. Bitwise AND of Numbers Range
Medium

3237

234

Add to List

Share
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

 

Example 1:

Input: left = 5, right = 7
Output: 4
Example 2:

Input: left = 0, right = 0
Output: 0
Example 3:

Input: left = 1, right = 2147483647
Output: 0
 

Constraints:

0 <= left <= right <= 231 - 1
Accepted
276,154
Submissions
638,174
''')
