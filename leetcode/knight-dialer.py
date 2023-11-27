from lc import *

# https://leetcode.com/problems/knight-dialer/discuss/1334052/Why-I-love-Python%3A-O(N)-in-5-lines

class Solution:
    def knightDialer(self, n: int) -> int:
        moves={1:(6,8),2:(7,9),3:(4,8),4:(0,3,9),5:tuple(),6:(1,7,0),7:(2,6),8:(1,3),9:(2,4),0:(4,6)}
        dp=[1]*10
        for _ in range(n-1):
            dp=[sum(dp[c] for c in moves[i]) for i in range(10)]
        return sum(dp)%1000000007

# https://leetcode.com/problems/knight-dialer/discuss/764265/Python3-6-line-116ms-solution-using-maths

class Solution:
    def knightDialer(self, n: int) -> int:
        if n<= 1:
            return 10
        a,b,c,d=2,4,2,1
        for _ in range(n-1):
            a,b,c,d=(b,2*(a+c),(b+2*d),c)
        return (a+b+c+d)%(10**9+7)

class Solution:
    def knightDialer(self, n: int) -> int:
        return(n<2)+sum(reduce(lambda x,_:(lambda a,b,c,d:(b,2*(a+c),b+2*d,c))(*x),range(n-1),[2,4,2,1]))%(10**9+7)

class Solution:
    def knightDialer(self, n: int) -> int:
        return(n<2)+sum(reduce(lambda p,_:(p[1],2*(p[0]+p[2]),p[1]+2*p[3],p[2]),[0]*(n-1),[2,4,2,1]))%(10**9+7)

test('''
935. Knight Dialer
Medium

2156

394

Add to List

Share
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:


We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


Given an integer n, return how many distinct phone numbers of length n we can dial.

You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

 

Example 1:

Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.
Example 2:

Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
Example 3:

Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.
 

Constraints:

1 <= n <= 5000
''')

