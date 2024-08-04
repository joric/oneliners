from lc import *

# https://leetcode.com/problems/regions-cut-by-slashes/discuss/205680/JavaC%2B%2BPython-Split-4-parts-and-Union-Find

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        f = {}
        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]
        def union(x, y):
            f[find(x)] = find(y)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    union((i - 1, j, 2), (i, j, 0))
                if j:
                    union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] != "/":
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if grid[i][j] != "\\":
                    union((i, j, 3), (i, j, 0))
                    union((i, j, 1), (i, j, 2))
        return len(set(map(find, f)))

class Solution:
    def regionsBySlashes(self, g: List[str]) -> int:
        d,r,f,u={},range(len(g)),lambda x:d.setdefault(x,x)and x!=d[x]and setitem(d,x,f(d[x]))or d[x],lambda x,y:setitem(d,f(x),f(y));[(i and u((i-1,j,2),(i,j,0)),j and u((i,j-1,1),(i,j,3)),g[i][j]!='/' and(u((i,j,0),(i,j,1)),u((i,j,2),(i,j,3))),g[i][j]!='\\'and(u((i,j,3),(i,j,0)),u((i,j,1),(i,j,2))))for i in r for j in r];return len({*map(f,d)})

test(r'''''
959. Regions Cut By Slashes
Medium

3078

584

Add to List

Share
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:


Input: grid = [" /","/ "]
Output: 2
Example 2:


Input: grid = [" /","  "]
Output: 1
Example 3:


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.
Accepted
52,125
Submissions
75,004
''')
