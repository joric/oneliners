from lc import *

# https://leetcode.com/problems/power-of-four/discuss/772269/Python-O(1)-oneliner-solution-explained

# Number is positive AND Number is power of 2 AND This power of 2 is even power

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n&(n-1)==0 and 0b1010101010101010101010101010101&n==n

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n&(n-1)==0 and 0x55555555&n==n

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n&(n-1)==0 and 1431655765&n==n

# https://leetcode.com/problems/power-of-four/discuss/80460/1-line-C%2B%2B-solution-without-confusing-bit-manipulations

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n&(n-1)==0 and (n-1)%3==0

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        t=n-1;return n>0and n&t==0and t%3==0

test('''
342. Power of Four
Easy

3362

353

Add to List

Share
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-2^31 <= n <= 2^31 - 1
 

Follow up: Could you solve it without loops/recursion?
''')

