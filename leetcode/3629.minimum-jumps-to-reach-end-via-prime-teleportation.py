from lc import *

# https://leetcode.com/problems/minimum-jumps-to-reach-end-via-prime-teleportation

class Solution:
    def minJumps(self, a: List[int]) -> int:
        n = len(a)
        m = max(a)
        p = [1] * (m + 1)
        p[0] = p[1] = 0
        for i in range(2, int(m ** 0.5) + 1):
            if p[i]:
                s = i
                t = i * i
                for j in range(t, m + 1, s):
                    p[j] = 0

        d = defaultdict(list)
        for i,x in enumerate(a):
            d[x].append(i)

        v = [0] * n
        u = [0] * (m + 1)

        q = deque()
        q.append((0, 0))
        v[0] = 1

        while q:
            i, c = q.popleft()
            if i == n - 1:
                return c
            for b in (i - 1, i + 1):
                if 0 <= b < n and not v[b]:
                    v[b] = 1
                    q.append((b, c + 1))
            x = a[i]
            if p[x] and not u[x]:
                u[x] = 1
                for k in range(x, m + 1, x):
                    if k in d:
                        for j in d[k]:
                            if not v[j]:
                                v[j] = 1
                                q.append((j, c + 1))
        return -1

class Solution:
    def minJumps(self, a: List[int]) -> int:
        n=len(a);m=max(a);p=[0,0]+[1]*m;d=defaultdict(list)
        [setitem(p,j,0)for i in range(2,isqrt(m)+1)if p[i]for j in range(i*i,m+1,i)]
        [d[x].append(i)for i,x in enumerate(a)]
        u={0}
        v={0}
        q=deque([(0,0)])
        while q:
            i,c=q.popleft()
            if i==n-1:
                return c
            for b in(i-1,i+1):
                if 0<=b<n and{b}-v:
                    v.add(b)
                    q.append((b,c+1))
            x=a[i]
            if p[x]and{x}-u:
                u.add(x)
                for k in range(x,m+1,x):
                    for j in d[k]:
                        if {j}-v:
                            v.add(j)
                            q.append((j,c+1))
        return-1

class Solution:
    def minJumps(self, a: List[int]) -> int:
        n,m,u,v,d,q=len(a),max(a),{0},{0},defaultdict(list),deque();p=[0,0]+[1]*m;[setitem(p,j,0) for i in range(2,isqrt(m)+1)if p[i]for j in range(i*i,m+1,i)];[d[x].append(i)for i,x in enumerate(a)];return(f:=lambda i,c:c if i==n-1 else([v.add(b)or q.append((b,c+1))for b in (i-1,i+1)if 0<=b<n and {b}-v],p[x:=a[i]]and{x}-u and(u.add(x)or[v.add(j)or q.append((j,c+1))for k in range(x,m+1,x)for j in d[k]if{j}-v]))and q and f(*q.popleft())or-1)(0,0)

# 11771 ms

class Solution:
    def minJumps(self, a: List[int]) -> int:
        r=range;n,m,v,d,q=len(a),max(a),{0},defaultdict(list),deque();s={0,1}|{j for i in r(2,m)for j in r(i*i,m+1,i)};[d[a[i]].append(i)for i in r(n)];return(f:=lambda i,c:i<n-1 and([v.add(b)or q.append((b,c+1))for b in(i-1,i+1)if 0<=b<n and{b}-v],{x:=a[i]}-s and(s.add(x)or[v.add(j)or q.append((j,c+1))for k in r(x,m+1,x)for j in d[k]if{j}-v]))and q and f(*q.popleft())or c)(0,0)

test('''
3629. Minimum Jumps to Reach End via Prime Teleportation
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n.

You start at index 0, and your goal is to reach index n - 1.

From any index i, you may perform one of the following operations:

Adjacent Step: Jump to index i + 1 or i - 1, if the index is within bounds.
Prime Teleportation: If nums[i] is a prime number p, you may instantly jump to any index j != i such that nums[j] % p == 0.
Return the minimum number of jumps required to reach index n - 1.

 

Example 1:

Input: nums = [1,2,4,6]

Output: 2

Explanation:

One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index 1.
At index i = 1, nums[1] = 2 is a prime number. Therefore, we teleport to index i = 3 as nums[3] = 6 is divisible by 2.
Thus, the answer is 2.

Example 2:

Input: nums = [2,3,4,7,9]

Output: 2

Explanation:

One optimal sequence of jumps is:

Start at index i = 0. Take an adjacent step to index i = 1.
At index i = 1, nums[1] = 3 is a prime number. Therefore, we teleport to index i = 4 since nums[4] = 9 is divisible by 3.
Thus, the answer is 2.

Example 3:

Input: nums = [4,6,5,8]

Output: 3

Explanation:

Since no teleportation is possible, we move through 0 → 1 → 2 → 3. Thus, the answer is 3.

Other examples:

Input: nums = [7,5,7]
Output: 1

Input: nums = [10,3,8,10]
Output: 3

Constraints:

1 <= n == nums.length <= 105
1 <= nums[i] <= 106
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
27,130/84.9K
Acceptance Rate
31.9%
Topics
Staff
Array
Hash Table
Math
Breadth-First Search
Number Theory
Weekly Contest 460
icon
Companies
Hint 1
Use a breadth-first search.
Hint 2
Precompute prime factors of each nums[i] via a sieve, and build a bucket bucket[p] mapping each prime p to all indices j with nums[j] % p == 0.
Hint 3
During the BFS, when at index i, enqueue its adjacent steps (i+1 and i-1) and all indices in bucket[p] for each prime p dividing nums[i], then clear bucket[p] so each prime's bucket is visited only once.
''')
