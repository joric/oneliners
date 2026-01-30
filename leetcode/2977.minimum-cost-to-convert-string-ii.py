from lc import *

# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/solutions/4450555/simple-dijkstra-dp-python-3-by-layzerk-5135/

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        adj = defaultdict(lambda: defaultdict(int))
        change_lengths = set(len(sub) for sub in original)
        
        for i, start in enumerate(original):
            end = changed[i]
            c = cost[i]
            
            if end in adj[start]:
                adj[start][end] = min(adj[start][end], c)
            else:
                adj[start][end] = c
        
        
        @cache
        def dijkstra(start, end):
            heap = [(0, start)]
            costs = defaultdict(lambda: inf)
            costs[start] = 0
            while heap:
                path_cost, curr = heapq.heappop(heap)
                if curr == end:
                    return path_cost
                for nei in adj[curr]:
                    nei_cost = adj[curr][nei]
                    
                    new_cost = nei_cost + path_cost
                    
                    if new_cost < costs[nei]:
                        costs[nei] = new_cost
                        heapq.heappush(heap, (new_cost, nei))
            return inf
        

        @cache
        def dfs(i):
            #let dfs(i) be the cost of matching everything at i and onwards assuming everything before i is matched
            if i >= len(target):
                return 0
           
            c = inf if target[i] != source[i] else dfs(i+1) #if they match save default cost as just continue
            for length in change_lengths:
                t_sub = target[i:i+length]
                s_sub = source[i:i+length]
                trans_cost = dijkstra(s_sub, t_sub)

                if trans_cost != inf:
                    c = min(c, trans_cost + dfs(i+length))
            return c
        ans = dfs(0)
        return ans if ans != inf else -1

class Solution:
    def minimumCost(self, s: str, t: str, o: List[str], c: List[str], p: List[int]) -> int:
        return(z:=setitem,r:=range,f:=inf,u:={*o,*c},m:={x:i for i,x in enumerate(u)},n:=len(m),q:=r(n),w:=[[0 if i==j else f for j in q]for i in q],any(z(w[m[a]],m[b],min(w[m[a]][m[b]],e))for a,b,e in zip(o,c,p)),any(w[i][k]<f and any(w[k][j]<f and z(w[i],j,min(w[i][j],w[i][k]+w[k][j]))for j in q)for k in q for i in q),d:=[0]+[f]*(k:=len(s)),g:={len(x)for x in u},[d[i]<f and((i<k and s[i]==t[i]and z(d,i+1,min(d[i+1],d[i]))),[z(d,i+l,min(d[i+l],d[i]+w[x][y]))for l in g if i+l<=k and(x:=m.get(s[i:i+l],-1))>-1<(y:=m.get(t[i:i+l],-1))and w[x][y]<f])for i in r(k)])and(-1,d[k])[d[k]<f]

# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/solutions/4468594/easy-to-understand-bfs-dijkstra-by-delet-ihnt/

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        lookup = {a: {} for a in set(original)}
        
        def bfs(a):
            heap = [(0, a)]
            visited = set()
            while heap:
                curr_cost, b = heappop(heap)
                if b in visited:
                    continue
                visited.add(b)
                lookup[a][b] = curr_cost
                for c in graph[b]:
                    heappush(heap, (curr_cost + graph[b][c], c))
        
        graph = defaultdict(dict)
        for x, y, z in zip(original, changed, cost):
            if y not in graph[x]:
                graph[x][y] = z
            else:
                graph[x][y] = min(graph[x][y], z)

        for a in set(original):
            bfs(a)

        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            if source[i - 1] == target[i - 1]:
                dp[i] = dp[i - 1]

            for length in set(len(s) for s in original):
                if i >= length and (s := source[i - length:i]) in lookup and (t := target[i - length:i]) in lookup[s]:
                    dp[i] = min(dp[i], dp[i - length] + lookup[s][t])

        return dp[-1] if dp[-1] < float('inf') else -1

class Solution:
    def minimumCost(self, s: str, t: str, o: List[str], c: List[str], k: List[int]) -> int:
        e=setitem;g=defaultdict(dict);l={a:{}for a in o};n=len(s);d=[0]+[inf]*n;u={*map(len,o)};f=lambda a:(q:=lambda d,b,h=[],v=set():(b not in v and(v.add(b),setitem(l[a],b,d),[heappush(h,(d+g[b][x],x))for x in g[b]]),h and q(*heappop(h))))(0,a);[e(g[x],y,z if y not in g[x]else min(g[x][y],z))for x,y,z in zip(o,c,k)];[*map(f,{*o})];[(s[i-1]==t[i-1]and e(d,i,d[i-1]),[e(d,i,min(d[i],d[i-j]+l[x][y]))for j in u if i>=j and(x:=s[i-j:i])in l and(y:=t[i-j:i])in l[x]])for i in range(1,n+1)];return(-1,t:=d[-1])[inf>t]

# https://leetcode.com/problems/minimum-cost-to-convert-string-ii/solutions/4468594/easy-to-understand-bfs-dijkstra-by-delet-ihnt/

class Solution:
    def minimumCost(self, s: str, t: str, o: List[str], c: List[str], k: List[int]) -> int:
        l = {a: {} for a in set(o)}
        
        def f(a):
            h = [(0, a)]
            v = set()
            while h:
                d, b = heappop(h)
                if b in v:
                    continue
                v.add(b)
                l[a][b] = d
                for x in g[b]:
                    heappush(h, (d + g[b][x], x))
        
        g = defaultdict(dict)
        for x, y, z in zip(o, c, k):
            if y not in g[x]:
                g[x][y] = z
            else:
                g[x][y] = min(g[x][y], z)

        for a in set(o):
            f(a)

        n = len(s)
        d = [inf] * (n + 1)
        d[0] = 0

        u = set(len(x) for x in o)
        for i in range(1, n + 1):
            if s[i - 1] == t[i - 1]:
                d[i] = d[i - 1]

            for j in u:
                if i >= j and (x := s[i - j:i]) in l and (y := t[i - j:i]) in l[x]:
                    d[i] = min(d[i], d[i - j] + l[x][y])

        return d[-1] if d[-1] < inf else -1

class Solution:
    def minimumCost(self, s: str, t: str, o: List[str], c: List[str], k: List[int]) -> int:
        e=setitem;g=defaultdict(dict);l={};n=len(s);d=[0]+[inf]*n;u={*map(len,o)};[e(g[x],y,min(g[x].get(y,inf),z))for x,y,z in zip(o,c,k)];[(e(l,a,{}),(q:=lambda d,b,h=[]:(b in l[a]or(e(l[a],b,d),[heappush(h,(d+g[b][x],x))for x in g[b]]),h and q(*heappop(h))))(0,a))for a in o];[(s[i-1]==t[i-1]and e(d,i,d[i-1]),[e(d,i,min(d[i],d[i-j]+l[x][y]))for j in u if i>=j and(x:=s[i-j:i])in l and(y:=t[i-j:i])in l[x]])for i in range(1,n+1)];return(-1,t:=d[-1])[inf>t]

test('''
2977. Minimum Cost to Convert String II
Hard
Topics
premium lock icon
Companies
Hint
You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English characters. You are also given two 0-indexed string arrays original and changed, and an integer array cost, where cost[i] represents the cost of converting the string original[i] to the string changed[i].

You start with the string source. In one operation, you can pick a substring x from the string, and change it to y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y. You are allowed to do any number of operations, but any pair of operations must satisfy either of these two conditions:

The substrings picked in the operations are source[a..b] and source[c..d] with either b < c or d < a. In other words, the indices picked in both operations are disjoint.
The substrings picked in the operations are source[a..b] and source[c..d] with a == c and b == d. In other words, the indices picked in both operations are identical.
Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].

 

Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert "abcd" to "acbe", do the following operations:
- Change substring source[1..1] from "b" to "c" at a cost of 5.
- Change substring source[2..2] from "c" to "e" at a cost of 1.
- Change substring source[2..2] from "e" to "b" at a cost of 2.
- Change substring source[3..3] from "d" to "e" at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28. 
It can be shown that this is the minimum possible cost.
Example 2:

Input: source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]
Output: 9
Explanation: To convert "abcdefgh" to "acdeeghh", do the following operations:
- Change substring source[1..3] from "bcd" to "cde" at a cost of 1.
- Change substring source[5..7] from "fgh" to "thh" at a cost of 3. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation.
- Change substring source[5..7] from "thh" to "ghh" at a cost of 5. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
The total cost incurred is 1 + 3 + 5 = 9.
It can be shown that this is the minimum possible cost.
Example 3:

Input: source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"], cost = [100,1578]
Output: -1
Explanation: It is impossible to convert "abcdefgh" to "addddddd".
If you select substring source[1..3] as the first operation to change "abcdefgh" to "adddefgh", you cannot select substring source[3..7] as the second operation because it has a common index, 3, with the first operation.
If you select substring source[3..7] as the first operation to change "abcdefgh" to "abcddddd", you cannot select substring source[1..3] as the second operation because it has a common index, 3, with the first operation.
 

Constraints:

1 <= source.length == target.length <= 1000
source, target consist only of lowercase English characters.
1 <= cost.length == original.length == changed.length <= 100
1 <= original[i].length == changed[i].length <= source.length
original[i], changed[i] consist only of lowercase English characters.
original[i] != changed[i]
1 <= cost[i] <= 106
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
6,798/25.5K
Acceptance Rate
26.7%
Topics
Array
String
Dynamic Programming
Graph Theory
Trie
Shortest Path
Weekly Contest 377
icon
Companies
Hint 1
Give each unique string in original and changed arrays a unique id. There are at most 2 * m unique strings in total where m is the length of the arrays. We can put them into a hash map to assign ids.
Hint 2
We can pre-compute the smallest costs between all pairs of unique strings using Floyd Warshall algorithm in O(m ^ 3) time complexity.
Hint 3
Let dp[i] be the smallest cost to change the first i characters (prefix) of source into target, leaving the suffix untouched. We have dp[0] = 0. dp[i] = min(
dp[i - 1] if (source[i - 1] == target[i - 1]),
dp[j-1] + cost[x][y] where x is the id of source[j..(i - 1)] and y is the id of target e[j..(i - 1)])
). If neither of the two conditions is satisfied, dp[i] = infinity.
Hint 4
We can use Trie to check for the second condition in O(1).
Hint 5
The answer is dp[n] where n is source.length.
Similar Questions
Can Convert String in K Moves
Medium
Minimum Moves to Convert String
Easy
Minimum Number of Valid Strings to Form Target II
Hard
Minimum Number of Valid Strings to Form Target I
Medium
''')
