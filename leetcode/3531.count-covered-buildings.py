from lc import * 

# https://leetcode.com/problems/count-covered-buildings/solutions/7400159/four-simple-lines-of-code-by-mikposp-omdx/

class Solution:
    def countCoveredBuildings(self, n: int, b: List[List[int]]) -> int:
        u,d,r,l = ([q]*-~n for q in [0,n,0,n])
        for x,y in b:
            u[x],d[x],l[y],r[y] = max(u[x],y),min(d[x],y),min(l[y],x),max(r[y],x)
        return sum(d[x]<y<u[x] and l[y]<x<r[y] for x,y in b)

class Solution:
    def countCoveredBuildings(self, n: int, b: List[List[int]]) -> int:
        u,d,r,l=([q]*-~n for q in[0,n,0,n]);[setitem(c,i,m(c[i],v))for x,y in b for m,c,i,v in((max,u,x,y),(min,d,x,y),(min,l,y,x),(max,r,y,x))];return sum(d[x]<y<u[x]and l[y]<x<r[y]for x,y in b)

test('''
3531. Count Covered Buildings
Medium
Topics
premium lock icon
Companies
Hint
You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

A building is covered if there is at least one building in all four directions: left, right, above, and below.

Return the number of covered buildings.

 

Example 1:



Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]

Output: 1

Explanation:

Only building [2,2] is covered as it has at least one building:
above ([1,2])
below ([3,2])
left ([2,1])
right ([2,3])
Thus, the count of covered buildings is 1.
Example 2:



Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]

Output: 0

Explanation:

No building has at least one building in all four directions.
Example 3:



Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]

Output: 1

Explanation:

Only building [3,3] is covered as it has at least one building:
above ([1,3])
below ([5,3])
left ([3,2])
right ([3,5])
Thus, the count of covered buildings is 1.
 

Constraints:

2 <= n <= 105
1 <= buildings.length <= 105 
buildings[i] = [x, y]
1 <= x, y <= n
All coordinates of buildings are unique.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
21,194/55.1K
Acceptance Rate
38.4%
Topics
Array
Hash Table
Sorting
Weekly Contest 447
icon
Companies
Hint 1
Group buildings with the same x or y value together, and sort each group.
Hint 2
In each sorted list, the buildings that are not at the first or last positions are covered in that direction.
''')
