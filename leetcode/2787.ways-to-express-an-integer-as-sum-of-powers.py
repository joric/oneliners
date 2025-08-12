from lc import *

# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/?envType=daily-question&envId=2025-08-12

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        def f(r,v):
            if r == 0:
                return 1
            i, s = v, 0
            while True:
                t = r - i**x
                if t < 0:
                    break
                i += 1
                s += f(t,i)
            return s
        return f(n,1)%(10**9+7)

# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/solutions/7051628/two-simple-lines-of-code/?envType=daily-question&envId=2025-08-12

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        p = [q**x for q in range(1,round(n**(1/x))+1)]
        @cache
        def f(i,n):
            if i<len(p) and n>=p[i]:
                return (f(i+1,n)+f(i+1,n-p[i]))%(10**9+7)
            return int(n==0)
        return f(0,n)

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        return ~~(f:=cache(lambda i,n,p=[q**x for q in range(1,round(n**(1/x))+1)]:
            i<len(p) and n>=p[i] and (f(i+1,n)+f(i+1,n-p[i]))%(10**9+7) or n==0))(0,n)

# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/solutions/3847607/easy-recursion-memoization/?envType=daily-question&envId=2025-08-12

class Solution: # MLE
    def numberOfWays(self, n: int, x: int) -> int:
        return(f:=cache(lambda n,i:n==0 or i<=n>0 and f(n-i**x,i+1)+f(n,i+1)))(n,1)%(10**9+7)

class Solution: # MLE
    def numberOfWays(self, n: int, x: int) -> int:
        return(f:=cache(lambda n,i:n>=i and f(n-i**x,i+1)+f(n,i+1)or n==0))(n,1)%(10**9+7)

# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/solutions/3802157/python-medium/?envType=daily-question&envId=2025-08-12

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        @cache
        def calc(curVal, cur_integer):
            r = curVal - cur_integer ** x
            if not r:
                return 1
            if r < 0:
                return 0
            return calc(r, cur_integer + 1) + calc(curVal, cur_integer + 1)
        return calc(n, 1) % MOD

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        return(f:=cache(lambda n,i:0<(r:=n-i**x)and f(r,i+1)+f(n,i+1)or r==0))(n,1)%(10**9+7)

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        return(f:=cache(lambda n,i:n>=i**x and f(n-i**x,i+1)+f(n,i+1)or n<1))(n,1)%(10**9+7)

test('''
2787. Ways to Express an Integer as Sum of Powers
Medium
Topics
premium lock icon
Companies
Hint
Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

 

Example 1:

Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
Example 2:

Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.
 

Constraints:

1 <= n <= 300
1 <= x <= 5
Seen this question in a real interview before?
1/5
Yes
No
Accepted
35,451/89.1K
Acceptance Rate
39.8%
Topics
Dynamic Programming
Biweekly Contest 109
icon
Companies
Hint 1
You can use dynamic programming, where dp[k][j] represents the number of ways to express k as the sum of the x-th power of unique positive integers such that the biggest possible number we use is j.
Hint 2
To calculate dp[k][j], you can iterate over the numbers smaller than j and try to use each one as a power of x to make our sum k.
Similar Questions
Perfect Squares
Medium
Combination Sum IV
Medium
Target Sum
Medium
''')
