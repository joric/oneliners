from lc import *

# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/discuss/1149266/Python3-topological-sort/1265574

class Solution:
    def sortItems(self, n: int, m: int, g: List[int], b: List[List[int]]) -> List[int]:
        p,u,q,v = {},[0]*(m+n),{},[0]*n

        for i in range(n):
            if g[i]==-1:
                g[i] = i+m

        for i, x in enumerate(b):
            for j in x: 
                if g[j]!=g[i]: 
                    p.setdefault(g[j],[]).append(g[i])
                    u[g[i]] += 1
                q.setdefault(j,[]).append(i)
                v[i] += 1

        def f(g,d):
            r = []
            s = [k for k in range(len(d)) if d[k]==0]
            while s: 
                n = s.pop()
                r.append(n)
                for i in g.get(n, []):
                    d[i] -= 1
                    if d[i] == 0:
                        s.append(i)
            return r

        a = {x:i for i,x in enumerate(f(p,u))}
        b = {x:i for i,x in enumerate(f(q,v))}
        return len(a)==len(u) and len(b)==len(v) and sorted(range(n),key=lambda x:(a[g[x]],b[x])) or []

class Solution:
    def sortItems(self, n: int, m: int, g: List[int], b: List[List[int]]) -> List[int]:
        p,u,q,v = {},[0]*(m+n),{},[0]*n
        [g[i]==-1 and setitem(g,i,i+m)for i in range(n)]
        [(g[j]!=g[i] and (p.setdefault(g[j],[]).append(g[i]),setitem(u,g[i],u[g[i]]+1)),q.setdefault(j,[]).append(i),setitem(v,i,v[i]+1))for i,x in enumerate(b)for j in x]
        f=lambda g,d:next((r for _ in count() if not(q and(n:=q.pop(),r.append(n),[(setitem(d,i,d[i]-1),d[i]==0 and q.append(i))for i in g.get(n,[])]))),(r:=[],q:=[k for k in range(len(d)) if d[k]==0]))
        a={x:i for i,x in enumerate(f(p,u))}
        b={x:i for i,x in enumerate(f(q,v))}
        return len(a)==len(u) and len(b)==len(v) and sorted(range(n),key=lambda x:(a[g[x]],b[x])) or []

class Solution:
    def sortItems(self, n: int, m: int, g: List[int], b: List[List[int]]) -> List[int]:
        p,u,q,v={},[0]*(m+n),{},[0]*n;[g[i]==-1 and setitem(g,i,i+m)for i in range(n)];[(g[j]!=g[i] and (p.setdefault(g[j],[]).append(g[i]),setitem(u,g[i],u[g[i]]+1)),q.setdefault(j,[]).append(i),setitem(v,i,v[i]+1))for i,x in enumerate(b)for j in x];f=lambda g,d:next((r for _ in count() if not(q and(n:=q.pop(),r.append(n),[(setitem(d,i,d[i]-1),d[i]==0 and q.append(i))for i in g.get(n,[])]))),(r:=[],q:=[k for k in range(len(d)) if d[k]==0]));a={x:i for i,x in enumerate(f(p,u))};b={x:i for i,x in enumerate(f(q,v))};return len(a)==len(u) and len(b)==len(v) and sorted(range(n),key=lambda x:(a[g[x]],b[x]))or[]

# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/discuss/1149266/Python3-topological-sort/1265574

class Solution:
    def sortItems(self, n: int, m: int, g: List[int], s: List[List[int]]) -> List[int]:
        def f(o,e):
            r = {k:[] for k in o}
            c = Counter({k:0 for k in o})
            [r[a].append(b) or c.update({b:1}) for a,b in e if a in o and b in o]
            t = [k for k,v in c.items() if v<=0]
            [c.update({k:-1}) or c[k]==0 and t.append(k) for d in t for k in r[d]]
            return t if len(t)==len(r) else []
        g = [m+i if x==-1 else x for i,x in enumerate(g)]
        u = {(g[x],i) for i,j in zip(g,s) for x in j if g[x]!=i}
        v = {(x,i) for i,j in enumerate(s) for x in j}
        a = {x:i for i,x in enumerate(f({*g}, u))}
        b = {x:i for i,x in enumerate(f({*range(n)}, v))}
        return len(a)==len({*g}) and len(b)==n and sorted(range(n),key=lambda x:(a[g[x]], b[x])) or []

class Solution:
    def sortItems(self, n: int, m: int, g: List[int], s: List[List[int]]) -> List[int]:
        w,f=enumerate,lambda o,e:(r:={k:[]for k in o},c:=Counter({k:0 for k in o}),[r[a].append(b)or c.update({b:1})for a,b in e if a in o and b in o],t:=[k for k,v in c.items()if v<=0],[c.update({k:-1})or c[k]==0 and t.append(k)for d in t for k in r[d]],t if len(t)==len(r)else[])[-1];(g:=[m+i if x==-1 else x for i,x in w(g)],u:={(g[x],i)for i,j in zip(g,s)for x in j if g[x]!=i},v:={(x,i)for i,j in w(s)for x in j},a:={x:i for i,x in w(f({*g}, u))},b:={x:i for i,x in w(f({*range(n)},v))});return len(a)==len({*g})and len(b)==n and sorted(range(n),key=lambda x:(a[g[x]], b[x]))or[]

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

