from lc import *

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        a = defaultdict(list)
        v = [0]*n
        c = [0]
        for i, j in connections:
            a[i].append([j,1])
            a[j].append([i,-1])
        def f(i):
            v[i] = 1
            for x in a[i]:
                if v[x[0]]==0:
                    f(x[0])
                    if x[1]==1:
                        c[0] += 1
        f(0)
        return c[0]

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        return (a:=defaultdict(list),v:=[0]*n,c:=[0],all((a[i].append([j,1]),a[j].append([i,-1])) for i, j in connections),(f:=lambda i:setitem(v,i,1) or [v[x[0]]==0 and f(x[0]) and x[1]==1 and setitem(c,0,c[0]+1) for x in a[i]])(0)) and c[0]

test('''

1466. Reorder Routes to Make All Paths Lead to the City Zero
Medium

2190

54

Add to List

Share
There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

 

Example 1:


Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:


Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0
 

Constraints:

2 <= n <= 5 * 10^4
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi

Accepted
76,335
Submissions
123,322

''')
