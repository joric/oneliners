from lc import *

# bfs
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g,s,q,r = defaultdict(list),set(),[1],inf
        for u,v,w in roads:
            g[u].append((v,w))
            g[v].append((u,w))
        while q:
            u = q.pop()
            for v,w in g[u]:
                r = min(r,w)
                if v not in s:
                    q.append(v)
                    s.add(v)
        return r

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        return next((r for _ in count() if not(q and (u:=q.pop(),[(r:=min(r,w),v not in s and (q.append(v),s.add(v))) for v,w in g[u]]))),
            (g:=defaultdict(list),s:=set(),q:=[1],r:=inf,all((g[u].append((v,w)),g[v].append((u,w))) for u,v,w in roads)))

# dfs
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g,s=defaultdict(list),set()
        for u,v,_ in roads:
            g[u].append(v)
            g[v].append(u)
        def f(u):
            if u not in s:
                s.add(u)
                all(map(f,g[u]))
        f(1)
        return min(w for u,v,w in roads if s>={u,v})

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        return (g:=defaultdict(list),s:=set(),all((g[u].append(v),g[v].append(u)) for u,v,_ in roads),
            (f:=lambda u:u not in s and (s.add(u),all(map(f,g[u]))))(1)) and min(w for u,v,w in roads if s>={u,v})

test('''

2492. Minimum Score of a Path Between Two Cities
Medium

331

51

Add to List

Share
You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.
 

Example 1:


Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
Example 2:


Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
 

Constraints:

2 <= n <= 10^5
1 <= roads.length <= 10^5
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distance_i <= 10^4
There are no repeated edges.
There is at least one path between 1 and n.

Accepted
15,795
Submissions
33,995

''')

