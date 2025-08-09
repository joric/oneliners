from lc import *

# https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and not(n&n-1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return(n>0)*(n&~-n<1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return(n-1&n==0)*n>0

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return(n&~-n<1)*n>0

# POTD 2025-08-09

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return-n&n==n>0

test('''
231. Power of Two
Easy

6256

401

Add to List

Share
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

More examples:

Input: n = 0
Output: false

Constraints:

-2^31 <= n <= 2^31 - 1
''')
