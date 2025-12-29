from lc import *

# https://leetcode.com/problems/pyramid-transition-matrix/solutions/939885/python-8-lines-dfs-by-ggyc1993-u433/?envType=daily-question&envId=2025-12-29

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allow_map = defaultdict(list)
        for s in allowed: allow_map[s[0]+s[1]].append(s[2])
        def dfs(layer):
            if len(layer) == 2 and layer in allow_map: return True
            for l, r in zip(layer, layer[1:]):
                if l + r not in allow_map: return False
            return any(dfs(next_layer) for next_layer in list(map(lambda cand: "".join(cand), itertools.product(*[allow_map[l + r] for l, r in zip(layer, layer[1:])]))))
        return dfs(bottom)

# https://leetcode.com/problems/pyramid-transition-matrix/solutions/113038/python-solution-by-lee215-n6gd/?envType=daily-question&envId=2025-12-29

class Solution: # TLE
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        f = collections.defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed: f[a][b].append(c)
        def pyramid(bottom):
            return len(bottom) == 1 or any(pyramid(i) for i in product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))))
        return pyramid(bottom)

class Solution:
    def pyramidTransition(self,b:str,a:List[str])->bool:
        d={x+y:[z for u,v,z in a if u==x and v==y]for x in{s[0]for s in a}for y in{s[1]for s in a}};return(f:=cache(lambda s:1==len(s)or any(f(''.join(c))for c in product(*(d.get(x+y,[])for x,y in zip(s,s[1:]))))))(b)

class Solution:
    def pyramidTransition(self,b:str,a:List[str])->bool:
        d={};[d.setdefault(x,{}).setdefault(y,[]).append(z)for x,y,z in a];return(f:=cache(lambda s:1==len(s)or any(f(''.join(c))for c in product(*(d.get(x,{}).get(y,[])for x,y in zip(s,s[1:]))))))(b)

class Solution:
    def pyramidTransition(self, b: str, a: List[str]) -> bool:
        d=defaultdict;t=d(lambda:d(list));[t[x][y].append(z)for x,y,z in a];return(f:=cache(lambda s:1==len(s)or any(f(i)for i in product(*(t[x][y]for x,y in zip(s,s[1:]))))))(b)

test('''
756. Pyramid Transition Matrix
Medium
Topics
premium lock icon
Companies
You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.

To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.

For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.

Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.

 

Example 1:


Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
Output: true
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.
Example 2:


Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
Output: false
Explanation: The allowed triangular patterns are shown on the right.
Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.
 

Constraints:

2 <= bottom.length <= 6
0 <= allowed.length <= 216
allowed[i].length == 3
The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
All the values of allowed are unique.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
39,334/73.8K
Acceptance Rate
53.3%
Topics
Hash Table
String
Backtracking
Bit Manipulation
Weekly Contest 65
''')
