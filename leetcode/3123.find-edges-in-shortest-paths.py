from lc import *

# Q4. https://leetcode.com/contest/weekly-contest-394/
# https://leetcode.com/problems/find-edges-in-shortest-paths/

# https://leetcode.com/problems/find-edges-in-shortest-paths/discuss/5052501/Python3-Dijkstra-from-2-ends
class Solution:
    def findAnswer(self, n: int, e: List[List[int]]) -> List[bool]:
        def f(y): 
            d = [inf]*n
            d[y] = 0 
            q = [(0,y)]
            while q: 
                x, u = heappop(q)
                if d[u] == x: 
                    for v, w in g[u]: 
                        if x+w < d[v]: 
                            d[v] = x+w
                            heappush(q, (x+w, v))
            return d
        g = defaultdict(list)
        [g[u].append((v,w))or g[v].append((u,w))for u,v,w in e]
        a,b = f(0),f(n-1)
        return [inf>a[n-1]and(a[u]+w+b[v]==a[n-1]or a[v]+w+b[u]==a[n-1])for u,v,w in e]

class Solution:
    def findAnswer(self, n: int, e: List[List[int]]) -> List[bool]:
        g=defaultdict(list);[g[u].append((v,w))or g[v].append((u,w))for u,v,w in e];f=lambda y:(d:=[inf]*n,setitem(d,y,0),q:=[],(r:=lambda x,u:(x==d[u]and[x+w<d[v]and(setitem(d,v,x+w),heappush(q,(x+w,v)))for v,w in g[u]],q and r(*heappop(q))))(0,y))and d;a=f(0);b=f(n-1);return[inf>a[u]+w+b[v]==a[n-1]or inf>a[v]+w+b[u]==a[n-1]for u,v,w in e]

test('''
3123. Find Edges in Shortest Paths
Hard

26

1

Add to List

Share
You are given an undirected weighted graph of n nodes numbered from 0 to n - 1. The graph consists of m edges represented by a 2D array edges, where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.

Consider all the shortest paths from node 0 to node n - 1 in the graph. You need to find a boolean array answer where answer[i] is true if the edge edges[i] is part of at least one shortest path. Otherwise, answer[i] is false.

Return the array answer.

Note that the graph may not be connected.

 

Example 1:


Input: n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]

Output: [true,true,true,false,true,true,true,false]

Explanation:

The following are all the shortest paths between nodes 0 and 5:

The path 0 -> 1 -> 5: The sum of weights is 4 + 1 = 5.
The path 0 -> 2 -> 3 -> 5: The sum of weights is 1 + 1 + 3 = 5.
The path 0 -> 2 -> 3 -> 1 -> 5: The sum of weights is 1 + 1 + 2 + 1 = 5.
Example 2:


Input: n = 4, edges = [[2,0,1],[0,1,1],[0,3,4],[3,2,2]]

Output: [true,false,false,true]

Explanation:

There is one shortest path between nodes 0 and 3, which is the path 0 -> 2 -> 3 with the sum of weights 1 + 2 = 3.

 

Constraints:

2 <= n <= 5 * 104
m == edges.length
1 <= m <= min(5 * 104, n * (n - 1) / 2)
0 <= ai, bi < n
ai != bi
1 <= wi <= 105
There are no repeated edges.
Accepted
3,045
Submissions
7,023
''')