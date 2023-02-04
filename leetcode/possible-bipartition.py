from lc import *

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph, color = defaultdict(list), {}
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node, c = 0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])
        return all(dfs(node) for node in range(1, n+1) if node not in color)

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        return (g:=defaultdict(list),c:={},all((g[u].append(v),g[v].append(u)) for u,v in dislikes),f:=lambda k,v=0:c[k]==v if k in c else (setitem(c,k,v) or all(f(w, v^1) for w in g[k]))) and all(f(k) for k in range(1, n+1) if k not in c)

test('''

886. Possible Bipartition
Medium

3013

66

Add to List

Share
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Constraints:

1 <= n <= 2000
0 <= dislikes.length <= 10^4
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
All the pairs of dislikes are unique.

''')

