from lc import *

# https://leetcode.com/problems/largest-magic-square/solutions/5886441/a-kinda-concise-and-clear-python-solutio-lknz/?envType=daily-question&envId=2026-01-18

class Solution:
    def largestMagicSquare(self,g:List[List[int]])->int:
        r=[list(accumulate(x,initial=0))for x in g]
        c=[list(accumulate(x,initial=0))for x in zip(*g)]
        m,n=len(g),len(g[0])
        for s in range(min(m,n),0,-1):
            for i in range(m-s+1):
                for j in range(n-s+1):
                    t=r[i][j+s]-r[i][j]
                    if(all(r[k][j+s]-r[k][j]==t for k in range(i+1,i+s))
                    and all(c[k][i+s]-c[k][i]==t for k in range(j,j+s))
                    and sum(g[i+k][j+k]for k in range(s))==t
                    and sum(g[i+k][j+s-1-k]for k in range(s))==t):
                        return s

class Solution:
    def largestMagicSquare(self,g:List[List[int]])->int:
        m,n=len(g),len(g[0]);r,c=[[[*accumulate([0,*x])]for x in t]for t in(g,zip(*g))];return next(s for s in range(min(m,n),0,-1)for i in range(m-s+1)for j in range(n-s+1)if(t:=r[i][j+s]-r[i][j])and all(t==r[k][j+s]-r[k][j]for k in range(i+1,i+s))and all(t==c[k][i+s]-c[k][i]for k in range(j,j+s))and sum(g[i+k][j+k]for k in range(s))==sum(g[i+k][j+s-1-k]for k in range(s))==t)

test('''
1895. Largest Magic Square
Medium
Topics
premium lock icon
Companies
Hint
A k x k magic square is a k x k grid filled with integers such that every row sum, every column sum, and both diagonal sums are all equal. The integers in the magic square do not have to be distinct. Every 1 x 1 grid is trivially a magic square.

Given an m x n integer grid, return the size (i.e., the side length k) of the largest magic square that can be found within this grid.

 

Example 1:


Input: grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
Output: 3
Explanation: The largest magic square has a size of 3.
Every row sum, column sum, and diagonal sum of this magic square is equal to 12.
- Row sums: 5+1+6 = 5+4+3 = 2+7+3 = 12
- Column sums: 5+5+2 = 1+4+7 = 6+3+3 = 12
- Diagonal sums: 5+4+3 = 6+4+2 = 12
Example 2:


Input: grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
Output: 2
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 106
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
28,614/44.4K
Acceptance Rate
64.5%
Topics
Array
Matrix
Prefix Sum
Biweekly Contest 54
icon
Companies
Hint 1
Check all squares in the matrix and find the largest one.
Similar Questions
Magic Squares In Grid
Medium
''')
