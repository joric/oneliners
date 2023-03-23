from lc import *

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        g,s = defaultdict(set),set()
        for i,j in connections:
            g[i].add(j)
            g[j].add(i)
        def f(i):
            if i in s:
                return 0
            s.add(i)
            for j in g[i]:
                f(j)
            return 1
        return sum(map(f,range(n))) - 1

# fastest (99.9%)

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        r = [*range(n)]
        def f(r,i):
            while r[i] is not i:
                r[i] = r[r[i]]
                i = r[i]
            return i
        for x,y in connections:
            a,b = f(r,x),f(r,y)
            if a is not b:
                r[a] = b
                n-=1
        return n-1

# shortest

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        s = ''.join(map(chr,range(n)))
        for a, b in connections:
            s = s.replace(s[a],s[b])
        return len(set(s))-1

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        return -1 if len(connections)<n-1 else len(set(reduce(lambda s,p:s.replace(s[p[0]],s[p[1]]),connections,''.join(map(chr,range(n))))))-1

test('''

1319. Number of Operations to Make Network Connected
Medium

3169

40

Add to List

Share
There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 

Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 

Constraints:

1 <= n <= 10^5
1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.

Accepted
116,374
Submissions
197,466

''')

