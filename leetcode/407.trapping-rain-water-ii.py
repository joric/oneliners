from lc import *

# https://leetcode.com/problems/trapping-rain-water-ii/solutions/7244645/14-lines-of-python-code-beats-100-70ms-o-k-m-n/?envType=daily-question&envId=2025-10-03

import numpy as np
class Solution:             # Time = O(k*m*n) | Space = O(m*n)
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        heightMap = np.array(heightMap, dtype=int)
        water_level, w_old = heightMap.copy(), 0
        water_level[1:-1, 1:-1] = np.max(heightMap)
        while True:
            wl = np.pad(water_level, ((1, 1), (1, 1)))
            water_level = np.maximum(np.minimum(
                    np.minimum(wl[0:-2, 1:-1], wl[2:, 1:-1]), 
                    np.minimum(wl[1:-1, 0:-2], wl[1:-1, 2:])), heightMap)
            w = np.sum(water_level - heightMap)
            if w == w_old:  return int(w)
            else:   w_old = w

# https://leetcode.com/problems/trapping-rain-water-ii/solutions/245884/python-heap-solution-15-lines/?envType=daily-question&envId=2025-10-03

class Solution:
    def trapRainWater(self, hm: List[List[int]]) -> int:
        if not hm or not hm[0]: return 0
        m, n, res = len(hm), len(hm[0]), 0
        heap = list(set([(hm[i][0], i, 0) for i in range(m)] + [(hm[i][n - 1], i, n - 1) for i in range(m)] + [(hm[0][j], 0, j) for j in range(n)] + [(hm[m - 1][j], m - 1, j) for j in range(n)]))
        heapq.heapify(heap)
        seen = {(x, y) for h, x, y in heap}
        while heap:
            h, x, y = heapq.heappop(heap)
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                xx, yy = x + d[0], y + d[1]
                if not (xx >= m or xx < 0 or yy >= n or yy < 0 or (xx, yy) in seen): 
                    seen.add((xx, yy))
                    res += max(0, h - hm[xx][yy])
                    heapq.heappush(heap, (max(h, hm[xx][yy]), xx, yy))
        return res

class Solution:
    def trapRainWater(self, h: List[List[int]]) -> int:
        m, n, r = len(h), len(h[0]), 0
        q = [*set((h[i][j],i,j)for i in range(m)for j in range(n)if i in(0,m-1)or j in(0,n-1))]
        v = {(x,y)for z,x,y in q}
        heapify(q)
        while q:
            z, x, y = heappop(q)
            for i,j in((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if m>i>-1<j<n and (i,j)not in v:
                    v.add((i, j))
                    heappush(q,(max(z,h[i][j]),i,j))
                    r += max(0,z-h[i][j])
        return r

class Solution:
    def trapRainWater(self, h: List[List[int]]) -> int:
        m,n=len(h),len(h[0]);q=[*set((h[i][j],i,j)for i in range(m)for j in range(n)if i in(0,m-1)or j in(0,n-1))];v={(x,y)for z,x,y in q};heapify(q);return(f:=lambda z,x,y:sum(v.add((i,j))or heappush(q,(max(z,h[i][j]),i,j))or max(0,z-h[i][j]) for i,j in((x+1,y),(x-1,y),(x,y+1),(x,y-1))if m>i>-1<j<n and (i,j)not in v)+(q and f(*heappop(q))or 0))(*heappop(q))

test('''
407. Trapping Rain Water II
Solved
Hard
Topics
premium lock icon
Companies
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

 

Example 1:


Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
Example 2:


Input: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
Output: 10
 

Constraints:

m == heightMap.length
n == heightMap[i].length
1 <= m, n <= 200
0 <= heightMap[i][j] <= 2 * 104
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
227,699/365.7K
Acceptance Rate
62.3%
Topics
Array
Breadth-First Search
Heap (Priority Queue)
Matrix
icon
Companies
Similar Questions
Trapping Rain Water
Hard
Maximum Number of Points From Grid Queries
Hard
''')
