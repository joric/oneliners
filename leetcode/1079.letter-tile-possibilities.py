from lc import *

# https://leetcode.com/problems/letter-tile-possibilities/solutions/321673/python-dfs-set/?envType=daily-question&envId=2025-02-17

class Solution:
    def numTilePossibilities(self, t: str) -> int:
        r = set()
        def f(p, t):
            if p:
                r.add(p)
            for i in range(len(t)):
                f(p+t[i],t[:i]+t[i+1:])
        f('', t)
        return len(r)

# https://leetcode.com/problems/letter-tile-possibilities/solutions/997076/1-line-python3/?envType=daily-question&envId=2025-02-17

class Solution:
    def numTilePossibilities(self, t: str) -> int:
        return len(functools.reduce(lambda pre, curr: pre|{d[:i]+curr+d[i:] for d in pre for i in range(len(d)+1)}, tiles,{''})) - 1

# https://leetcode.com/problems/letter-tile-possibilities/solutions/6432307/one-line-solution-using-itertools/?envType=daily-question&envId=2025-02-17

class Solution:
    def numTilePossibilities(self, t: str) -> int:
        return len({*chain(*map(permutations,[t]*len(t),range(1,len(t)+1)))})

class Solution:
    def numTilePossibilities(self, t: str) -> int:
        n=len(t);return len({*chain(*map(permutations,[t]*n,range(1,n+1)))})

class Solution:
    def numTilePossibilities(self, t: str) -> int:
        return len({x for i in range(len(t))for x in permutations(t,i+1)})

class Solution:
    def numTilePossibilities(self, t: str) -> int:
        return sum(len({*permutations(t,i+1)})for i in range(len(t)))

test('''
1079. Letter Tile Possibilities
Medium
Topics
Companies
Hint
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
147.6K
Submissions
185K
Acceptance Rate
79.8%
Topics
Hash Table
String
Backtracking
Counting
Companies
Hint 1
Try to build the string with a backtracking DFS by considering what you can put in every position.
''')
