from lc import *

# https://leetcode.com/problems/number-of-zigzag-arrays-i/solutions/7238638/recursion-approach-with-memoization3d-dp-3n8z/?envType=daily-question&envId=2026-06-23

# MLE
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        return(f:=cache(lambda i,d,p:not i or l<=p+d<=r and f(i-1,-d,p+d)+f(i,d,p+d)))(n,-1,r+1)*2%(10**9+7)

# POTD 2026-06-22

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m=10**9+7;h=lambda a:[*accumulate(a[:-1],lambda x,y:(x+y)%m)][::-1]+[0];return sum(reduce(lambda s,_:(h(s[1]),h(s[0])),range(n-1),([1]*(r-l+1),)*2)[0])*2%m

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        return sum(reduce(lambda d,_:[0,*accumulate(d[:0:-1])],range(n-1),[1]*(r-l+1)))*2%(10**9+7)

test('''
3699. Number of ZigZag Arrays I
Hard
Topics
premium lock icon
Companies
Hint
You are given three integers n, l, and r.

A ZigZag array of length n is defined as follows:

Each element lies in the range [l, r].
No two adjacent elements are equal.
No three consecutive elements form a strictly increasing or strictly decreasing sequence.
Return the total number of valid ZigZag arrays.

Since the answer may be large, return it modulo 109 + 7.

A sequence is said to be strictly increasing if each element is strictly greater than its previous one (if exists).

A sequence is said to be strictly decreasing if each element is strictly smaller than its previous one (if exists).

 

Example 1:

Input: n = 3, l = 4, r = 5

Output: 2

Explanation:

There are only 2 valid ZigZag arrays of length n = 3 using values in the range [4, 5]:

[4, 5, 4]
[5, 4, 5]​​​​​​​
Example 2:

Input: n = 3, l = 1, r = 3

Output: 10

Explanation:

There are 10 valid ZigZag arrays of length n = 3 using values in the range [1, 3]:

[1, 2, 1], [1, 3, 1], [1, 3, 2]
[2, 1, 2], [2, 1, 3], [2, 3, 1], [2, 3, 2]
[3, 1, 2], [3, 1, 3], [3, 2, 3]
All arrays meet the ZigZag conditions.

 

Constraints:

3 <= n <= 2000
1 <= l < r <= 2000
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
16,350/49.2K
Acceptance Rate
33.2%
Topics
Senior Staff
Dynamic Programming
Prefix Sum
Weekly Contest 469
icon
Companies
Hint 1
Use dynamic programming: let dp[i][dir][x] be the count of length-i sequences ending at value x where dir is the required next comparison (0 = down, 1 = up).
Hint 2
If the required move is up (dir=1) do dp[i+1][0][y] += sum(dp[i][1][x]) for x < y; if the required move is down (dir=0) do dp[i+1][1][y] += sum(dp[i][0][x]) for x > y.
Hint 3
Speed up with prefix/suffix sums so each layer updates in O(m) instead of O(m2); take values mod 109+7.
''')
