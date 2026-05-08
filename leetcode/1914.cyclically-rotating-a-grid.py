from lc import *

# https://leetcode.com/problems/cyclically-rotating-a-grid/solutions/2211724/python3-on-space-level-by-level-pair-un-8hp3g/?envType=daily-question&envId=2026-05-09

class Solution:
    def rotateGrid(self,g: List[List[int]],k: int) -> List[List[int]]:
        m,n=len(g),len(g[0])
        for t in range(min(n,m)//2):
            p=[[t,j]for j in range(t,n-t)]+[[i,n-1-t]for i in range(t+1,m-t)]+[[m-1-t,j]for j in range(n-1-t-1,t-1,-1)]+[[i,t]for i in range(m-1-t-1,t,-1)]
            v=[g[i][j]for i,j in p]
            l=len(p)
            b=k%l
            v=v[b:]+v[:b]
            for h in range(l):
                g[p[h][0]][p[h][1]]=v[h]
        return g

class Solution:
    def rotateGrid(self, g: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(g),len(g[0]);r=range;[[setitem(g[x],y,d[(i+k)%len(c)])for i,(x,y)in enumerate(c)]for t in r(min(m,n)//2)for c in[[(t,j)for j in r(t,n+~t)]+[(i,n+~t)for i in r(t,m+~t)]+[(m+~t,j)for j in r(n+~t,t,-1)]+[(i,t)for i in r(m+~t,t,-1)]]for d in[[g[x][y]for x,y in c]]];return g

test('''
1914. Cyclically Rotating a Grid
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


Return the matrix after applying k cyclic rotations to it.

 

Example 1:


Input: grid = [[40,10],[30,20]], k = 1
Output: [[10,20],[40,30]]
Explanation: The figures above represent the grid at every state.
Example 2:


Input: grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
Output: [[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
Explanation: The figures above represent the grid at every state.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 50
Both m and n are even integers.
1 <= grid[i][j] <= 5000
1 <= k <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
16,467/31.8K
Acceptance Rate
51.8%
Topics
Senior
Array
Matrix
Simulation
Weekly Contest 247
icon
Companies
Hint 1
First, you need to consider each layer separately as an array.
Hint 2
Just cycle this array and then re-assign it.
''')
