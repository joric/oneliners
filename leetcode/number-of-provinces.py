from lc import *

# https://leetcode.com/problems/number-of-provinces/discuss/1231384/8-lines-Python-with-explanation

class Solution:
    def findCircleNum(self, m: List[List[int]]) -> int:
        g,n,v,f=defaultdict(list),len(m),set(),lambda g,s,v:v.add(s)or[f(g,n,v) for n in g[s] if n not in v]
        [(g[i].append(j),g[j].append(i)) for i in range(n) for j in range(i+1,n) if m[i][j]==1]
        return len([f(g,s,v) for s in range(n) if s not in v])

# https://leetcode.com/problems/number-of-provinces/discuss/129360/Python-8-lines-easy-and-clear-DFS-solution-64-ms-beats-68

class Solution:
    def findCircleNum(self, m: List[List[int]]) -> int:
        p=''.join(map(chr,range(s:=len(m))));[p:=p.replace(p[k],p[n]) for n in range(s) for k in range(n) if m[n][k]];return len(set(p))

# https://leetcode.com/problems/number-of-provinces/discuss/772762/One-Line-Linear-Algebraic-Solution

class Solution:
    def findCircleNum(self, m: List[List[int]]) -> int:
        np=__import__('numpy');return len(m)-np.linalg.matrix_rank(np.diag(np.sum(m,axis=1))-m)


test('''
547. Number of Provinces
Medium

7669

295

Add to List

Share
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
Accepted
633,641
Submissions
989,206
''')

