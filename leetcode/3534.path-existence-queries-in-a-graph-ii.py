from lc import *

# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/solutions/6695182/python-10-lines-binary-jumping-by-dsapel-ny14/

class Solution: # TLE
    def pathExistenceQueries(self, n: int, v: List[int], m: int, q: List[List[int]]) -> List[int]:
        v=sorted((n,i)for i,n in enumerate(v))
        d={i:j for j,(n,i)in enumerate(v)}
        f=cache(lambda a,b:a<b and(-inf if(t:=bisect_right(v,v[a][0]+m,key =lambda x:x[0],lo=a+1)-1)==a else 1+f(t,b))or 0)
        return[(-1,r:=f(*sorted((d[a],d[b]))))[f.cache_clear()or r>-inf]for a,b in q]

# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        # Sort the nums and convert the indices
        idx = sorted(range(n), key=nums.__getitem__)
        mapping = {j:i for i,j in enumerate(idx)}
        
        # Find the furthest step to the left for each node
        ptr, prv = 0, []
        for j in idx:
            while nums[j] - nums[idx[ptr]] > maxDiff:
                ptr += 1
            prv.append(ptr)
        
        # Build the trees with the reversing pointers from the previous step, and collect the roots
        rts, conn = [], [[] for _ in range(n)]
        for i,p in enumerate(prv):
            if i == p:
                rts.append(i)
            else:
                conn[p].append(i)
            
        # DFS, collect the root, level and post-order number of each node
        def dfs(node: int):
            parent = prv[node]
            root[node] = root[parent]
            level[node] = level[parent] + 1
            order[node] = order[parent]
            for nxt in conn[node]:
                dfs(nxt)
            order[parent] = order[node] + 1
            
        root, level, order = list(range(n)), [0] * n, [0] * n
        for i in rts:
            dfs(i)
                
        # Online, O(1) per query
        ans = []
        for u,v in queries:
            u,v = mapping[u], mapping[v]
            if root[u] != root[v]:
                # Not in the same tree
                ans.append(-1)
            else:
                if u < v:
                    u,v = v,u
                # Get the level difference as their distance
                ans.append(level[u] - level[v] + (order[u] > order[v]))
                
        return ans

# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/solutions/6690608/binary-jumping-by-harkness-ph3y/

inf = float('inf')
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        vi = sorted([(v, i) for i, v in enumerate(nums)])
        n2i = {t[1]: i for i, t in enumerate(vi)}
        vals = [t[0] for t in vi]

        h = len(bin(n)[2:]) + 1
        jumps = [[-1] * h for _ in range(n)]
        j = 0
        for i in range(n):
            while j+1 < n and vals[j+1] - vals[i] <= maxDiff:
                j += 1
            jumps[i][0] = j
        for j in range(1, h):
            for i in range(n):
                jumps[i][j] = jumps[jumps[i][j-1]][j-1]
        
        def query(a, b, h):
            if a == b:
                return 0
            if jumps[a][0] >= b:
                return 1
            if jumps[a][h] < b:
                return inf 
            for j in range(h, -1, -1):
                if jumps[a][j] < b:
                    break
            return (1 << j) + query(jumps[a][j], b, j)
            
        
        res = []
        for a, b in queries:
            a, b = n2i[a], n2i[b]
            cur = query(min(a, b), max(a, b), h-1)
            res.append(cur if cur < inf else -1)
        return res

# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/submissions/2060762529/

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sortedIdx = sorted(range(n), key = lambda i:nums[i])
        idxMap = {}
        for newIdx, origIdx in enumerate(sortedIdx):
            idxMap[origIdx] = newIdx
        nums.sort()
        maxReach = [-1] * n
        j = 0
        for i in range(n):
            while j < n and abs(nums[i] - nums[j]) <= maxDiff:
                j += 1
            maxReach[i] = j - 1
        LOG = max(1, (n - 1).bit_length())

        A = [[-1] * LOG for _ in range(n)]
        for i in range(n):
            A[i][0] = maxReach[i]
        for k in range(1, LOG):
            for i in range(n):
                A[i][k] = A[A[i][k - 1]][k - 1]
        def minJumps(a, b):
            if a >= b:
                return 0
            ans = 0
            cur = a
            for k in range(LOG - 1, -1, -1):
                if A[cur][k] < b:
                    cur = A[cur][k]
                    ans += 2 ** k
            return ans + 1 if maxReach[cur] >= b else -1
        res= []
        for u, v in queries:
            a, b = idxMap[u], idxMap[v]
            a, b = min(a, b), max(a, b)
            res.append(minJumps(a, b))
        return res

# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/submissions/2060765786/

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        arr = sorted((v, i) for i, v in enumerate(nums))
        vals = [v for v, _ in arr]
        pos = [0] * n
        for i, (_, j) in enumerate(arr):
            pos[j] = i

        comp = [0] * n
        for i in range(1, n):
            comp[i] = comp[i - 1] + (vals[i] - vals[i - 1] > maxDiff)

        nxt = [0] * n
        j = 0
        for i in range(n):
            while j < n and vals[j] <= vals[i] + maxDiff:
                j += 1
            nxt[i] = j - 1

        logn = (n - 1).bit_length()
        jump = [nxt]
        for k in range(1, logn):
            pre = jump[k - 1]
            cur = [0] * n
            for i in range(n):
                cur[i] = pre[pre[i]]
            jump.append(cur)

        out = []
        for u, v in queries:
            pu, pv = pos[u], pos[v]
            if comp[pu] != comp[pv]:
                out.append(-1)
            elif pu == pv:
                out.append(0)
            else:
                if pu > pv:
                    pu, pv = pv, pu
                x = pu
                ans = 0
                for k in range(logn - 1, -1, -1):
                    y = jump[k][x]
                    if y < pv:
                        x = y
                        ans |= 1 << k
                out.append(ans + 1)
        return out

# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/solutions/6694896/python3-onlogn-beat-100-with-sort-and-sp-k6rr/

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        conn, far, remap = [0] * n, list(range(n)), [0] * n
        nums_with_idx = sorted((v, i) for i, v in enumerate(nums))
        for sorted_pos, (_, orig_idx) in enumerate(nums_with_idx): remap[orig_idx] = sorted_pos
        nums_sorted = [v for v, _ in nums_with_idx]
        curc = 0
        for i in range(1, n):
            if nums_sorted[i] - nums_sorted[i - 1] > maxDiff: curc = i
            conn[i] = curc
        j = 0
        for i in range(n):
            while j < n and nums_sorted[j] - nums_sorted[i] <= maxDiff: j += 1
            far[i] = j - 1
        maxlog = floor(math.log2(n)) if n > 1 else 0
        st = [[0] * (maxlog + 1) for _ in range(n)]
        for i in range(n): st[i][0] = far[i]
        for k in range(1, maxlog + 1):
            for i in range(n): st[i][k] = st[st[i][k - 1]][k - 1]
        @lru_cache(None)
        def min_jumps(u, v):
            if u == v: return 0
            if u > v: u, v = v, u
            if far[u] >= v: return 1
            jumps = 0
            for k in range(maxlog, -1, -1):
                nxt = st[u][k]
                if nxt < v:
                    u = nxt
                    jumps += (1 << k)
            return jumps + 1
        ans = []
        for u, v in queries:
            u, v = remap[u], remap[v]
            ans.append(min_jumps(u, v) if conn[u] == conn[v] else -1)
        return ans

class Solution:
    def pathExistenceQueries(self, n: int, m: List[int], d: int, q: List[List[int]]) -> List[int]:
        a=sorted(range(n),key=m.__getitem__);v=[m[i]for i in a];p={x:i for i,x in enumerate(a)};t=[[bisect_right(v,x+d)-1 for x in v]];[t.append([t[-1][i]for i in t[-1]])for _ in range(17)];return[(lambda u,w:-1 if t[-1][u]<w else sum((u:=t[k][u])*0+(1<<k)for k in range(17,-1,-1)if t[k][u]<w)+(u<w))(*sorted([p[x],p[y]]))for x,y in q]

test('''
3534. Path Existence Queries in a Graph II
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer n representing the number of nodes in a graph, labeled from 0 to n - 1.

You are also given an integer array nums of length n and an integer maxDiff.

An undirected edge exists between nodes i and j if the absolute difference between nums[i] and nums[j] is at most maxDiff (i.e., |nums[i] - nums[j]| <= maxDiff).

You are also given a 2D integer array queries. For each queries[i] = [ui, vi], find the minimum distance between nodes ui and vi. If no path exists between the two nodes, return -1 for that query.

Return an array answer, where answer[i] is the result of the ith query.

Note: The edges between the nodes are unweighted.

 

Example 1:

Input: n = 5, nums = [1,8,3,4,2], maxDiff = 3, queries = [[0,3],[2,4]]

Output: [1,1]

Explanation:

The resulting graph is:



Query   Shortest Path   Minimum Distance
[0, 3]  0 → 3   1
[2, 4]  2 → 4   1
Thus, the output is [1, 1].

Example 2:

Input: n = 5, nums = [5,3,1,9,10], maxDiff = 2, queries = [[0,1],[0,2],[2,3],[4,3]]

Output: [1,2,-1,1]

Explanation:

The resulting graph is:



Query   Shortest Path   Minimum Distance
[0, 1]  0 → 1   1
[0, 2]  0 → 1 → 2   2
[2, 3]  None    -1
[4, 3]  3 → 4   1
Thus, the output is [1, 2, -1, 1].

Example 3:

Input: n = 3, nums = [3,6,1], maxDiff = 1, queries = [[0,0],[0,1],[1,2]]

Output: [0,-1,-1]

Explanation:

There are no edges between any two nodes because:

Nodes 0 and 1: |nums[0] - nums[1]| = |3 - 6| = 3 > 1
Nodes 0 and 2: |nums[0] - nums[2]| = |3 - 1| = 2 > 1
Nodes 1 and 2: |nums[1] - nums[2]| = |6 - 1| = 5 > 1
Thus, no node can reach any other node, and the output is [0, -1, -1].

 

Constraints:

1 <= n == nums.length <= 105
0 <= nums[i] <= 105
0 <= maxDiff <= 105
1 <= queries.length <= 105
queries[i] == [ui, vi]
0 <= ui, vi < n
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
4,566/16.8K
Acceptance Rate
27.1%
Topics
Principal
Array
Two Pointers
Binary Search
Dynamic Programming
Greedy
Bit Manipulation
Graph Theory
Sorting
Weekly Contest 447
icon
Companies
Hint 1
Sort the nodes according to nums[i].
Hint 2
Can we use binary jumping?
Hint 3
Use binary jumping with a sparse table data structure.
''')
