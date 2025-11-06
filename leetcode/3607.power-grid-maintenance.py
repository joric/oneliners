from lc import *

# https://leetcode.com/problems/power-grid-maintenance/solutions/7187225/unionfind-sortedlist-by-viniusck-0r2x/

# TODO

from sortedcontainers import SortedList

class UnionFind:
    """UnionFind."""

    def __init__(self, size: int) -> None:
        """Constructor of UnionFind."""
        self.parents = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, i: int) -> int:
        if self.parents[i] == i:
            return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i: int, j: int) -> None:
        pi = self.find(i)
        pj = self.find(j)
        if pi == pj:
            return
        pi_rank, pj_rank = self.rank[pi], self.rank[pj]
        if pi_rank < pj_rank:
            self.parents[pi] = pj
            self.rank[pi] += 1
        else:
            self.parents[pj] = pi
            self.rank[pj] += 1

    def __repr__(self) -> str:
        return f"UnionFind(parents={self.parents}, rank={self.rank})"


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        connections.sort()
        ans = []
        uf = UnionFind(c)
        for u, v in connections:
            u, v = u - 1, v - 1
            uf.union(u, v)
        for u, v in connections:
            u, v = u - 1, v - 1
            uf.find(u)
            uf.find(v)
        par_sets = defaultdict(SortedList)
        for v, p in enumerate(uf.parents):
            par_sets[p].add(v)
        for u, v in queries:
            v = v - 1
            cur_list = par_sets[uf.parents[v]]
            if u == 1:
                try:
                    if v in cur_list:
                        ans.append(v + 1)
                    else:
                        ans.append(cur_list[0] + 1)
                except (IndexError, KeyError):
                    ans.append(-1)
            elif u == 2:
                cur_list.discard(v)
        return ans

# a-la unicode find

class Solution:
    def processQueries(self, n: int, c: List[List[int]], q: List[List[int]]) -> List[int]:
        c.sort()
        p = list(range(n))
        f = lambda i: i if p[i] == i else f(setitem(p, i, f(p[i])) or p[i])
        for u, v in c:
            u, v = u - 1, v - 1
            x, y = f(u), f(v)
            x != y and setitem(p, x, y)
        s = defaultdict(SortedList)
        [s[f(i)].add(i)for i in range(n)]
        a = []
        for x, v in q:
            v -= 1
            l = s[f(v)]
            if x == 1:
                a.append((v if v in l else l[0]) + 1 if l else -1)
            else:
                l.discard(v)
        return a

class Solution:
    def processQueries(self, n: int, c: List[List[int]], q: List[List[int]]) -> List[int]:
        c.sort()
        p=[*range(n)]
        f=lambda i:i if p[i]==i else f(setitem(p,i,f(p[i]))or p[i])
        [setitem(p,*t)for u,v in c if not eq(*(t:=[*map(f,(u-1,v-1))]))]
        s = defaultdict(SortedList)
        [s[f(i)].add(i)for i in range(n)]
        a = []
        [(t:=s[f(v:=y-1)],a.append((v if v in t else t[0])+1 if t else -1)if x==1 else t.discard(v))for x,y in q]
        return a

class Solution:
    def processQueries(self, n: int, c: List[List[int]], q: List[List[int]]) -> List[int]:
        c.sort();p,s,a=[*range(n)],defaultdict(SortedList),[];f=lambda i:i if p[i]==i else f(setitem(p,i,f(p[i]))or p[i]);[setitem(p,*t)for u,v in c if not eq(*(t:=[*map(f,(u-1,v-1))]))];[s[f(i)].add(i)for i in range(n)];[(t:=s[f(v:=y-1)],a.append((v if v in t else t[0])+1 if t else -1)if x==1 else t.discard(v))for x,y in q];return a

test('''
3607. Power Grid Maintenance
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).

These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.

Initially, all stations are online (operational).

You are also given a 2D array queries, where each query is one of the following two types:

[1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.

[2, x]: Station x goes offline (i.e., it becomes non-operational).

Return an array of integers representing the results of each query of type [1, x] in the order they appear.

Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.

 

Example 1:

Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

Output: [3,2,3]

Explanation:



Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.
Example 2:

Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]

Output: [1,-1]

Explanation:

There are no connections, so each station is its own isolated grid.
Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
Query [2,1]: Station 1 goes offline.
Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1.
 

Constraints:

1 <= c <= 105
0 <= n == connections.length <= min(105, c * (c - 1) / 2)
connections[i].length == 2
1 <= ui, vi <= c
ui != vi
1 <= queries.length <= 2 * 105
queries[i].length == 2
queries[i][0] is either 1 or 2.
1 <= queries[i][1] <= c
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
19,787/44.3K
Acceptance Rate
44.7%
Topics
Array
Hash Table
Depth-First Search
Breadth-First Search
Union Find
Graph
Heap (Priority Queue)
Ordered Set
Weekly Contest 457
icon
Companies
Hint 1
Use DFS or BFS to assign each station a component ID
Hint 2
For each component, maintain a sorted set of online station IDs
Hint 3
For query [2, x], remove x from the set of its component
Hint 4
For query [1, x], if x is in its component’s set return x; otherwise if the set is non-empty return its smallest element; else return -1
Hint 5
Precompute all components and then handle each query in O(log n) time using the sorted sets
''')
