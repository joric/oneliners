from lc import *

# https://leetcode.com/problems/power-of-four/discuss/164458/Python-recursive-iterative-math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        elif n==0:
            return False
        while n!=1:
            if n%4 != 0:
                return False
            else:
                n = n/4
        return True

# https://leetcode.com/problems/power-of-four/discuss/384752/Shortest-than-shortest

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n==0:
            return False
        return n%4==0 and self.isPowerOfFour(n/4)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n==1 or n!=0 and n%4==0 and self.isPowerOfFour(n/4)

# https://leetcode.com/problems/power-of-four/discuss/772269/Python-O(1)-oneliner-solution-explained
# Number is positive AND Number is power of 2 AND This power of 2 is even power

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n&(n-1)==0 and 0b1010101010101010101010101010101&n==n

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0==n&(n-1)==n&int.from_bytes(b'\xaa\xaa\xaa\xaa','little')

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n&(n-1)==0 and 1431655765&n==n

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n&(n-1)==0 and 0xAAAAAAAA&n==0

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n and n&(n-1)==0 and 0x55555555&n==n

# https://leetcode.com/problems/power-of-four/discuss/772524/Shortest-one-liner-in-Python-20ms-(beats-99.28-of-python3-submissions)

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and log(n,4).is_integer()

# https://leetcode.com/problems/power-of-four/discuss/80460/1-line-C%2B%2B-solution-without-confusing-bit-manipulations

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and n&(n-1)==0 and (n-1)%3==0

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        t=n-1;return n>0 and n&t==0 and t%3==0

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        t=n-1;return n>0==n&t==t%3

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0==n&(n-1)==n%3-1

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0==log(n,4)%1

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

Other examples:

Input: n = 2
Output: false

Constraints:

-2^31 <= n <= 2^31 - 1
 

Follow up: Could you solve it without loops/recursion?
''')