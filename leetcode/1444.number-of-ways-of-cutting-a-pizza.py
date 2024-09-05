from lc import *

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m,n = len(pizza),len(pizza[0])
        s = [[int(c!='.') for c in r] for r in pizza]
        a=lambda i,j: s[i][j] if 0<=i<m and 0<=j<n else 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                s[i][j] += (a(i+1,j) + a(i,j+1) - a(i+1,j+1))
        @cache
        def f(i,j,c):
            if c==0:
                return int(a(i, j)>0)
            r = 0
            for h in range(i+1, m):
                if a(i,j)-a(h,j)>0:
                    r += f(h,j,c-1)
            for v in range(j+1, n):
                if a(i,j)-a(i,v)>0:
                    r += f(i,v,c-1)
            return r
        return f(0,0,k-1)%(10**9+7)

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        return (m:=len(pizza),n:=len(pizza[0]),s:=[[int(c!='.') for c in r] for r in pizza],a:=lambda i,j:0<=i<m and 0<=j<n and s[i][j], any(setitem(s[i],j,s[i][j]+(a(i+1,j)+a(i,j+1)-a(i+1,j+1))) for i in range(m)[::-1] for j in range(n)[::-1]), (f:=cache(lambda i,j,c:sum(a(i,j)-a(h,j)>0 and f(h,j,c-1) for h in range(i+1,m))+sum(a(i,j)-a(i,v)>0 and f(i,v,c-1) for v in range(j+1,n)) if c else int(a(i,j)>0)))(0,0,k-1)%(10**9+7))[-1]

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        m,n = len(pizza),len(pizza[0])
        s = [[0]*(n+1) for _ in range(m+1)]
        any(setitem(s[r],c,s[r][c]+s[r][c+1]+s[r+1][c]-s[r+1][c+1]+(pizza[r][c]=='A')) for r in range(m)[::-1] for c in range(n)[::-1])
        f = cache(lambda t,r,c:0 if s[r][c]==0 else 1 if t==0 else sum(s[r][c]-s[i][c]>0 and f(t-1,i,c) for i in range(r+1,m))+sum(s[r][c]-s[r][j]>0 and f(t-1,r,j) for j in range(c+1,n)))
        return f(k-1,0,0)%(10**9+7)

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        return (m:=len(pizza),n:=len(pizza[0]),s:=[[0]*(n+1) for _ in range(m+1)],any(setitem(s[r],c,s[r][c]+s[r][c+1]+s[r+1][c]-s[r+1][c+1]+(pizza[r][c]=='A')) for r in range(m)[::-1] for c in range(n)[::-1]),(f:=cache(lambda t,r,c:0 if s[r][c]==0 else 1 if t==0 else sum(s[r][c]-s[i][c]>0 and f(t-1,i,c) for i in range(r+1,m))+sum(s[r][c]-s[r][j]>0 and f(t-1,r,j) for j in range(c+1,n))))(k-1,0,0)%(10**9+7))[-1]


test('''

1444. Number of Ways of Cutting a Pizza
Hard

749

43

Add to List

Share
Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:



Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1
 

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
Accepted
26,858
Submissions
47,328
Seen this question in a real interview before?

Yes

No
Selling Pieces of Wood
Hard
Note that after each cut the remaining piece of pizza always has the lower right coordinate at (rows-1,cols-1).
Use dynamic programming approach with states (row1, col1, c) which computes the number of ways of cutting the pizza using "c" cuts where the current piece of pizza has upper left coordinate at (row1,col1) and lower right coordinate at (rows-1,cols-1).
For the transitions try all vertical and horizontal cuts such that the piece of pizza you have to give a person must contain at least one apple. The base case is when c=k-1.
Additionally use a 2D dynamic programming to respond in O(1) if a piece of pizza contains at least one apple.

''')
