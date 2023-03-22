from lc import *

# bfs
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g,v,q,r = defaultdict(list),set(),[1],inf
        for a,b,d in roads:
            g[a].append((b,d))
            g[b].append((a,d))
        while q:
            x = q.pop()
            for a,d in g[x]:
                r = min(r,d)
                if a not in v:
                    q.append(a)
                    v.add(a)
        return r

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        return next((r for _ in count() if not(q and (x:=q.pop(),[(r:=min(r,s),a not in v and (q.append(a),v.add(a))) for a,s in g[x]]))),(g:=defaultdict(list),r:=inf,v:=set(),q:=[1],all((g[a].append((b,d)),g[b].append((a,d))) for a,b,d in roads)))

# dfs
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g,v=defaultdict(list),set()
        for a,b,d in roads:
            g[a].append((b,d))
            g[b].append((a,d))
        def f(a,v):
            if a not in v:
                v.add(a)
                for b,d in g[a]:
                    f(b,v)
        f(1,v)
        return min(d for a,b,d in roads if a in v and b in v)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        return (g:=defaultdict(list),v:=set(),all((g[a].append((b,d)),g[b].append((a,d))) for a,b,d in roads),(f:=lambda a,v: a not in v and (v.add(a),[f(b,v) for b,d in g[a]]))(1,v)) and min(d for a,b,d in roads if a in v and b in v)

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

