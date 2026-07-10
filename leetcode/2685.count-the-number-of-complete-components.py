from lc import *

# https://leetcode.com/problems/count-the-number-of-complete-components/editorial/?envType=daily-question&envId=2026-07-11

class Solution:
    def countCompleteComponents(self, n: int, e: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        c = defaultdict(int)
        for i in range(n):
            g[i] = [i]
        for u,v in e:
            g[u].append(v)
            g[v].append(u)
        for i in range(n):
            c[tuple(sorted(g[i]))] += 1
        return sum(x==len(t)for t,x in c.items())


# https://leetcode.com/problems/count-the-number-of-complete-components/solutions/3557267/one-line-java-by-brinuke-u2nm/?envType=daily-question&envId=2026-07-11

'''
import static java.util.stream.Collectors.*;

class Solution {
    public static int countCompleteComponents(int n, int[][] edges) {
        return (int) Stream.concat(IntStream.range(0, n).mapToObj(i -> new int[] { i, i }), Stream.of(edges).flatMap(e -> Stream.of(e, new int[] { e[1], e[0] }))).collect(groupingBy(e -> e[0], mapping(e -> e[1], toSet()))).values().stream().collect(groupingBy(Function.identity(), counting())).entrySet().stream().filter(y -> y.getKey().size() == y.getValue()).count();
    }
}
'''

class Solution:
    def countCompleteComponents(self, n: int, e: List[List[int]]) -> int:
        a=[(1<<i)|sum(1<<x+y-i for x,y in e if i in (x,y))for i in range(n)];return sum(a.count(x)==x.bit_count()for x in{*a})

class Solution:
    def countCompleteComponents(self, n: int, e: List[List[int]]) -> int:
        a=[sum(1<<x+y-i for x,y in e if i in(x,y))|1<<i for i in range(n)];return sum(a.count(x)==x.bit_count()for x in{*a})

test('''
2685. Count the Number of Complete Components
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

 

Example 1:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.
Example 2:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
 

Constraints:

1 <= n <= 50
0 <= edges.length <= n * (n - 1) / 2
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no repeated edges.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
165,701/213.4K
Acceptance Rate
77.7%
Topics
Staff
Depth-First Search
Breadth-First Search
Union-Find
Graph Theory
Weekly Contest 345
icon
Companies
Hint 1
Find the connected components of an undirected graph using depth-first search (DFS) or breadth-first search (BFS).
Hint 2
For each connected component, count the number of nodes and edges in the component.
Hint 3
''')
