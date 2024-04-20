from lc import *

# https://leetcode.com/problems/find-all-groups-of-farmland/discuss/1640116/Python3-DFS-(easy-to-understand)

class Solution:
    def findFarmland(self, g: List[List[int]]) -> List[List[int]]:
        h,w=len(g),len(g[0])
        def f(i,j):
            if h>i>-1<j<w and g[i][j]:
                g[i][j] = 0
                a,b = f(i+1,j)
                c,d = f(i,j+1)
                return max(a,c,i),max(b,d,j)
            return 0,0
        return[(i,j)+f(i,j)for i in range(h)for j in range(w)if g[i][j]]

class Solution:
    def findFarmland(self, g: List[List[int]]) -> List[List[int]]:
        h,w=len(g),len(g[0]);return[(i,j)+(f:=lambda i,j:h>i>-1<j<w and g[i][j]and(setitem(g[i],j,0)or(lambda a,b,c,d:(max(a,c,i),max(b,d,j)))(*f(i+1,j)+f(i,j+1)))or(0,0))(i,j)for i in range(h)for j in range(w)if g[i][j]]

class Solution:
    def findFarmland(self, g: List[List[int]]) -> List[List[int]]:
        h,w=len(g),len(g[0]);return[(i,j)+(f:=lambda i,j:h>i>-1<j<w and g[i][j]and(setitem(g[i],j,0),p:=f(i+1,j)+f(i,j+1),max(*p[::2],i),max(*p[1::2],j))[2:]or(0,0))(i,j)for i in range(h)for j in range(w)if g[i][j]]

class Solution:
    def findFarmland(self, g: List[List[int]]) -> List[List[int]]:
        h,w=len(g),len(g[0])
        def f(i,j):
            if h>i>-1<j<w and g[i][j]:
                g[i][j] = 0
                return map(max,zip(f(i+1,j),f(i,j+1),(i,j)))
            return 0,0
        return[(i,j,*f(i,j))for i in range(h)for j in range(w)if g[i][j]]

class Solution:
    def findFarmland(self, g: List[List[int]]) -> List[List[int]]:
        h,w=len(g),len(g[0]);return[(i,j,*(f:=lambda i,j:h>i>-1<j<w and g[i][j]and(setitem(g[i],j,0)or map(max,zip(f(i+1,j),f(i,j+1),(i,j))))or(0,0))(i,j))for i in range(h)for j in range(w)if g[i][j]]

class Solution:
    def findFarmland(self, g: List[List[int]]) -> List[List[int]]:
        e=enumerate;return[(i,j,*(f:=lambda i,j:g[i:]and g[i][j:]and g[i][j]and(setitem(g[i],j,0)or map(max,zip(f(i+1,j),f(i,j+1),(i,j))))or(0,0))(i,j))for i,r in e(g)for j,v in e(r)if v]

class Solution:
    def findFarmland(self, g: List[List[int]]) -> List[List[int]]:
        e=enumerate;return[(i,j,*(f:=lambda i,j:g[i:] and g[j::1]and(setitem(g[i],j,0)or map(max,zip(f(i+1,j),f(i,j+1),(i,j))))or(0,0))(i,j))for i,r in e(g)for j,v in e(r)if v]

test('''
1992. Find All Groups of Farmland
Medium

880

37

Add to List

Share
You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.

 

Example 1:


Input: land = [[1,0,0],[0,1,1],[0,1,1]]
Output: [[0,0,0,0],[1,1,2,2]]
Explanation:
The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0].
The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].
Example 2:


Input: land = [[1,1],[1,1]]
Output: [[0,0,1,1]]
Explanation:
The first group has a top left corner at land[0][0] and a bottom right corner at land[1][1].
Example 3:


Input: land = [[0]]
Output: []
Explanation:
There are no groups of farmland.
 

Other examples:

Input: land = [[1,0],[1,0]]
Output: [[0,0,1,0]]

Constraints:

m == land.length
n == land[i].length
1 <= m, n <= 300
land consists of only 0's and 1's.
Groups of farmland are rectangular in shape.
Accepted
39,236
Submissions
55,205
''')
