from lc import *

# https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/1982821/Python-Simple-and-Concise-MST-with-Explanation

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d, res = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}, 0
        while d:
            x, y = min(d, key=d.get)
            res += d.pop((x, y))
            for x1, y1 in d:
                d[(x1, y1)] = min(d[(x1, y1)], abs(x-x1)+abs(y-y1))
        return res

class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        return(f:=lambda d:d and d.pop(p:=min(d,key=d.get))+f({(x,y):min(d[x,y],abs(x-p[0])+abs(y-p[1]))for x,y in d})or 0)({(x,y):i and inf for i,(x,y)in enumerate(p)})

test('''
1584. Min Cost to Connect All Points
Medium

4003

88

Add to List

Share
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18
 

Constraints:

1 <= points.length <= 1000
-10^6 <= xi, yi <= 10^6
All pairs (xi, yi) are distinct.
''')

