from lc import *

class Solution:
    def maxNumEdgesToRemove(self, n: int, e: List[List[int]]) -> int:
        p,r,a,b = [*range(n+1)],0,0,0
        def f(x):
            if p[x] != x:
                p[x] = f(p[x])
            return p[x]

        def u(i,j):
            x, y = f(i), f(j)
            if x == y:
                return False
            else:
                p[y] = x
                return True

        for t,i,j in e:
            if t == 3:
                if u(i,j):
                    a += 1
                    b += 1 
                else:
                    r += 1

        q = p[:]
        for t,i,j in e:
            if t == 1:
                if u(i,j):
                    a += 1
                else:
                    r += 1

        p = q[:]
        for t,i,j in e:
            if t == 2:
                if u(i,j):
                    b += 1
                else:
                    r += 1

        return r if a == b == n - 1 else -1

class Solution:
    def maxNumEdgesToRemove(self, n: int, e: List[List[int]]) -> int:
        r = a = b = 0
        p = [*range(n+1)]
        f = lambda x:p[x]!=x and setitem(p,x,f(p[x])) or p[x]
        u = lambda i,j:(x:=f(i))!=(y:=f(j)) and not setitem(p,y,x)
        [(a:=a+1,b:=b+1) if u(i,j) else (r:=r+1) for t,i,j in e if t==3]
        q = p[:]
        [(a:=a+1) if u(i,j) else (r:=r+1) for t,i,j in e if t==1]
        p = q[:]
        [(b:=b+1) if u(i,j) else (r:=r+1) for t,i,j in e if t==2]
        return r if a==b==n-1 else -1

class Solution:
    def maxNumEdgesToRemove(self, n: int, e: List[List[int]]) -> int:
        return (r:=(a:=(b:=0)),p:=[*range(n+1)],f:=lambda x:p[x]!=x and setitem(p,x,f(p[x])) or p[x],u:=lambda i,j:(x:=f(i))!=(y:=f(j)) and not setitem(p,y,x),[(a:=a+1,b:=b+1) if u(i,j) else (r:=r+1) for t,i,j in e if t==3],q:=p[:],[(a:=a+1) if u(i,j) else (r:=r+1) for t,i,j in e if t==1],p:=q[:],[(b:=b+1) if u(i,j) else (r:=r+1) for t,i,j in e if t==2],r if a==b==n-1 else -1)[-1]

test('''
1579. Remove Max Number of Edges to Keep Graph Fully Traversable
Hard

976

11

Add to List

Share
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

Constraints:

1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.
Accepted
18,954
Submissions
35,524
Seen this question in a real interview before?

Yes

No
Build the network instead of removing extra edges.
Suppose you have the final graph (after removing extra edges). Consider the subgraph with only the edges that Alice can traverse. What structure does this subgraph have? How many edges are there?
Use disjoint set union data structure for both Alice and Bob.
Always use Type 3 edges first, and connect the still isolated ones using other edges.
''')

