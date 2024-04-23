from lc import *

# https://leetcode.com/problems/minimum-height-trees/discuss/3397763/Python-Simple-and-Clean-beats-99.89

class Solution:
    def findMinHeightTrees(self, n: int, e: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        g = defaultdict(set)
        for i,j in e:
            g[i].add(j)
            g[j].add(i)
        q = deque(i for i in range(n)if len(g[i])==1)
        while n>2:
            c = len(q)
            n -= c
            for i in range(c):
                u = q.popleft()
                v = g[u].pop()
                g[v].remove(u)
                if len(g[v])==1:
                    q.append(v)
        return q

class Solution:
    def findMinHeightTrees(self, n: int, e: List[List[int]]) -> List[int]:
        g=defaultdict(set);[g[i].add(j)or g[j].add(i)for i,j in e];q=deque(i for i in range(n)if len(g[i])==1);return n==1 and[0]or next(q for _ in e if not(n>2 and(c:=len(q),n:=n-c,[g[v:=g[u:=q.popleft()].pop()].remove(u)or len(g[v])==1 and q.append(v)for i in range(c)])))

test('''
310. Minimum Height Trees
Medium

7470

328

Add to List

Share
A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
 

Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
Accepted
290,803
Submissions
747,709
''')
