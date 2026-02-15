from lc import *

# https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        r = ''
        a = list(a)
        b = list(b)
        while a or b or c:
            if a:
                c += int(a.pop())
            if b:
                c += int(b.pop())
            r += str(c%2)
            c //= 2
        return r[::-1]

# POTD 2026-02-15

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f'{int(a,2)+int(b,2):b}'

test('''
67. Add Binary
Easy

6847

707

Add to List

Share
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
''')
