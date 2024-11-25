from lc import *

# https://leetcode.com/problems/sliding-puzzle/discuss/113613/C%2B%2B-9-lines-DFS-and-BFS

class Solution:
    def slidingPuzzle(self, b: List[List[int]]) -> int:
        m,v,d={0:(1,3),1:(0,2,4),2:(1,5),3:(0,4),4:(3,5,1),5:(4,2)},{},[inf]
        @cache
        def f(s, i, j, k):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            s = ''.join(s)
            if s == '123450':
                d[0] = min(d[0],k)
                return
            if k < d[0] and (s not in v or v[s]>k):
                v[s] = k
                for z in m[j]:
                    f(s, j, z, k + 1)
        s=''.join(map(str,sum(b,[])))
        i=s.find('0')
        f(s, i, i, 0)
        return(-1,d[0])[d[0]<inf]

class Solution:
    def slidingPuzzle(self, b: List[List[int]]) -> int:
        v={}
        @cache
        def f(s,i,j,k,r):
            s = ''.join(s[{i:j,j:i}.get(k,k)] for k in range(len(s)))
            if s=='123450':
                return k
            if k<r and k<v.get(s,inf):
                v[k] = k
                return min(f(s,j,z,k+1,r)for z in{0:(1,3),1:(0,2,4),2:(1,5),3:(0,4),4:(3,5,1),5:(4,2)}[j])
            return r
        s = ''.join(map(str,sum(b,[])))
        i = s.find(0)
        t = f(s,i,i,0,inf)
        return t if t<inf else t

class Solution:
    def slidingPuzzle(self, b: List[List[int]]) -> int:
        v,f={},cache(lambda s,i,j,k,r:k if(s:=''.join(s[{i:j,j:i}.get(k,k)]for k in range(len(s))))=='123450'else min(f(s,j,z,k+1,r)for z in{0:(1,3),1:(0,2,4),2:(1,5),3:(0,4),4:(3,5,1),5:(4,2)}[j])if k<r and k<v.get(s,inf)and[setitem(v,s,k)]else r);return(-1,t:=f(s:=''.join(map(str,sum(b,[]))),i:=s.find('0'),i,0,inf))[t<inf]

test('''
773. Sliding Puzzle
Hard

2054

52

Add to List

Share
On an 2 x 3 board, there are five tiles labeled from 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.

The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].

Given the puzzle board board, return the least number of moves required so that the state of the board is solved. If it is impossible for the state of the board to be solved, return -1.

 

Example 1:


Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.
Example 2:


Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.
Example 3:


Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.
An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]
 

Other examples:

Input: board = [[1,2,3],[4,5,0]]
Output: 0

Constraints:

board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
Each value board[i][j] is unique.
Accepted
99,622
Submissions
152,506
''')
