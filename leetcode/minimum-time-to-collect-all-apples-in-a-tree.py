from lc import *

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g = [[] for _ in range(n)]
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        def dfs(a,p,d=0):
            for b in g[a]:
                if b != p:
                    d += dfs(b,a)
            return d+2 if d or hasApple[a] else 0
        return max(dfs(0,-1)-2,0)


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        return (g:=[[] for _ in range(n)]) and [g[a].append(b) or g[b].append(a) for a,b in edges] and max(((f:=lambda a,p,d=0:([d:=d+f(b,a) for b in g[a] if b!=p] and d or hasApple[a]) and d+2 or 0))(0,-1)-2,0)


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        g,s = defaultdict(list), set()
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        def f(i):
            s.add(i)
            d = sum(f(j) for j in g[i] if not j in s)
            return 2*(i>0)+d if d or hasApple[i] else 0
        return f(0)

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        return (g:=defaultdict(list),s:=set(),[g[a].append(b) or g[b].append(a) for a,b in edges]) and (f:=lambda i:s.add(i) or int((d:=sum(f(j) for j in g[i] if not j in s)) or hasApple[i]) and 2*(i>0)+d)(0)


test('''

1443. Minimum Time to Collect All Apples in a Tree
Medium

1195

95

Add to List

Share
Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

 

Example 1:


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 2:


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
Example 3:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0
 

Example 4:

Input: n = 4, edges = [[0,2],[0,3],[1,2]], hasApple = [false,true,false,false]
Output: 4

Constraints:

1 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai < bi <= n - 1
fromi < toi
hasApple.length == n

''')

