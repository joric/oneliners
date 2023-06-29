from lc import *

# https://leetcode.com/problems/path-with-maximum-probability/discuss/731760/Python-Short-Dijkstra

class Solution:
    def maxProbability(self, n: int, m: List[List[int]], c: List[float], s: int, e: int) -> float:
        g,v,h=defaultdict(dict),set(),[(-1,s)]
        for (a,b),p in zip(m,c):
            g[a][b]=g[b][a]=p
        while h:
            p,o=heappop(h)
            if o==e:
                return -p
            v.add(o)
            for i in g[o]:
                if i not in v:
                    heappush(h,(p*g[o][i],i))
        return 0

class Solution:
    def maxProbability(self, n: int, m: List[List[int]], c: List[float], s: int, e: int) -> float:
        g,v,h=defaultdict(dict),set(),[(-1,s)];[setitem(g[a],b,p)or setitem(g[b],a,p)for(a,b),p in zip(m,c)];return next(-p for _ in count()if not((p:=len(h)and h[0][0])and(o:=heappop(h)[1])!=e and(v.add(o),[heappush(h,(p*g[o][i],i))for i in g[o]if i not in v])))

# https://leetcode.com/problems/path-with-maximum-probability/discuss/1011001/Python-Simple-Djikstra's-and-Bellman-Ford-algorithm

class Solution:
    def maxProbability(self, n: int, m: List[List[int]], c: List[float], u: int, v: int) -> float:
        d = [0] * n
        d[u] = 1
        for i in range(int(sqrt(n))):
            for (s,e),p in zip(m,c):
                if d[s] != 0 and d[s] * p > d[e]:
                    d[e] = d[s] * p
                if d[e] != 0 and d[e] * p > d[s]:
                    d[s] = d[e] * p
        return d[v]

class Solution:
    def maxProbability(self, n: int, m: List[List[int]], c: List[float], u: int, v: int) -> float:
        d = [0] * n
        d[u] = 1
        for i in range(int(sqrt(n))):
            for(s,e),p in zip(m,c):
                for q,r in([s,e],[e,s]):
                    d[q] = max(d[q],d[r]*p)
        return d[v]

class Solution:
    def maxProbability(self, n: int, m: List[List[int]], c: List[float], u: int, v: int) -> float:
        d=[0]*n;d[u]=1;[setitem(d,q,max(d[q],d[r]*p))for i in range(int(sqrt(n))) for(s,e),p in zip(m,c)for q,r in([s,e],[e,s])];return d[v]


test('''
1514. Path with Maximum Probability
Medium

1816

36

Add to List

Share
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.
 

Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
Accepted
67,986
Submissions
138,548
Seen this question in a real interview before?

Yes

No
Multiplying probabilities will result in precision errors.
Take log probabilities to sum up numbers instead of multiplying them.
Use Dijkstra's algorithm to find the minimum path between the two nodes after negating all costs.
''')


