from lc import *

# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/solutions/7579030/brilliant-python3cpp-implementation-onq-vn85l/?envType=daily-question&envId=2026-10-29

class Solution:
    def palindromePath(self, n: int, es: list[list[int]], S: str, qs: list[str]) -> list[bool]:
        pa = [0] * n
        deg = [0] * n
        deg[0] = 2  # Set root degree to avoid it being treated as a leaf
        for a, b in es:
            pa[a] ^= b; pa[b] ^= a  # Store XOR sum of neighbors
            deg[a] += 1; deg[b] += 1

        siz = [1] * n
        ch = [-1] * n
        qu = [i for i in range(n) if deg[i] == 1]  # Start from leaves
        for i in qu:
            p = pa[i]  # Current XOR sum contains only the parent
            s = siz[i]
            siz[p] += s
            if (c := ch[p]) == -1 or s > siz[c]:
                ch[p] = i  # Identify heavy child
            pa[p] ^= i  # Remove child from parent's XOR sum to isolate grandparent/parent
            deg[p] -= 1
            if deg[p] == 1:
                qu.append(p)
        qu.append(0)

        top = [-1] * n
        dfn = [-1] * n
        l = [0] * n
        t = 0
        for i in reversed(qu):  # Top-down traversal to establish HLD
            if ~dfn[i]: continue
            tt = i
            while ~i:
                top[i] = tt
                l[t] = 1 << ord(S[i]) - 97  # Map character to bitmask
                dfn[i] = t
                t += 1
                i = ch[i]
        
        # O(n) BIT construction
        bit = [0] + l
        for i in range(1, n + 1):
            j = i + (i & -i)
            if j <= n: bit[j] ^= bit[i]

        ans = []
        for qq in qs:
            if qq.startswith("u"):  # Point update logic
                _, i, c = qq.split()
                i = int(i)
                x = dfn[i]
                v = (1 << ord(c) - 97)
                d = v ^ l[x]
                l[x] = v
                x += 1
                while x <= n:
                    bit[x] ^= d
                    x += x & -x
            else:  # Path query logic
                _, a, b = qq.split()
                a, b = int(a), int(b)
                res = 0
                while top[a] != top[b]:
                    if dfn[top[a]] < dfn[top[b]]:
                        a, b = b, a
                    s, t = dfn[top[a]], dfn[a] + 1
                    while t > s:  # Efficient range XOR query
                        res ^= bit[t]; t &= t - 1
                    while s > t:
                        res ^= bit[s]; s &= s - 1
                    a = pa[top[a]]
                if dfn[a] > dfn[b]:
                    a, b = b, a
                s, t = dfn[a], dfn[b] + 1
                while t > s:
                    res ^= bit[t]; t &= t - 1
                while s > t:
                    res ^= bit[s]; s &= s - 1
                ans.append(res & (res - 1) == 0)  # Check if at most one bit is set
        return ans

class Solution:
    def palindromePath(self, n: int, es: list[list[int]], S: str, qs: list[str]) -> list[bool]:
        g=[[]for _ in S];[g[a].append(b)or g[b].append(a)for a,b in es];s=[(0,0)];o=[*s]+[s.extend(([(v,-1)]+[(w,v)for w in g[v]if w-q])*(q>=0))or(v,q)for v,q in iter(lambda:s and s.pop(),[])];I={v^q>>99:t for t,(v,q)in enumerate(o)};A=[I[q]for v,q in o];m=[1<<ord(S[v])for v,q in o];k=0;P=[k:=k^v for v in m];B=[0]*len(m);T=[A];[T.append([*map(min,u:=T[-1],u[1<<len(T)-1:])])for _ in T if T[-1]];f=lambda x:x and B[x]^f(x&x-1);h=lambda u,d:u<len(B)and(setitem(B,u,B[u]^d)or h(u+(u&-u),d));return[a==b or(e:=P[a]^P[b]^f(a)^f(b)^m[min(T[j:=len(bin(b-a))-3][a+1],T[j][b+1-2**j])])&e-1<1for c,x,y in map(str.split,qs)if c<'u'or h(p:=I[i:=int(x)],d:=1<<ord(y)^m[p])or h(I[~i],d)or setitem(m,p,m[p]^d)for a,b in[sorted((I[int(x)],I[int(y)]))]]

class Solution:
    def palindromePath(self, n: int, e: list[list[int]], s: str, q: list[str]) -> list[bool]:
        g=[[]for _ in s];[g[a].append(b)or g[b].append(a)for a,b in e];t=[(0,0)];o=[*t]+[t.extend(([(v,-1)]+[(w,v)for w in g[v]if w-r])*(r>=0))or(v,r)for v,r in iter(lambda:t and t.pop(),[])];I={v^r>>99:z for z,(v,r)in enumerate(o)};A=[I[r]for v,r in o];m=[1<<ord(s[v])for v,r in o];k=0;P=[k:=k^v for v in m];B=[0]*len(m);T=[A];[T.append([*map(min,u:=T[-1],u[1<<len(T)-1:])])for _ in T if T[-1]];f=lambda x:x and B[x]^f(x&x-1);h=lambda u,d:u<len(B)and(setitem(B,u,B[u]^d)or h(u+(u&-u),d));return[a==b or(c:=P[a]^P[b]^f(a)^f(b)^m[min(T[j:=len(bin(b-a))-3][a+1],T[j][b+1-2**j])])&c-1<1for d,x,y in map(str.split,q)if d<'u'or h(p:=I[i:=int(x)],c:=1<<ord(y)^m[p])or h(I[~i],c)or setitem(m,p,m[p]^c)for a,b in[sorted((I[int(x)],I[int(y)]))]]

class Solution:
    def palindromePath(self, n: int, e: list[list[int]], s: str, q: list[str]) -> list[bool]:
        g=[[]for _ in s];[g[a].append(b)or g[b].append(a)for a,b in e];t=[0,(0,0)];o=[~r and t.extend([(v,-1)]+[(w,v)for w in g[v]if w-r])or(v,r)for v,r in iter(t.pop,0)];B=[0]*len(o);f=lambda x:x and B[x]^f(x&x-1);h=lambda u,d:u<len(B)and(setitem(B,u,B[u]^d)or h(u+(u&-u),d));I={v^r>>99:h(z,1<<ord(s[v]))or z for z,(v,r)in enumerate(o,1)};T=[[I[r]for v,r in o]];[T.append([*map(min,u,u[1<<len(T)-1:])])for u in T if u];return[(c:=f(a)^f(b)^f(k:=min(T[j:=len(bin(b-a))-3][a],T[j][b-2**j]))^f(k-1))&c-1<1for d,x,y in map(str.split,q)if d<'u'or h(p:=I[i:=int(x)],c:=1<<ord(y)^f(p)^f(p-1))or h(I[~i],c)for a,b in[sorted((I[int(x)],I[int(y)]))]]

test('''
3841. Palindromic Path Queries in a Tree
Hard
Topics
premium lock icon
Companies
Hint
You are given an undirected tree with n nodes labeled 0 to n - 1. This is represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi] indicates an undirected edge between nodes ui and vi.

You are also given a string s of length n consisting of lowercase English letters, where s[i] represents the character assigned to node i.

You are also given a string array queries, where each queries[i] is either:

"update ui c": Change the character at node ui to c. Formally, update s[ui] = c.
"query ui vi": Determine whether the string formed by the characters on the unique path from ui to vi (inclusive) can be rearranged into a palindrome.
Return a boolean array answer, where answer[j] is true if the jth query of type "query ui vi"​​​​​​​ can be rearranged into a palindrome, and false otherwise.

 

Example 1:

Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0 2","update 1 b","query 0 2"]

Output: [true,false]

Explanation:

"query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form "aca", a palindrome. Thus, answer[0] = true.
"update 1 b": Update node 1 to 'b', now s = "abc".
"query 0 2": Path characters are "abc", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
Thus, answer = [true, false].

Example 2:

Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1 2","update 0 b","query 2 3","update 3 a","query 1 3"]

Output: [false,false,true]

Explanation:

"query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form a palindrome. Thus, answer[0] = false.
"update 0 b": Update node 0 to 'b', now s = "bbca".
"query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form a palindrome. Thus, answer[1] = false.
"update 3 a": Update node 3 to 'a', s = "bbca".
"query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form "bab", a palindrome. Thus, answer[2] = true.
Thus, answer = [false, false, true].

 

Constraints:

1 <= n == s.length <= 5 * 104
edges.length == n - 1
edges[i] = [ui, vi]
0 <= ui, vi <= n - 1
s consists of lowercase English letters.
The input is generated such that edges represents a valid tree.
1 <= queries.length <= 5 * 104​​​​​​​
queries[i] = "update ui c" or
queries[i] = "query ui vi"
0 <= ui, vi <= n - 1
c is a lowercase English letter.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
4,430/12.6K
Acceptance Rate
35.2%
Topics
Principal
Array
String
Divide and Conquer
Bit Manipulation
Tree
Depth-First Search
Binary Indexed Tree
Segment Tree
Biweekly Contest 176
icon
Companies
Hint 1
Use heavy light decomposition to break each path query into O(log n) segments.
Hint 2
Represent characters as a 26-bit mask and maintain segment data with XOR. A path can form a palindrome if the resulting mask has at most one bit set.
''')
