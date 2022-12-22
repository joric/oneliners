from lc import *

class Solution:
    def sumOfDistancesInTree(self, n, edges):
        g = defaultdict(set)
        for i, j in edges:
            g[i].add(j)
            g[j].add(i)
        def f(o,p,d):
            r = 1
            for b in g[o]:
                if b!=p:
                    r += f(b,o,d+1)
            m[o] = r
            h[o] = d
            return r
        def e(o,p,w):
            r[o] = w
            for b in g[o]:
                if b!=p:
                    e(b,o,w+n-2*m[b])
        m, h, r = [0]*n, [0]*n, [0]*n
        f(0, -1, 0)
        e(0, -1, sum(h))
        return r

class Solution:
    def sumOfDistancesInTree(self, n, edges):
        return (g:=defaultdict(set),m:=[0]*n,h:=[0]*n,r:=[0]*n) and all((g[i].add(j),g[j].add(i)) for i,j in edges) \
        and (f:=lambda o,p,d,r=1: ([r:=r+f(b,o,d+1) for b in g[o] if b!=p], m.__setitem__(o,r),h.__setitem__(o,d)) and r)(0, -1, 0) \
        and (e:=lambda o,p,w: (r.__setitem__(o,w),[e(b,o,w+n-2*m[b]) for b in g[o] if b!=p]))(0, -1, sum(h)) and r

test('''

834. Sum of Distances in Tree
Hard

3351

73

Add to List

Share
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
Example 2:


Input: n = 1, edges = []
Output: [0]
Example 3:


Input: n = 2, edges = [[1,0]]
Output: [1,1]
 

Constraints:

1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.

''')


