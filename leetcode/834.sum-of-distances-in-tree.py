from lc import *

# https://leetcode.com/problems/sum-of-distances-in-tree

class Solution:
    def sumOfDistancesInTree(self, N, edges):
        G = defaultdict(set)
        for i, j in edges:
            G[i].add(j)
            G[j].add(i)
        def dfs(node, parent, depth):
            ans = 1
            for neib in G[node]:
                if neib != parent:
                    ans += dfs(neib, node, depth + 1)
            weights[node] = ans
            depths[node] = depth
            return ans
        def dfs2(node, parent, w):
            ans[node] = w
            for neib in G[node]:
                if neib != parent:
                    dfs2(neib, node, w + N - 2*weights[neib])
        weights, depths, ans = [0]*N, [0]*N, [0]*N
        dfs(0, -1, 0)
        dfs2(0, -1, sum(depths))
        return ans

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
        and (f:=lambda o,p,d,r=1: ([r:=r+f(b,o,d+1) for b in g[o] if b!=p], setitem(m,o,r),setitem(h,o,d)) and r)(0, -1, 0) \
        and (e:=lambda o,p,w: (setitem(r,o,w),[e(b,o,w+n-2*m[b]) for b in g[o] if b!=p]))(0, -1, sum(h)) and r

# updated 2024-04-28

class Solution:
    def sumOfDistancesInTree(self, n: int, e: List[List[int]]) -> List[int]:
        g,m,h,r,s=defaultdict(set),[0]*n,[0]*n,[0]*n,setitem;[g[i].add(j)or g[j].add(i)for i,j in e];(f:=lambda o,p,d,r=1:([r:=r+f(b,o,d+1)for b in g[o]if b!=p],s(m,o,r),s(h,o,d))and r)(0,-1,0);(e:=lambda o,p,w:(s(r,o,w),[e(b,o,w+n-2*m[b])for b in g[o]if b!=p]))(0,-1,sum(h));return r

# https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130583/C%2B%2BJavaPython-Pre-order-and-Post-order-DFS-O(N)

class Solution:
    def sumOfDistancesInTree(self, n: int, e: List[List[int]]) -> List[int]:
        t,r,c = defaultdict(set),[0]*n,[1]*n
        for i,j in e:
            t[i].add(j)
            t[j].add(i)
        def f(x,p):
            for i in t[x]:
                if i != p:
                    f(i,x)
                    c[x] += c[i]
                    r[x] += r[i] + c[i]
        def g(x,p):
            for i in t[x]:
                if i != p:
                    r[i] = n+r[x]-c[i]*2
                    g(i,x)
        f(0,-1)
        g(0,-1)
        return r

class Solution:
    def sumOfDistancesInTree(self, n: int, e: List[List[int]]) -> List[int]:
        t,r,c,s=defaultdict(set),[0]*n,[1]*n,setitem;[t[i].add(j)or t[j].add(i)for i, j in e];(f:=lambda x,p:[(f(i,x),s(c,x,c[x]+c[i]),s(r,x,r[x]+r[i]+c[i]))for i in t[x]if i!=p])(0,-1);(g:=lambda x,p:[(s(r,i,n+r[x]-c[i]*2),g(i,x))for i in t[x]if i!=p])(0,-1);return r

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

