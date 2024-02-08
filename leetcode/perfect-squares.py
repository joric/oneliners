from lc import *

# https://leetcode.com/problems/perfect-squares/discuss/71512/Static-DP-C%2B%2B-12-ms-Python-172-ms-Ruby-384-ms

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0]
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

# https://leetcode.com/problems/perfect-squares/discuss/558231/Python-one-liner-brute-force

class Solution:
    def numSquares(self, n):
        return next(r for r in range(1,n+1)for c in combinations_with_replacement([x**2 for x in range(1,n+1)if x**2<=n],r) if sum(c)==n)

# bottom-up
class Solution:
    def numSquares(self, n: int) -> int:
        d=[0]+[n]*n;any(n<(q:=i*i)or any(setitem(d,j,min(d[j],n if j<q else 1+d[j-q]))for j in range(n+1))for i in range(n));return d[-1]

# https://leetcode.com/problems/perfect-squares/discuss/3844078/Python-one-liner-Top-Down-DP

class Solution:
    @cache
    def numSquares(s, n: int) -> int:
        return n and min(s.numSquares(n-i*i)for i in range(1,isqrt(n)+1))+1

class Solution:
    def numSquares(self, n: int) -> int:
        return(f:=cache(lambda n:n and min(f(n-i*i)for i in range(1,isqrt(n)+1))+1))(n)

test('''
279. Perfect Squares
Medium

10560

432

Add to List

Share
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Example 3:

Input: n = 4
Output: 1

Constraints:

1 <= n <= 10^4
Accepted
751,510
Submissions
1,402,378
''')
