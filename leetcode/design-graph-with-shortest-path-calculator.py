from lc import *

# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/discuss/3420014/JavaPython-3-Dijkstra-Algorithm.

class Graph:
    def __init__(self, n: int, e: List[List[int]]):
        self.g = defaultdict(dict)
        any(map(self.addEdge,e))
    def addEdge(self, e: List[int]) -> None:
        a,b,c = e
        self.g[a][b]=c
    def shortestPath(self, a: int, b: int) -> int:
        v,h=set(),[(0,a)]
        while h:
            c,x = heappop(h)
            if x == b:
                return c
            if x not in v and x in self.g:
                v.add(x)
                for y,d in self.g[x].items():
                    heappush(h,(c+d,y))
        return -1

class Graph:
    def __init__(s, n: int, e: List[List[int]]):
        (setattr(s,'g',defaultdict(dict)),[*map(s.addEdge,e)])and None
    def addEdge(s, e: List[int]) -> None:
        setitem(s.g[e[0]],e[1],e[2])
    def shortestPath(s, a: int, b: int) -> int:
        v,h=set(),[(0,a)]
        while h:
            c,x = heappop(h)
            if x==b:
                return c
            x not in v and x in s.g and(v.add(x),any(heappush(h,(c+d,y))for y,d in s.g[x].items()))
        return -1

class Graph:
    def __init__(s, n: int, e: List[List[int]]):
        (setattr(s,'g',defaultdict(dict)),[*map(s.addEdge,e)])and None
    def addEdge(s, e: List[int]) -> None:
        setitem(s.g[e[0]],e[1],e[2])
    def shortestPath(s, a: int, b: int) -> int:
        return(v:=set(),h:=[(0,a)])and(f:=lambda c,x:c if x==b else[x not in v and x in s.g and(v.add(x),[heappush(h,(c+d,y))for y,d in s.g[x].items()])]and h and f(*heappop(h))or-1)(*heappop(h))

Graph=type('',(),{'__init__':lambda s,n,e:(setattr(s,'g',defaultdict(dict)),[*map(s.addEdge,e)])and None,'addEdge':lambda s,e:setitem(s.g[e[0]],e[1],e[2]),'shortestPath':lambda s,a,b:(v:=set(),h:=[])and(f:=lambda c,x:c if x==b else[x not in v and x in s.g and(v.add(x),[heappush(h,(c+d,y))for y,d in s.g[x].items()])]and h and f(*heappop(h))or-1)(0,a)})

test('''
2642. Design Graph With Shortest Path Calculator
Hard

407

29

Add to List

Share
There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:

Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
 

Example 1:


Input
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
Output
[null, 6, -1, null, 6]

Explanation
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.
 

Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1)
edges[i].length == edge.length == 3
0 <= fromi, toi, from, to, node1, node2 <= n - 1
1 <= edgeCosti, edgeCost <= 10^6
There are no repeated edges and no self-loops in the graph at any point.
At most 100 calls will be made for addEdge.
At most 100 calls will be made for shortestPath.
Accepted
24,401
Submissions
36,420
''', classname=Graph)

