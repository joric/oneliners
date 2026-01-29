from lc import *

# https://leetcode.com/problems/minimum-cost-to-convert-string-i/discuss/4449571/Python-Dijkstra

class Solution:
    def minimumCost(self, s: str, t: str, o: List[str], c: List[str], p: List[int]) -> int:
        def f(g,s):
            d = defaultdict(lambda: inf)
            d[s] = 0
            q = [(0, s)]
            while q:
                p,v = heappop(q)
                if p==d[v]:
                    for w,e in g[v]:
                        if e+p<d[w]:
                            d[w] = e+p
                            heappush(q,(e+p,w))
            return d
        n,m,g = len(o),len(s),defaultdict(list)
        [g[o[i]].append((c[i],p[i]))for i in range(n)]
        d={(a:=chr(i+ord('a'))):f(g,a)for i in range(27)}
        return (-1,r:=sum(d[s[i]][t[i]]for i in range(m)))[r<inf]

class Solution:
    def minimumCost(self, s: str, t: str, o: List[str], c: List[str], p: List[int]) -> int:
        (h:=defaultdict,f:=lambda g,s:(d:=h(lambda:inf),d.update({s:0}),q:=[],(z:=lambda p,v:(p==d[v]and[e+p<d[w]and setitem(d,w,e+p)==heappush(q,(e+p,w))for w,e in g[v]],q and z(*heappop(q))))(0,s))and d,n:=len(o),m:=len(s),g:=h(list),[g[o[i]].append((c[i],p[i]))for i in range(n)],d:={(a:=chr(i+ord('a'))):f(g,a)for i in range(27)});return(-1,r:=sum(d[s[i]][t[i]]for i in range(m)))[r<inf]

class Solution:
    def minimumCost(self, s: str, t: str, o: List[str], c: List[str], p: List[int]) -> int:
        d=defaultdict(lambda:inf);e=setitem;r={*o,*c,*s,*t};[e(d,u+v,min(d[u+v],w))for u,v,w in zip(o,c,p)];[e(d,k+k,0)or[e(d,i+j,min(d[i+j],d[i+k]+d[k+j]))for i in r for j in r]for k in r];return(-1,t:=sum(d[u+v]for u,v in zip(s,t)))[t<inf]

test('''
2976. Minimum Cost to Convert String I
Medium

278

14

Add to List

Share
You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 

Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.
Example 2:

Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.
Example 3:

Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.
 

Constraints:

1 <= source.length == target.length <= 105
source, target consist of lowercase English letters.
1 <= cost.length == original.length == changed.length <= 2000
original[i], changed[i] are lowercase English letters.
1 <= cost[i] <= 106
original[i] != changed[i]
Accepted
15,204
Submissions
37,782
''')