from lc import *

# https://leetcode.com/problems/find-subtree-sizes-after-changes/solutions/6008328/one-dfs-fast-by-vokasik-869x/?envType=daily-question&envId=2026-11-21

class Solution:
    def findSubtreeSizes(self, p: List[int], s: str) -> List[int]:
        n = len(s)
        s = [ord(c)-97 for c in s]
        d = defaultdict(list)
        for u in range(1,n):
            d[p[u]].append(u)
        r = [1] * n
        a = [-1] * 26
        def f(u):
            t = a[s[u]]
            a[s[u]] = u
            for v in d[u]:
                f(v)
                if a[s[v]] == -1:
                    r[u] += r[v]
                else:
                    r[a[s[v]]] += r[v]
            a[s[u]] = t
        f(0)
        return r

class Solution: # TLE
    def findSubtreeSizes(self, p: List[int], s: str) -> List[int]:
        d=defaultdict(list);k=[[1]for _ in s];[d[p].append(i)for i,p in enumerate(p)];f=lambda v:((l:=d[s[v]]).append(k[v]),[[k[v],*d[s[w]]][-1].append(f(w))for w in d[v]],sum(l.pop()))[2];f(0);return[*map(sum,k)]

# https://leetcode.com/problems/find-subtree-sizes-after-changes/solutions/5971273/python-simple-dfs-by-rnotappl-882u/?envType=daily-question&envId=2026-11-21

class Solution:
    def findSubtreeSizes(self, p: List[int], s: str) -> List[int]:
        n = len(p)
        a = [1]*n
        g = defaultdict(list)
        def f(u):
            c = s[u]
            o = p[u]
            while u:
                u = p[u]
                if s[u] == c:
                    return u
            return o
        d = [f(i) for i in range(n)]
        for i in range(n):
            if d[i] != -1:
                g[d[i]].append(i)
        def t(u):
            if u is None:
                return
            for v in g[u]:
                t(v)
                a[u] += a[v]
        t(0)
        return a

class Solution:
    def findSubtreeSizes(self, p: List[int], s: str) -> List[int]:
        return (n:=len(s),g:=[[]for _ in s],[(g[x].append(i))for i,x in enumerate(p)if i],r:=[1]*n,a:=[-1]*26,f:=lambda u:(c:=ord(s[u])-97,t:=a[c],a.__setitem__(c,u),[f(v)for v in g[u]],r.__setitem__(t if t>=0 else p[u],r[t if t>=0 else p[u]]+r[u])if t>=0 or p[u]>=0 else 0,a.__setitem__(c,t)),f(0),r)[-1]

class Solution:
    def findSubtreeSizes(self, p: List[int], s: str) -> List[int]:
        m=setitem;return (n:=len(s),g:=[[]for _ in s],[(g[x].append(i))for i,x in enumerate(p)if i],r:=[1]*n,a:=[-1]*26,f:=lambda u:(c:=ord(s[u])-97,t:=a[c],m(a,c,u),[f(v)for v in g[u]],m(r,t if t>=0 else p[u],r[t if t>=0 else p[u]]+r[u])if t>=0 or p[u]>=0 else 0,m(a,c,t)),f(0),r)[-1]

class Solution:
    def findSubtreeSizes(self, p: List[int], s: str) -> List[int]:
        m=setitem;n=len(s);g=[[]for _ in s];[g[x].append(i)for i,x in enumerate(p)if i];r=[1]*n;a=[-1]*26;f=lambda u:(c:=ord(s[u])-97,t:=a[c],m(a,c,u),[f(v)for v in g[u]],m(r,t if t>=0 else p[u],r[t if t>=0 else p[u]]+r[u])if u else 0,m(a,c,t));f(0);return r

test('''
3331. Find Subtree Sizes After Changes
Medium
Topics
premium lock icon
Companies
Hint
You are given a tree rooted at node 0 that consists of n nodes numbered from 0 to n - 1. The tree is represented by an array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

We make the following changes on the tree one time simultaneously for all nodes x from 1 to n - 1:

Find the closest node y to node x such that y is an ancestor of x, and s[x] == s[y].
If node y does not exist, do nothing.
Otherwise, remove the edge between x and its current parent and make node y the new parent of x by adding an edge between them.
Return an array answer of size n where answer[i] is the size of the subtree rooted at node i in the final tree.

 

Example 1:

Input: parent = [-1,0,0,1,1,1], s = "abaabc"

Output: [6,3,1,1,1,1]

Explanation:


The parent of node 3 will change from node 1 to node 0.

Example 2:

Input: parent = [-1,0,4,0,1], s = "abbba"

Output: [5,2,1,1,1]

Explanation:


The following changes will happen at the same time:

The parent of node 4 will change from node 1 to node 0.
The parent of node 2 will change from node 4 to node 1.
 

Constraints:

n == parent.length == s.length
1 <= n <= 105
0 <= parent[i] <= n - 1 for all i >= 1.
parent[0] == -1
parent represents a valid tree.
s consists only of lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
17,526/33.1K
Acceptance Rate
52.9%
Topics
Staff
Array
Hash Table
String
Tree
Depth-First Search
Biweekly Contest 142
icon
Companies
Hint 1
Perform a depth-first search on the tree, starting from the root.
Hint 2
During the DFS, keep track of the most recent node where each character from 'a' to 'z' has been seen.
''')
