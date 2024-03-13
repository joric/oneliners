from lc import *

# humanoid version

class Solution:
    def pivotInteger(self, n: int) -> int:
        # (x * (x + 1)) / 2 = n * (n + 1) / 2 - (x - 1) * x / 2
        # x^2 / 2 + x / 2 = (n^2 + n)/2 - x^2 / 2 + x / 2
        # x^2 = n ^ 2 + n / 2
        x = sqrt(n ** 2 / 2 + n / 2)
        if x != int(x):
            return -1
        return int(x)

class Solution:
    def pivotInteger(self, n: int) -> int:
        return next((x for x in range(1,n+1)if 2*x*x==n*n+n),-1)

# precalc

class Solution:
    def pivotInteger(self, n: int) -> int:
        return{1:1,8:6,49:35,288:204}.get(n,-1)

# https://leetcode.com/problems/find-the-pivot-integer/discuss/3874194/Easy-solution-1-line

class Solution:
    def pivotInteger(self, n: int) -> int:
        return x if (x:=int(sqrt(s:=n*(n+1)/2)))*x==s else -1

class Solution:
    def pivotInteger(self, n: int) -> int:
        return(x:=isqrt(s:=n*-~n//2),-1)[x*x<s]

test('''
2485. Find the Pivot Integer
Easy

623

11

Add to List

Share
Given a positive integer n, find the pivot integer x such that:

The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

 

Example 1:

Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.
Example 3:

Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.
 

Constraints:

1 <= n <= 1000
Accepted
59,285
Submissions
74,084
''')
