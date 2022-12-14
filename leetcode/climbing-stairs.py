from lc import *

class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for _ in range(n):
            a, b = b, a + b
        return a

class Solution:
    def climbStairs(self, n: int, a=1, b=1) -> int:
        return self.climbStairs(n-1, b, a+b) if n>1 else b

class Solution:
    def climbStairs(self, n: int) -> int:
        return (f:=lambda n,a,b:n>1 and f(n-1,b,a+b) or b)(n,1,1)

class Solution:
    def climbStairs(self, n: int) -> int:
        return reduce(lambda x,_:(x[1],sum(x)),range(n),(1,1))[0]

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
 

Constraints:

1 <= n <= 45
''')
