from lc import *

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a 

class Solution:
    def fib(self, n: int) -> int:
        return reduce(lambda p,_:[p[1],sum(p)],[0]*n,[0,1])[0]

# matrix exponential

import numpy as np
class Solution:
    def fib(self, n: int) -> int:
        def f(m,p):
            if p==1:
                return m
            h = f(m,p//2)
            r = np.dot(h,h)
            return np.dot(r,m) if p&1 else r
        return n and np.dot(f(np.matrix([[0,1],[1,1]]),n),np.matrix([[0],[1]])).item((0,0)) or 0

class Solution:
    def fib(self, n: int) -> int:
        return (np:=__import__('numpy')) and n and np.dot((f:=lambda m,p:m if p==1 else (r:=np.dot(h:=f(m,p//2),h),1) and (np.dot(r,m) if p&1 else r))(np.matrix([[0,1],[1,1]]),n),np.matrix([[0],[1]])).item((0,0)) or 0

# https://leetcode.com/problems/fibonacci-number/discuss/3439417/MATH-solution

# classic Binet

class Solution:
    def fib(self, n: int) -> int:
        phi = (1 + sqrt(5)) / 2
        return round(pow(phi, n) / sqrt(5))

# same as climbing-stars but subtract 1 from n

class Solution:
    def fib(self, n: int) -> int:
        n-=1;r=5**.5;return round(((1+r)/2)**-~n/r)

class Solution:
    def fib(self, n: int) -> int:
        r=5**.5;return round(((1+r)/2)**n/r)

# generating function (see climbing-stars)

class Solution:
    def fib(self, n: int) -> int:
        x=1<<32;return x**~-n*x*x//(x*x+~x)%x

class Solution:
    def fib(self, n: int) -> int:
        x=9**n;return x**-~n//(x*x+~x)%x

class Solution:
    def fib(self, n: int) -> int:
        return pow(x:=2<<n,n+1,x*x+~x)%x

# also see climbing stairs solutions

test('''
509. Fibonacci Number
Easy

6049

304

Add to List

Share
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

Example 4:
Input: n = 0
Output: 0

Example 5:
Input: n = 1
Output: 1

Constraints:

0 <= n <= 30

''')
