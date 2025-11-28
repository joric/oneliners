from lc import *

# https://leetcode.com/problems/maximum-number-of-k-divisible-components/discuss/4110077/DFS-oror-python-oror-recursion

class Solution:
    def maxKDivisibleComponents(self, n: int, e: List[List[int]], v: List[int], k: int) -> int:
        g,s=defaultdict(list),set()
        for i,j in e:
            g[i].append(j)
            g[j].append(i)
        def f(i,x):
            if i in s:
                return 0,0
            s.add(i)
            t = v[i] % k
            r = 0
            for j in g[i]:
                if j != x:
                    a, b = f(j,i)
                    t = (t + b)%k
                    r += a
            return r+(t==0), t
        return max(f(0,-1)[0],1)

class Solution:
    def maxKDivisibleComponents(self, n: int, e: List[List[int]], v: List[int], k: int) -> int:
        g,s=defaultdict(list),set();[g[i].append(j)or g[j].append(i)for i,j in e];f=lambda i,x:i in s and(0,0)or((s.add(i),t:=v[i]%k)and sum((p:=f(j,i),t:=(t+p[1])%k)and p[0]for j in g[i]if j!=x)+(t==0),t);return max(f(0,-1)[0],1)

# POTD 2025-11-28

class Solution:
    def maxKDivisibleComponents(self, n: int, e: List[List[int]], v: List[int], k: int) -> int:
        g,s=defaultdict(set),set();[g[i].add(j)or g[j].add(i)for i,j in e];f=lambda i,x:i in s and(0,0)or((s.add(i),t:=v[i]%k)and sum((p:=f(j,i),t:=(t+p[1])%k)and p[0]for j in g[i]if j!=x)+(t==0),t);return max(f(0,-1)[0],1)


# https://leetcode.com/problems/maximum-number-of-k-divisible-components/solutions/6169655/dfs-based-solution-simple-short-code-by-6hftf/

class Solution:
    def maxKDivisibleComponents(self, n: int, e: List[List[int]], v: List[int], k: int) -> int:
        g = defaultdict(set)
        for i,j in e:
            g[i].add(j)
            g[j].add(i)
        r = 0
        def f(c, p):
            nonlocal r
            t = v[c]
            for d in g[c]:
                if d != p:
                    t += f(d, c)
            if t % k == 0:
                r += 1
            return t
        f(0,-1)
        return r

class Solution:
    def maxKDivisibleComponents(self, n: int, e: List[List[int]], v: List[int], k: int) -> int:
        g,r=defaultdict(set),[0];[g[i].add(j)or g[j].add(i)for i,j in e];(f:=lambda c,p:(t:=v[c]+sum(f(d,c)for d in g[c]if d!=p),setitem(r,0,r[0]+((t%k)<1)),t)[0])(0,-1);return r[0]

test('''
2872. Maximum Number of K-Divisible Components
Hard

299

9

Add to List

Share
There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array values of length n, where values[i] is the value associated with the ith node, and an integer k.

A valid split of the tree is obtained by removing any set of edges, possibly empty, from the tree such that the resulting components all have values that are divisible by k, where the value of a connected component is the sum of the values of its nodes.

Return the maximum number of components in any valid split.

 

Example 1:


Input: n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
Output: 2
Explanation: We remove the edge connecting node 1 with 2. The resulting split is valid because:
- The value of the component containing nodes 1 and 3 is values[1] + values[3] = 12.
- The value of the component containing nodes 0, 2, and 4 is values[0] + values[2] + values[4] = 6.
It can be shown that no other valid split has more than 2 connected components.
Example 2:


Input: n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
Output: 3

Explanation: We remove the edge connecting node 0 with 2, and the edge connecting node 0 with 1. The resulting split is valid because:
- The value of the component containing node 0 is values[0] = 3.
- The value of the component containing nodes 2, 5, and 6 is values[2] + values[5] + values[6] = 9.
- The value of the component containing nodes 1, 3, and 4 is values[1] + values[3] + values[4] = 6.
It can be shown that no other valid split has more than 3 connected components.
 

Other examples:

Input: n = 1, edges = [], values = [0], k = 1
Output: 1

Constraints:

1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
values.length == n
0 <= values[i] <= 109
1 <= k <= 109
Sum of values is divisible by k.
The input is generated such that edges represents a valid tree.
Accepted
22,230
Submissions
35,316
''')
