from lc import *

# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/discuss/1043042/Simple-Python-DFS

class Solution:
    def restoreArray(self, p: List[List[int]]) -> List[int]:
        g,s,r = defaultdict(list),set(),[]
        for u,v in p:
            g[u].append(v)
            g[v].append(u)
        def f(u):
            r.append(u)
            s.add(u)
            for v in g[u]:
                if not v in s:
                    f(v)
        f(next(x for x in g if len(g[x])==1))
        return r

class Solution:
    def restoreArray(self, p: List[List[int]]) -> List[int]:
        g,s,r=defaultdict(list),set(),[];[(g[u].append(v),g[v].append(u))for u,v in p];(f:=lambda u:(r.append(u),s.add(u),[f(v)for v in g[u]if v not in s]))(next(x for x in g if len(g[x])==1));return r

class Solution:
    def restoreArray(self, p: List[List[int]]) -> List[int]:
        g,s,r=defaultdict(list),set(),[];[(g[u].append(v),g[v].append(u))for u,v in p];(f:=lambda u:u not in s and(r.append(u),s.add(u),[*map(f,g[u])]))(next(x for x in g if len(g[x])==1));return r

test('''
1743. Restore the Array From Adjacent Pairs
Medium

1079

33

Add to List

Share
There is an integer array nums that consists of n unique elements, but you have forgotten it. However, you do remember every pair of adjacent elements in nums.

You are given a 2D integer array adjacentPairs of size n - 1 where each adjacentPairs[i] = [ui, vi] indicates that the elements ui and vi are adjacent in nums.

It is guaranteed that every adjacent pair of elements nums[i] and nums[i+1] will exist in adjacentPairs, either as [nums[i], nums[i+1]] or [nums[i+1], nums[i]]. The pairs can appear in any order.

Return the original array nums. If there are multiple solutions, return any of them.

 

Example 1:

Input: adjacentPairs = [[2,1],[3,4],[3,2]]
Output: [1,2,3,4]
Explanation: This array has all its adjacent pairs in adjacentPairs.
Notice that adjacentPairs[i] may not be in left-to-right order.
Example 2:

Input: adjacentPairs = [[4,-2],[1,4],[-3,1]]
Output: [-2,4,1,-3]
Explanation: There can be negative numbers.
Another solution is [-3,1,4,-2], which would also be accepted.
Example 3:

Input: adjacentPairs = [[100000,-100000]]
Output: [100000,-100000]
 

Constraints:

nums.length == n
adjacentPairs.length == n - 1
adjacentPairs[i].length == 2
2 <= n <= 10^5
-10^5 <= nums[i], ui, vi <= 10^5
There exists some nums that has adjacentPairs as its pairs.
Accepted
43,725
Submissions
62,420
''')

