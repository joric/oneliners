from lc import *

# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/5705728/Python-12-line-answer

class Solution:
    def removeStones(self, s: List[List[int]]) -> int:
        w,v=0,set()
        def f(i,j):
            for r,c in s:
                if (r,c) not in v and (i==r or j==c):
                    v.add((r,c))
                    f(r,c)
        for r,c in s:
            if (r,c) not in v:
                f(r,c)
                w += 1
        return len(s)-w

class Solution:
    def removeStones(self, s: List[List[int]]) -> int:
        w,v=0,set();return len(s)-sum((r,c)not in v and(f:=lambda i,j:0!=[(r,c)not in v and(i==r or j==c)and(v.add((r,c))or f(r,c))for r,c in s])(r,c)for r,c in s)

# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/197668/Count-the-Number-of-Islands-O(N)

class Solution:
    def removeStones(self, s: List[List[int]]) -> int:
        u = {}
        def find(x):
            if x != u[x]:
                u[x] = find(u[x])
            return u[x]
        def union(x, y):
            u.setdefault(x, x)
            u.setdefault(y, y)
            u[find(x)] = find(y)
        for i, j in s:
            union(i, ~j)
        return len(s) - len({find(x) for x in u})

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if x != uf.setdefault(x, x):
                uf[x] = find(uf[x])
            return uf[x]
        for i, j in stones:
            uf[find(i)] = find(~j)
        return len(stones) - len({find(x) for x in uf})

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        return (uf:={},f:=lambda x: x!=uf.setdefault(x,x) and setitem(uf,x,f(uf[x])) or uf[x],
            any(setitem(uf,f(i),f(~j)) for i, j in stones)) and len(stones)-len({f(x) for x in uf})

# updated 2024-08-29

class Solution:
    def removeStones(self, s: List[List[int]]) -> int:
        u={};return(f:=lambda x:x!=u.setdefault(x,x)and setitem(u,x,f(u[x]))or u[x],any(setitem(u,f(i),f(~j)) for i,j in s))and len(s)-len({f(x) for x in u})

class Solution:
    def removeStones(self, s: List[List[int]]) -> int:
        u={};f=lambda x:x!=u.setdefault(x,x)and setitem(u,x,f(u[x]))or u[x];[setitem(u,f(i),f(~j))for i,j in s];return len(s)-len({*map(f,u)})

class Solution:
    def removeStones(self, s: List[List[int]]) -> int:
        u,e={},setitem;f=lambda x:x!=u.setdefault(x,x)and e(u,x,f(u[x]))or u[x];[e(u,f(i),f(~j))for i,j in s];return len(s)-len({*map(f,u)})

test('''
947. Most Stones Removed with Same Row or Column
Medium

3249

543

Add to List

Share
On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

 

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 10^4
No two stones are at the same coordinate point.

''')
