from lc import *

# https://leetcode.com/problems/path-crossing/discuss/3960790/Easy-readable-solution-8-lines

class Solution:
    def isPathCrossing(self, p: str) -> bool:
        c,v=(0,0),{(0,0)}
        for d in p:
            c = (c[0],c[1]+1)if d=='N'else(c[0],c[1]-1)if d=='S'else(c[0]+1,c[1])if d=='E'else(c[0]-1,c[1])
            if c in v:
                return True
            v.add(c)
        return False

# https://leetcode.com/problems/path-crossing/discuss/4443771/WeSimple-Shorter-than-thought

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        track = list(zip(
            accumulate(path, lambda acc, r: acc + {'E':1, 'W': -1}.get(r, 0), initial=0),
            accumulate(path, lambda acc, r: acc + {'N':1, 'S': -1}.get(r, 0), initial=0)
        ))
        return len(track) != len(set(track))

# https://leetcode.com/problems/path-crossing/discuss/2819934/Simple-Python-oror-Understandable-and-Clean

class Solution:
    def isPathCrossing(self, p: str) -> bool:
        x,y,v=0,0,{(0,0)}
        for c in p:
            if c == 'N': y += 1
            elif c == 'E': x += 1
            elif c == 'S': y -= 1
            else: x -= 1
            if (x,y) in v:
                return True
            v.add((x,y))
        return False

class Solution:
    def isPathCrossing(self, p: str) -> bool:
        return len(p)>=len({0,*accumulate(map({'N':1j,'E':1,'S':-1j,'W':-1}.get,p))})

test('''
1496. Path Crossing
Easy

714

18

Add to List

Share
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

Example 1:


Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
Example 2:


Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
 

Example 3:
Input: path = "SS"
Output: false


Example 4:
Input: path = "NNSWWEWSSESSWENNW"
Output: true

Constraints:

1 <= path.length <= 10^4
path[i] is either 'N', 'S', 'E', or 'W'.
Accepted
54,116
Submissions
95,899
''')

