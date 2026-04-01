from lc import *

# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/solutions/6320591/python-dfs-cache-by-pbelskiy-t1ok/?envType=daily-question&envId=2026-04-02

class Solution: # MLE
    def maximumAmount(s,c:List[List[int]])->int:
        h,w=len(c),len(c[0]);f=cache(lambda y,x,r:(y<h-1 or x<w-1)and max(v for i,j in((y+1,x),(y,x+1))if i<h and j<w for v in(f(i,j,r)+c[i][j],f(i,j,r-1))[:1+(r>0)])or 0);return max(f(0,0,1),f(0,0,2)+c[0][0])

# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/solutions/6285321/python3-13-lines-top-down-dp-w-example-9-5byc/?envType=daily-question&envId=2026-04-02

class Solution:
    def maximumAmount(self,c:List[List[int]])->int:
        m,n=len(c),len(c[0])
        r=range
        d=lambda v,x:(max(v+x[0],x[1]),max(v+x[1],x[2]),v+x[2])
        c[0][0]=(0,0,c[0][0])
        for j in r(1,n):
            c[0][j]=d(c[0][j],c[0][j-1])
        for i in r(1,m):
            c[i][0]=d(c[i][0],c[i-1][0])
            for j in r(1,n):
                a,b,e=c[i-1][j]
                f,g,h=c[i][j-1]
                k=(max(a,f),max(b,g),max(e,h))
                c[i][j]=d(c[i][j],k)
        return max(c[-1][-1])

class Solution:
    def maximumAmount(self,c:List[List[int]])->int:
        m,n=len(c),len(c[0]);s,r=setitem,range;c[0][0]=(0,0,c[0][0]);[s(c[0],j,(max(c[0][j]+c[0][j-1][0],c[0][j-1][1]),max(c[0][j]+c[0][j-1][1],c[0][j-1][2]),c[0][j]+c[0][j-1][2]))for j in r(1,n)];[s(c[i],0,(max(c[i][0]+c[i-1][0][0],c[i-1][0][1]),max(c[i][0]+c[i-1][0][1],c[i-1][0][2]),c[i][0]+c[i-1][0][2]))for i in r(1,m)];[[s(c[i],j,(max(c[i][j]+(k:=(max(c[i-1][j][0],c[i][j-1][0]),max(c[i-1][j][1],c[i][j-1][1]),max(c[i-1][j][2],c[i][j-1][2])))[0],k[1]),max(c[i][j]+k[1],k[2]),c[i][j]+k[2]))for j in r(1,n)]for i in r(1,m)];return max(c[-1][-1])

# POTD 2026-04-02

class Solution:
    def maximumAmount(self, c: List[List[int]]) -> int:
        d = [[-inf] * 3 for _ in range(len(c[0]) + 1)]
        for i, row in enumerate(c):
            for j, v in enumerate(row):
                if i == j == 0:
                    d[j+1] = [v, max(v, 0), max(v, 0)]
                else:
                    p0, p1, p2 = [max(a, b) for a, b in zip(d[j], d[j+1])]
                    d[j+1] = [p0 + v, max(p1 + v, p0), max(p2 + v, p1)]
        return d[-1][2]

class Solution:
    def maximumAmount(self,c:List[List[int]])->int:
        m=max;e=enumerate;d=[[-inf]*3]*(len(c[0])+1);[setitem(d,j+1,i==j==0 and[v,m(v,0),m(v,0)]or[(p:=[*map(m,d[j],d[j+1])])[0]+v,m(p[1]+v,p[0]),m(p[2]+v,p[1])])for i,r in e(c)for j,v in e(r)];return d[-1][2]

test('''
3418. Maximum Amount of Money Robot Can Earn
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n grid. A robot starts at the top-left corner of the grid (0, 0) and wants to reach the bottom-right corner (m - 1, n - 1). The robot can move either right or down at any point in time.

The grid contains a value coins[i][j] in each cell:

If coins[i][j] >= 0, the robot gains that many coins.
If coins[i][j] < 0, the robot encounters a robber, and the robber steals the absolute value of coins[i][j] coins.
The robot has a special ability to neutralize robbers in at most 2 cells on its path, preventing them from stealing coins in those cells.

Note: The robot's total coins can be negative.

Return the maximum profit the robot can gain on the route.

 

Example 1:

Input: coins = [[0,1,-1],[1,-2,3],[2,-3,4]]

Output: 8

Explanation:

An optimal path for maximum coins is:

Start at (0, 0) with 0 coins (total coins = 0).
Move to (0, 1), gaining 1 coin (total coins = 0 + 1 = 1).
Move to (1, 1), where there's a robber stealing 2 coins. The robot uses one neutralization here, avoiding the robbery (total coins = 1).
Move to (1, 2), gaining 3 coins (total coins = 1 + 3 = 4).
Move to (2, 2), gaining 4 coins (total coins = 4 + 4 = 8).
Example 2:

Input: coins = [[10,10,10],[10,10,10]]

Output: 40

Explanation:

An optimal path for maximum coins is:

Start at (0, 0) with 10 coins (total coins = 10).
Move to (0, 1), gaining 10 coins (total coins = 10 + 10 = 20).
Move to (0, 2), gaining another 10 coins (total coins = 20 + 10 = 30).
Move to (1, 2), gaining the final 10 coins (total coins = 30 + 10 = 40).
 

Constraints:

m == coins.length
n == coins[i].length
1 <= m, n <= 500
-1000 <= coins[i][j] <= 1000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
23,729/80K
Acceptance Rate
29.7%
Topics
Staff
Array
Dynamic Programming
Matrix
Weekly Contest 432
icon
Companies
Hint 1
Use Dynamic Programming.
Hint 2
Let dp[i][j][k] denote the maximum amount of money a robot can earn by starting at cell (i,j) and having neutralized k robbers.
''')
