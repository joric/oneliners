from lc import *

# https://leetcode.com/problems/path-with-maximum-gold/discuss/802925/Python-in-8-lines-simple

class Solution:
    def getMaximumGold(self, g: List[List[int]]) -> int:
        h,w = len(g),len(g[0])
        def f(i,j):
            if h>i>-1<j<w and g[i][j]:
                x = g[i][j]
                g[i][j] = 0
                c = max(map(f,(i+1,i-1,i,i),(j,j,j+1,j-1)))
                g[i][j] = x
                return c+x
            return 0
        return max(f(i,j)for i in range(h)for j in range(w))

class Solution:
    def getMaximumGold(self, g: List[List[int]]) -> int:
        h,w,s=len(g),len(g[0]),setitem;f=lambda i,j:h>i>-1<j<w and g[i][j]and(x:=g[i][j],s(g[i],j,0),c:=max(map(f,(i+1,i-1,i,i),(j,j,j+1,j-1))),s(g[i],j,x),c+x)[4]or 0;return max(f(i,j)for i in range(h)for j in range(w))

class Solution:
    def getMaximumGold(self, g: List[List[int]]) -> int:
        e,s=enumerate,setitem;g={i+j*1j:x for i,r in e(g)for j,x in e(r)};return max(map(f:=lambda z:(t:=g.get(z,0))and(s(g,z,0),c:=max(f(z+1j**k)for k in range(4)),s(g,z,t))and c+t,set(g)))

test('''
1219. Path with Maximum Gold
Medium

2681

68

Add to List

Share
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
Accepted
114,815
Submissions
180,581
''')