from lc import *

# https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1+n%2
        for _ in range(n//2):
            a += b
            b += a
        return a

# recursion

class Solution:
    def climbStairs(self, n: int, a=1, b=1) -> int:
        return self.climbStairs(n-1, b, a+b) if n>1 else b

class Solution:
    def climbStairs(self, n: int) -> int:
        return (f:=lambda n,a,b:n>1 and f(n-1,b,a+b) or b)(n,1,1)

# reduce

class Solution:
    def climbStairs(self, n: int) -> int:
        return reduce(lambda x,_:(x[1],sum(x)),range(n),(1,1))[0]

# numpy

class Solution:
    def climbStairs(self, n: int) -> int:
        return(__import__('numpy').matrix('1 1;1 0')**n).item(0)

# numpy with bigint

class Solution:
    def climbStairs(self, n: int) -> int:
        return(__import__('numpy').matrix('1 1;1 0','object')**n).item(0)

# inline loop

class Solution:
    def climbStairs(self, n: int) -> int:
        p=(1,1);[(p:=(p[1],sum(p)))for _ in[0]*n];return p[0]

class Solution:
    def climbStairs(self, n: int) -> int:
        a=b=1;[(t:=a,a:=b,b:=a+t)for _ in[0]*n];return a

class Solution:
    def climbStairs(self, n: int) -> int:
        a=b=1;[b:=a+(a:=b)for _ in' '*n];return a

# combinations https://leetcode.com/problems/climbing-stairs/solutions/3412081/one-line-solution/

class Solution:
    def climbStairs(self, n: int) -> int:
        return sum(comb(n-d,d)for d in range(n//2+1))

# https://r-knott.surrey.ac.uk/Fibonacci/fibFormula.html

# works up to n = 69 => 190392490709135
# breaks at n = 70 => 308061521170129

class Solution:
    def climbStairs(self, n: int) -> int:
        r=5**.5;return round(((1+r)/2)**-~n/r)

# https://en.wikipedia.org/wiki/Generating_function

class Solution:
    def climbStairs(self, n):
        x=1<<32;return x**n*x*x//(x*x+~x)%x

class Solution:
    def climbStairs(self, n):
        x=9**n;return x**-~-~n//(x*x+~x)%x

class Solution:
    def climbStairs(self, n):
        return pow(x:=2<<n,n+2,x*x+~x)%x

# also see fibonacci-number solutions

test('''

70. Climbing Stairs
Easy
15.9K
479
Companies
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Example 3:

Input: n = 45
Output: 1836311903

Example 4:

#Input: n = 69
#Output: 190392490709135

Example 5:

#Input: n = 70
#Output: 308061521170129
Fibonacci float precision breaks here, unfortunately

Constraints:

1 <= n <= 45
''')