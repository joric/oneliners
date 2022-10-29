from lc import *

class Solution1:
    def reverse(self, x: int) -> int:
        neg =  False
        if x<0:
            neg = True
            x = -x
        value = int(str(x)[::-1])
        if value<2**31-1 or (value == 2**31 and neg):
            if neg:
                return - value
            else:
                return  value
        else:
            return 0

class Solution2:
    def reverse(self, x: int) -> int:
        s = (x > 0) - (x < 0)
        r = int(str(x*s)[::-1])
        return s*r * (r < 2**31)

class Solution3:
    def reverse(self, x: int) -> int:
        r = int(str(abs(x))[::-1])
        return (r<2**31)*(r,-r)[x<0]

class Solution4:
    def reverse(self, x: int) -> int:
        r,x,s = 0,abs(x),x<0
        while x:
            r = r*10 + x%10
            x //= 10
        return (r<2**31)*(r,-r)[s]

class Solution5:
    def reverse(self, x: int) -> int:
        return ((r:=(f:=lambda r,x:f(r*10+x%10,x//10) if x else r)(0,abs(x)))<2**31)*(r,-r)[x<0]

class Solution:
    def reverse(self, x: int) -> int:
        return ((r:=int(str(abs(x))[::-1]))<2**31)*(r,-r)[x<0]

test('''
7. Reverse Integer

Medium

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Constraints:

-2**31 <= x <= 2**31 - 1
''')
