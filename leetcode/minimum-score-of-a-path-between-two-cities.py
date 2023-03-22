from lc import *

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        (r:=set(),s:={1})
        g,d = defaultdict(list),defaultdict(set)
        for a,b,t in roads:
            g[a].append(b)
            g[b].append(a)
            d[a].add(t)
            d[b].add(t)
        def f(r,s,x):
            s.add(x)
            r.update(set(d[x]))
            for y in g[x]:
                if y not in s:
                    f(r,s,y)
        f(r,s,1)
        return min(r)

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        return (r:=set(),s:={1},g:=defaultdict(list),d:=defaultdict(set),all((g[a].append(b),g[b].append(a),d[a].add(t),d[b].add(t)) for a,b,t in roads),(f:=lambda r,s,x:(s.add(x),r.update(set(d[x])),all(f(r,s,y) for y in g[x] if y not in s)))(r,s,1),min(r))[-1]

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

