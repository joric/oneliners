from lc import *

# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/discuss/1149266/Python3-topological-sort/1265574

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topo_sort(nodes, edges):
            grid, inp = {k: [] for k in nodes}, collections.Counter({k: 0 for k in nodes})
            [grid[a].append(b) or inp.update({b: 1}) for a, b in edges if a in nodes and b in nodes]
            topo = [k for k, v in inp.items() if v <= 0]
            [inp.update({kid: -1}) or inp[kid] == 0 and topo.append(kid) for node in topo for kid in grid[node]]
            return topo if len(topo) == len(grid) else []
        group = [m + idx if grp == -1 else grp for idx, grp in enumerate(group)]
        edges_grp = set((group[before], grp) for grp, befores in zip(group, beforeItems) for before in befores if group[before] != grp)
        if len(topo1 := topo_sort(set(group), edges_grp)) != len(set(group)):
            return []
        edges_node = set((before, idx) for idx, befores in enumerate(beforeItems) for before in befores)
        if len(topo2 := topo_sort(set(range(n)), edges_node)) != n:
            return []
        a, b = {x: i for i, x in enumerate(topo1)}, {x: i for i, x in enumerate(topo2)}
        return sorted(range(n), key=lambda x: (a[group[x]], b[x]))

class Solution:
    def sortItems(self, n: int, m: int, g: List[int], s: List[List[int]]) -> List[int]:
        def f(o, e):
            r = {k:[] for k in o}
            p = Counter({k:0 for k in o})
            [r[a].append(b) or p.update({b:1}) for a,b in e if a in o and b in o]
            t = [k for k,v in p.items() if v<=0]
            [p.update({c:-1}) or p[c]==0 and t.append(c) for d in t for c in r[d]]
            return t if len(t)==len(r) else []
        g = [m+i if x==-1 else x for i,x in enumerate(g)]
        u = set((g[x],i) for i,j in zip(g,s) for x in j if g[x] != i)
        v = set((x,i) for i,j in enumerate(s) for x in j)
        a = {x:i for i,x in enumerate(f(set(g), u))}
        b = {x:i for i,x in enumerate(f(set(range(n)), v))}
        return sorted(range(n),key=lambda x:(a[g[x]], b[x])) if len(a)==len(set(g)) and len(b)==n else []

class Solution:
    def sortItems(self, n: int, m: int, g: List[int], s: List[List[int]]) -> List[int]:
        f=lambda o,e:(r:={k:[]for k in o},p:=Counter({k:0 for k in o}),[r[a].append(b)or p.update({b:1})for a,b in e if a in o and b in o],t:=[k for k,v in p.items() if v<=0],[p.update({c:-1})or p[c]==0 and t.append(c) for d in t for c in r[d]],t if len(t)==len(r)else[])[-1];(g:=[m+i if x==-1 else x for i,x in enumerate(g)],u:=set((g[x],i)for i,j in zip(g,s)for x in j if g[x]!=i),v:=set((x,i)for i,j in enumerate(s) for x in j),a:= {x:i for i,x in enumerate(f(set(g), u))},b:= {x:i for i,x in enumerate(f(set(range(n)),v))});return sorted(range(n),key=lambda x:(a[g[x]], b[x]))if len(a)==len(set(g))and len(b)==n else[]

test('''
1203. Sort Items by Groups Respecting Dependencies
Hard

941

140

Add to List

Share
There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

Return a sorted list of the items such that:

The items that belong to the same group are next to each other in the sorted list.
There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
Return any solution if there is more than one solution and return an empty list if there is no solution.

 

Example 1:



Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
Output: [6,3,4,1,5,2,0,7]
Example 2:

Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
Output: []
Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
 

Constraints:

1 <= m <= n <= 3 * 10^4
group.length == beforeItems.length == n
-1 <= group[i] <= m - 1
0 <= beforeItems[i].length <= n - 1
0 <= beforeItems[i][j] <= n - 1
i != beforeItems[i][j]
beforeItems[i] does not contain duplicates elements.
Accepted
21,078
Submissions
37,535
Seen this question in a real interview before?

Yes

No
Think of it as a graph problem.
We need to find a topological order on the dependency graph.
Build two graphs, one for the groups and another for the items.
''',check=lambda res,exp,*args:set(res)==set(exp))

