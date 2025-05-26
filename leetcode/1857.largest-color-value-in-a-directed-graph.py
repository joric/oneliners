from lc import *

# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/discuss/1198908/Python-shortest-code-and-fast

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        d,g,c = Counter(), defaultdict(list), defaultdict(Counter)
        for u, v in edges:
            g[u].append(v)
            d[v] += 1
        q = [u for u in range(len(colors)) if d[u]==0]
        for u in q:
            c[u][colors[u]] += 1
            for v in g[u]:
                c[v] |= c[u]
                d[v] -= 1
                if d[v]==0:
                    q.append(v)
        return sum(d.values()) and -1 or max(max(c[u].values()) for u in c)

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        return (d:=Counter(),g:=defaultdict(list),c:=defaultdict(Counter),[(g[u].append(v),d.update({v})) for u,v in edges],q:=[u for u in range(len(colors)) if d[u]==0],[(c[u].update({colors[u]:1}),[(setitem(c,v,c[v]|c[u]),d.update({v:-1}),d[v]==0 and q.append(v)) for v in g[u]]) for u in q],sum(d.values()) and -1 or max(max(c[u].values()) for u in c))[-1]

class Solution:
    def largestPathValue(self, s: str, e: List[List[int]]) -> int:
        d,g,c=Counter(),defaultdict(list),defaultdict(Counter);[(g[u].append(v),d.update({v})) for u,v in e];q=[u for u in range(len(s))if d[u]==0];[(c[u].update({s[u]:1}),[(setitem(c,v,c[v]|c[u]),d.update({v:-1}),d[v]==0 and q.append(v))for v in g[u]])for u in q];return sum(d.values())and -1 or max(max(c[u].values())for u in c)

# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/solutions/3397614/python-short-and-clean-dfs-dp-functional-programming/

class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        Node = int
        Color = str
        Graph = Mapping[Node, tuple[Color, Collection[Node]]]
        def max_color_count(graph: Graph) -> int:
            seen: set[Node] = set()
            @cache
            def count_colors(root: Node) -> Counter[Color]:
                color, nodes = graph[root]
                if root in seen: return Counter({color: inf})
                seen.add(root)
                counter = Counter({color: 1}) + reduce(or_, map(count_colors, nodes), Counter())
                seen.remove(root)
                return counter
            return max(count_colors(node).most_common(1)[0][1] for node in graph)
        graph: Graph = {i: (c, set()) for i, c in enumerate(colors)}
        for u, v in edges: graph[u][1].add(v)
        count: int = max_color_count(graph)
        return -1 if count == inf else count

class Solution:
    def largestPathValue(self, o: str, e: List[List[int]]) -> int:
        g,s,c={i:[x,set()]for i, x in enumerate(o)},set(),Counter;[g[u][1].add(v)for u,v in e];f=cache(lambda u:c({g[u][0]:inf})if u in s else(s.add(u),c({g[u][0]: 1})+reduce(or_,map(f,g[u][1]),c()),s.remove(u))[1]);return(-1,n:=max(f(u).most_common(1)[0][1] for u in g))[n<inf]

test('''
1857. Largest Color Value in a Directed Graph
Hard

845

30

Add to List

Share
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

Example 1:



Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:



Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
 

Example 3:
Input: colors = "hhqhuqhqff", edges = [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]
Output: 3

Example 4:
Input: colors = "ab", edges = [[0,1],[1,1]]
Output: -1

Example 5:
Input: colors = "g", edges = []
Output: 1

Constraints:

n == colors.length
m == edges.length
1 <= n <= 10^5
0 <= m <= 10^5
colors consists of lowercase English letters.
0 <= aj, bj < n
Accepted
20,464
Submissions
46,296
Seen this question in a real interview before?

Yes

No
Use topological sort.
let dp[u][c] := the maximum count of vertices with color c of any path starting from vertex u. (by JerryJin2905)
''')
