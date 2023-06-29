from lc import *

# https://leetcode.com/problems/shortest-path-to-get-all-keys/discuss/1516812/Python3-bfs

class Solution:
    def shortestPathAllKeys(self, g: List[str]) -> int:
        m, n = len(g), len(g[0])
        x = y = t = 0
        for i in range(m):
            for j in range(n):
                if g[i][j]=='@':
                    x,y = i,j
                elif g[i][j].islower():
                    t += 1
        r = 0
        v = {(x,y,0)}
        q = deque([(x,y,0)])
        while q: 
            l = len(q)
            for _ in range(l):
                i,j,k = q.popleft()
                if k == (1 << t) - 1:
                    return r 
                for x,y in (i-1,j),(i,j-1),(i,j+1),(i+1,j):
                    if m>x>=0<=y<n and g[x][y]!='#': 
                        z = k 
                        if g[x][y].islower():
                            z |= 1<<ord(g[x][y])-ord('a')
                        if (x,y,z) in v or g[x][y].isupper() and not z & (1<<ord(g[x][y])-ord('A')):
                            continue 
                        q.append((x,y,z))
                        v.add((x,y,z))
            r += 1
        return -1

# TODO maybe similar to 847 https://leetcode.com/problems/shortest-path-visiting-all-nodes
# https://github.com/joric/oneliners/blob/main/leetcode/shortest-path-visiting-all-nodes.py

class Solution:
    def shortestPathAllKeys(self, g: List[str]) -> int:
        m, n = len(g), len(g[0])
        x = y = t = 0
        for i in range(m):
            for j in range(n):
                if g[i][j]=='@':
                    x,y = i,j
                elif g[i][j].islower():
                    t += 1
        r = 0
        v = {(x,y,0)}
        q = [(x,y,0)]

        while q: 
            w = []
            for i,j,k in q:
                if k == (1 << t) - 1:
                    return r
                for x,y in (i-1,j),(i,j-1),(i,j+1),(i+1,j):
                    if m>x>=0<=y<n and g[x][y]!='#': 
                        z = k 
                        if g[x][y].islower():
                            z |= 1<<ord(g[x][y])-ord('a')
                        if (x,y,z) not in v and (not g[x][y].isupper() or z & (1<<ord(g[x][y])-ord('A'))):
                            w.append((x,y,z))
                            v.add((x,y,z))
            r += 1
            q = w
        return -1

class Solution:
    def shortestPathAllKeys(self, g: List[str]) -> int:
        m,n=len(g),len(g[0]);x=y=t=0;r=0;v = {(x,y,0)};q=[(x,y,0)]
        [g[i][j]=='@' and(x:=i,y:=j)or g[i][j].islower()and(t:=t+1)for i in range(m)for j in range(n)]
        while q:
            w = []
            for i,j,k in q:
                if k == (1 << t) - 1:
                    return r
                [(z:=k,g[x][y].islower()and(z:=z|1<<ord(g[x][y])-ord('a')),((x,y,z) not in v and(not g[x][y].isupper() or z & (1<<ord(g[x][y])-ord('A'))))and(w.append((x,y,z)),v.add((x,y,z))))for x,y in ((i-1,j),(i,j-1),(i,j+1),(i+1,j)) if m>x>=0<=y<n and g[x][y]!='#']
            r += 1
            q = w
        return -1

test('''
864. Shortest Path to Get All Keys
Hard

1039

48

Add to List

Share
You are given an m x n grid grid where:

'.' is an empty cell.
'#' is a wall.
'@' is the starting point.
Lowercase letters represent keys.
Uppercase letters represent locks.
You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

 

Example 1:


Input: grid = ["@.a..","###.#","b.A.B"]
Output: 8
Explanation: Note that the goal is to obtain all the keys not to open all the locks.
Example 2:


Input: grid = ["@..aA","..B#.","....b"]
Output: 6
Example 3:


Input: grid = ["@Aa"]
Output: -1
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either an English letter, '.', '#', or '@'.
The number of keys in the grid is in the range [1, 6].
Each key in the grid is unique.
Each key in the grid has a matching lock.
''')

