from lc import *

# https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return 1 if not n else 1/self.myPow(x,-n) if n<0 else x*self.myPow(x,n-1) if n%2 else self.myPow(x*x,n/2)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

class Solution:myPow=pow

test('''
50. Pow(x, n)
Medium

7967

7983

Add to List

Share
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
n is an integer.
Either x is not zero or n > 0.
-10^4 <= xn <= 10^4
''')
