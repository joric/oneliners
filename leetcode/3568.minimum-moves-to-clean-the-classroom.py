from lc import *

# https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/solutions/6800295/bfs-bitmask-by-buggy_d_clown-e9k1/?envType=daily-question&envId=2026-09-01

class Solution:
    def minMoves(self, c: List[str], e: int) -> int:
        l={};q=deque();a,b=len(c),len(c[0])
        for i in range(a):
            for j in range(b):
                if(v:=c[i][j])=='S':
                    q+=[(0,i,j,0)];u,w=i,j
                if v=='L':
                    l[i,j]=len(l)
        if not l:
            return 0
        f=2**len(l)-1;s={(u,w,0):e}
        while q:
            m,i,j,k=q.popleft()
            for x,y in(i-1,j),(i+1,j),(i,j-1),(i,j+1):
                if 0<=x<a and 0<=y<b and(v:=c[x][y])!='X':
                    t,n=k,s[i,j,k]-1
                    if v=='L'and(t:=k|1<<l[x,y])==f:
                        return m+1
                    if v=='R':
                        n=e
                    if s.get((x,y,t),0)<n:
                        s[x,y,t]=n
                        q+=[(m+1,x,y,t)]
        return-1

class Solution:
    def minMoves(self, c: List[str], e: int) -> int:
        return[a:=len(c),b:=len(c[0]),l:={},[l.setdefault((i,j),len(l))if v=='L'else(q:=[(0,i,j,0)],s:={(i,j,0):e})for i in range(a)for j in range(b)if(v:=c[i][j])in'LS'],0 if not l else next((m+1 for m,i,j,k in q for x,y in((i-1,j),(i+1,j),(i,j-1),(i,j+1))if 0<=x<a and 0<=y<b and(v:=c[x][y])!='X'and(t:=k|(1<<l[x,y]if v=='L'else 0))==t and(v=='L'and t==2**len(l)-1 or(n:=e if v=='R'else s[i,j,k]-1)>0 and s.get((x,y,t),0)<n and[s.update({(x,y,t):n}),q.append((m+1,x,y,t))]and 0)),-1)][-1]

class Solution:
    def minMoves(self, c: List[str], e: int) -> int:
        b=len(c[0]);g=''.join(c);l={};[v>'L'and(q:=[(0,n,0)],s:={(n,0):e})or l.setdefault(n,1<<len(l))for n,v in enumerate(g)if v in'LS'];return l and next((m+1 for m,n,k,*_ in q for x in(n-b,n+b,n-1,n+1)if-1<x<len(g)and(b==abs(x-n)or x//b==n//b)and(v:=g[x])<'X'and[t:=k|l.get(x,0)]and(t==2**len(l)-1 or(f:=v=='R'and e or s[n,k]-1)>0 and f>s.get((x,t),0)and q.append((m+1,x,t,s.update({(x,t):f}))))),-1)or 0

class Solution:
    def minMoves(self, c: List[str], e: int) -> int:
        b=-~len(c[0]);g='X'.join(c)+'X'*b;t=g.count('L');q=[(0,g.find('S'),0,e)];s={};return next((m for m,n,k,y in q for d in(b,-b,1,-1)if t==k.bit_count()or y*((v:=g[x:=n+d])<'X')and(f:=[y-1,e][v=='R'])>s.get(u:=(x,k|(v=='L')<<x),-1)and q.append(s.update({u:f})or(m+1,*u,f))),-1)

test('''
3568. Minimum Moves to Clean the Classroom
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

'S': Starting position of the student
'L': Litter that must be collected (once collected, the cell becomes empty)
'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
'X': Obstacle the student cannot pass through
'.': Empty space
You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

 

Example 1:

Input: classroom = ["S.", "XL"], energy = 2

Output: 2

Explanation:

The student starts at cell (0, 0) with 2 units of energy.
Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
A valid sequence of moves to collect all litter is as follows:
Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
The student collects all the litter using 2 moves. Thus, the output is 2.
Example 2:

Input: classroom = ["LS", "RL"], energy = 4

Output: 3

Explanation:

The student starts at cell (0, 1) with 4 units of energy.
A valid sequence of moves to collect all litter is as follows:
Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
The student collects all the litter using 3 moves. Thus, the output is 3.
Example 3:

Input: classroom = ["L.S", "RXL"], energy = 3

Output: -1

Explanation:

No valid path collects all 'L'.

Other examples:

Input: classroom = ["SR"], energy = 1
Output: 0

Constraints:

1 <= m == classroom.length <= 20
1 <= n == classroom[i].length <= 20
classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'
1 <= energy <= 50
There is exactly one 'S' in the grid.
There are at most 10 'L' cells in the grid.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
9,595/36K
Acceptance Rate
26.6%
Topics
Staff
Array
Hash Table
Bit Manipulation
Breadth-First Search
Matrix
Weekly Contest 452
icon
Companies
Hint 1
Use BFS with states (x, y, mask, e, steps), initializing with (sx, sy, 0, energy, 0), and for each move update e (–1 per step), update mask on 'L', reset e=energy on 'R', and return steps when mask == fullMask.
Hint 2
Maintain a 3D array bestEnergy[x][y][mask] storing the maximum e seen for each (x,y,mask) and skip any new state with e <= bestEnergy[x][y][mask] to prune.
''')
