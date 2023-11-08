from lc import *

# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/discuss/4263761/Csebisev-disance-c

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return t!=1 if sx==fx and sy==fy else max(abs(sx-fx),abs(sy-fy))<=t

class Solution:
    def isReachableAtTime(self, a: int, b: int, c: int, d: int, t: int) -> bool:
        return t!=1 if a==c and b==d else max(abs(a-c),abs(b-d))<=t

# https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/discuss/4026074/Python-one-line

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        return max(abs(sx - fx), abs(sy - fy)) <= t if max(abs(sx - fx), abs(sy - fy)) else t != 1

class Solution:
    def isReachableAtTime(self, a: int, b: int, c: int, d: int, t: int) -> bool:
        return x<=t if(x:=max(abs(a-c),abs(b-d)))else t!=1

test('''
2849. Determine if a Cell Is Reachable at a Given Time
Medium

210

238

Add to List

Share
You are given four integers sx, sy, fx, fy, and a non-negative integer t.

In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.

Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.

 

Example 1:


Input: sx = 2, sy = 4, fx = 7, fy = 7, t = 6
Output: true
Explanation: Starting at cell (2, 4), we can reach cell (7, 7) in exactly 6 seconds by going through the cells depicted in the picture above. 
Example 2:


Input: sx = 3, sy = 1, fx = 7, fy = 3, t = 3
Output: false
Explanation: Starting at cell (3, 1), it takes at least 4 seconds to reach cell (7, 3) by going through the cells depicted in the picture above. Hence, we cannot reach cell (7, 3) at the third second.
 

Example 3:

Input: sx = 1, sy = 1, fx = 2, fy = 2, t = 1
Output: true

Constraints:

1 <= sx, sy, fx, fy <= 10^9
0 <= t <= 10^9
Accepted
27,212
Submissions
109,748
''')

