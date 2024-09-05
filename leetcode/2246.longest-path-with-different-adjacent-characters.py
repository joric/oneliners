from lc import *

# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/discuss/1958690/8-lines-Python-using-graphlib-TopologicalSorter

from graphlib import TopologicalSorter

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def lengths():
            downs = [[0] for _ in s]
            ts = TopologicalSorter(dict(enumerate(zip(parent))))
            for node in [*ts.static_order()][:0:-1]:
                yield 1 + sum(nlargest(2, downs[node]))
                if s[node] != s[parent[node]]:
                    downs[parent[node]].append(1 + max(downs[node]))
        return max(lengths())


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g = [[] for _ in range(len(s))]
        any(g[b].append(a) for a,b in enumerate(parent) if b>=0)
        def f(a,r=0):
            c = nlargest(2, [x[0] for b in g[a] if (x:=f(b,r),r:=x[1]) and s[a]!=s[b]])
            return max(c+[0])+1, max(r,sum(c)+1)
        return f(0)[1]


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        return (g:=[[] for _ in range(len(s))],[g[b].append(a) for a,b in enumerate(parent) if b>=0]) and (f:=lambda a,r:
        (max(c:=[0]+[x[0] for b in g[a] if (x:=f(b,r),r:=x[1]) and s[a]!=s[b]])+1,max(r,sum(c:=nlargest(2,c))+1)))(0,0)[1]


test('''

2246. Longest Path With Different Adjacent Characters
Hard

597

14

Add to List

Share
You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.

 

Example 1:


Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions. 
Example 2:


Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.
 

Example 3:

Input: parent = [-1,0,1], s = "aab"
Output: 2

Example 4:

Input: parent = [-1,17,37,80,9,16,12,78,63,8,29,30,71,16,5,80,62,14,71,41,9,13,31,80,36,18,66,62,62,39,5,56,80,27,71,37,69,36,28,47,78,28,21,78,17,39,7,71,39,22,58,66,66,54,27,56,78,9,27,9,78,40,63,36,75,63,27,50,10,0,11,80,24,5,42,47,18,69,36,25,27], s = "oozbypewdgpayutsufzpctovgkqrofjimkeckfzgvziqohymdtuppjcuytygjzlagiowhrfcjntjbbwru"
Output: 16

Constraints:

n == parent.length == s.length
1 <= n <= 10^5
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.

''')