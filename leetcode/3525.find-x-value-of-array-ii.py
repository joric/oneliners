from lc import *

# https://leetcode.com/problems/find-x-value-of-array-ii/solutions/6668800/segment-tree-explanation-pythonjavac-by-jyraa/?envType=daily-question&envId=2026-09-22

class SegTree:
    def __init__(self, nums: List[int], k: int):
        self.k = k
        self.n = len(nums)
        s = 1
        while s < self.n:
            s <<= 1
        self.s = s
        self.tree = [([0 for _ in range(k)], 1) for _ in range(2 * s)]
        for i in range(self.n):
            a_mod = nums[i] % k
            cnt = [0 for _ in range(k)]
            cnt[a_mod] = 1
            prod = a_mod
            self.tree[s + i] = (cnt, prod)
        for p in range(s - 1, 0, -1):
            self.tree[p] = self.merge(self.tree[2 * p], self.tree[2 * p + 1])

    def merge(self, l, r):
        cnt_a, prod_a = l
        cnt_b, prod_b = r
        k = self.k
        cnt = cnt_a.copy()
        for r_b, c in enumerate(cnt_b):
            if c:
                r = (prod_a * r_b) % k
                cnt[r] += c
        prod = (prod_a * prod_b) % k
        return cnt, prod

    def update(self, idx, val):
        pos = self.s + idx
        a_mod = val % self.k
        cnt = [0] * self.k
        cnt[a_mod] = 1
        prod = a_mod
        self.tree[pos] = (cnt, prod)
        pos //= 2
        while pos:
            self.tree[pos] = self.merge(self.tree[2 * pos], self.tree[2 * pos + 1])
            pos //= 2

    def query(self, l, r):
        l += self.s
        r += self.s
        cnt_l, prod_l = [0]*self.k, 1
        cnt_r, prod_r = [0]*self.k, 1
        while l < r:
            if l & 1:
                cnt_l, prod_l = self.merge((cnt_l, prod_l), self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                cnt_r, prod_r = self.merge(self.tree[r], (cnt_r, prod_r))
            l //= 2
            r //= 2
        return self.merge((cnt_l, prod_l), (cnt_r, prod_r))

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        st = SegTree(nums, k)
        res = []
        for idx, val, start, x in queries:
            st.update(idx, val)
            cnt_seg, _ = st.query(start, len(nums))
            res.append(cnt_seg[x])
        return res

class Solution:
    def resultArray(self, a: List[int], k: int, q: List[List[int]]) -> List[int]:
        n = len(a)
        s = 1 << (n - 1).bit_length()

        def m(x, y):
            p, u = x; r, v = y
            c = p[:]
            for i, z in enumerate(r): c[u*i % k] += z
            return c, u*v % k

        for i, v in enumerate(a):
            b = v % k; c = [0]*k; c[b] = 1
            t[s+i] = (c, b)
        for i in range(s-1, 0, -1):
            t[i] = m(t[2*i], t[2*i+1])

        def f(i, v):
            j = s + i; b = v % k; c = [0]*k; c[b] = 1
            t[j] = (c, b); j >>= 1
            while j:
                t[j] = m(t[2*j], t[2*j+1]); j >>= 1

        def g(l, r):
            l += s; r += s
            p, u = ([0]*k, 1), ([0]*k, 1)
            while l < r:
                if l & 1: p = m(p, t[l]); l += 1
                if r & 1: r -= 1; u = m(t[r], u)
                l >>= 1; r >>= 1
            return m(p, u)

        o = []
        for i, v, w, x in q:
            f(i, v)
            o.append(g(w, n)[0][x])
        return o

class Solution:
    def resultArray(self, a: List[int], k: int, q: List[List[int]]) -> List[int]:
        e=enumerate;g=range;s=setitem;n=len(a);b=1<<n.bit_length();z=[0]*k,1;t=[z]*2*b;d=lambda v:s(c:=[0]*k,v%k,1)or(c,v%k);m=lambda x,w:(c:=x[0][:],[s(c,j:=x[1]*i%k,c[j]+h)for i,h in e(w[0])if h],(c,x[1]*w[1]%k))[2];[s(t,b+i,d(v))for i,v in e(a)];[s(t,i,m(t[2*i],t[2*i+1]))for i in g(~-b,0,-1)];return[(s(t,j:=b+i,d(v)),[s(t,j:=j//2,m(t[2*j],t[2*j+1]))for _ in g(18)if j>1],l:=b+w,r:=b+n,p:=z,u:=z,[(p:=l&1 and m(p,t[l])or p,u:=r&1 and m(t[r-1],u)or u,l:=(l+1)//2,r:=r//2)for _ in g(18)if l<r],m(p,u)[0][x])[-1]for i,v,w,x in q]

# https://leetcode.com/problems/find-x-value-of-array-ii/solutions/6669392/square-root-decomposition-vs-segment-tre-tysm/?envType=daily-question&envId=2026-09-22

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        def rebuild(b):
            l = b * B
            r = min(n, l + B)
            for p in range(k):
                cnt = [0] * k
                cur = p
                for i in range(l, r):
                    cur = (cur * A[i]) % k
                    cnt[cur] += 1
                block_final[b][p] = cur
                block_cnt[b][p] = cnt

        n = len(nums)
        if k == 1:
            return [n - start for _, _, start, _ in queries]
        B = max(1, int((n / k) ** 0.5))
        A = [v % k for v in nums]
        nb = (n + B - 1) // B
        block_cnt = [[[0] * k for _ in range(k)] for _ in range(nb)]
        block_final = [[0] * k for _ in range(nb)]
        for b in range(nb):
            rebuild(b)
            
        res = []
        for idx, val, start, x in queries:
            A[idx] = val % k
            rebuild(idx // B)
            ans = 0
            p = 1
            b0 = start // B
            end = min(n, (b0 + 1) * B)
            for i in range(start, end):
                p = (p * A[i]) % k
                if p == x:
                    ans += 1
            b = b0 + 1
            while b < nb:
                ans += block_cnt[b][p][x]
                p = block_final[b][p]
                b += 1
            res.append(ans)
        return res

class Solution:
    def resultArray(self, a: List[int], b: int, c: List[List[int]]) -> List[int]:
        d=len(a)
        if b==1:return[d-s for j,v,s,x in c]
        e=max(1,isqrt(d//b));g=(d+e-1)//e;r=range;h=[[[0]*b for _ in r(b)]for _ in r(g)];i=[[0]*b for _ in r(g)]
        def u(x):
            for p in r(b):
                t=[0]*b;v=p
                for w in r(x*e,min(d,x*e+e)):v=v*a[w]%b;t[v]+=1
                i[x][p],h[x][p]=v,t
        for x in r(g):u(x)
        y=[]
        for j,v,s,x in c:
            a[j]=v;u(j//e);z=0;p=1;m=s//e
            for w in r(s,min(d,m*e+e)):p=p*a[w]%b;z+=p==x
            for w in r(m+1,g):z+=h[w][p][x];p=i[w][p]
            y+=[z]
        return y

class Solution:
    def resultArray(self, a: List[int], k: int, q: List[List[int]]) -> List[int]:
        l=len(a)
        if k==1:return[l-s for _,_,s,_ in q]
        b=int((l/k)**.5)or 1;m=(l-1)//b+1;a=[v%k for v in a];h,f=([[0]*k for _ in range(m)]for _ in'12');r=[]
        def w(i):
            for p in range(k):
                t=[0]*k;c=p
                for y in a[i*b:i*b+b]:c=c*y%k;t[c]+=1
                f[i][p],h[i][p]=c,t
        for i in range(m):w(i)
        for i,v,s,x in q:
            a[i]=v%k;w(i//b);n=0;p=1;c=s//b
            for y in a[s:c*b+b]:p=p*y%k;n+=p==x
            for j in range(c+1,m):n+=h[j][p][x];p=f[j][p]
            r.append(n)
        return r

class Solution:
    def resultArray(self, a: List[int], k: int, q: List[List[int]]) -> List[int]:
        l=len(a)
        b=isqrt(l//k)or 1
        m=(l-1)//b+1
        a=[v%k for v in a]
        h = [[0]*k for _ in range(m)]
        f = [[0]*k for _ in range(m)]
        r=[]

        def w(i):
            for p in range(k):
                t=[0]*k
                c=p
                for y in a[i*b:i*b+b]:
                    c = c*y%k
                    setitem(t,c,t[c]+1)
                setitem(f[i],p,c)
                setitem(h[i],p,t)

        for i in range(m):
            w(i)

        for i,v,s,x in q:
            a[i]=v%k
            w(i//b)
            n=0
            p=1
            c=s//b
            for y in a[s:c*b+b]:
                p=p*y%k
                n+=p==x
            for j in range(c+1,m):
                n+=h[j][p][x]
                p=f[j][p]
            r.append(n)
        return r

class Solution: # TLE
    def resultArray(self, a: List[int], k: int, q: List[List[int]]) -> List[int]:
        l=len(a);b=isqrt(l//k)or 1;m=(l-1)//b+1;a=[v%k for v in a];h,f=[[[0]*k for _ in range(m)]for _ in'..'];r=[];w=lambda i:all((t:=[0]*k,c:=p,all((c:=c*y%k,setitem(t,c,t[c]+1))for y in a[i*b:i*b+b]),setitem(f[i],p,c),setitem(h[i],p,t))for p in range(k));all(map(w,range(m)));return[(setitem(a,i,v%k),w(i//b),n:=0,p:=1,c:=s//b,all((p:=p*y%k,n:=n+(p==x))for y in a[s:c*b+b]),all((n:=n+h[j][p][x],p:=f[j][p])for j in range(c+1,m)),n)[-1]for i,v,s,x in q]

class Solution:
    def resultArray(self, a: List[int], k: int, q: List[List[int]]) -> List[int]:
        g=range;l=len(a);b=isqrt(l//k)or 1;m=(l-1)//b+1;a=[v%k for v in a];h,f=([[0]*k for _ in g(m)]for _ in'12');w=lambda i:(fq:=[0]*k,c:=1,[fq.__setitem__(c:=c*y%k,fq[c]+1)for y in a[i*b:i*b+b]],[(t:=[0]*k,[fq[x]and t.__setitem__(px:=p*x%k,t[px]+fq[x])for x in g(k)],f[i].__setitem__(p,p*c%k),h[i].__setitem__(p,t))for p in g(k)]);[w(i)for i in g(m)];return[l-s for _,_,s,_ in q]if k==1 else[(a.__setitem__(i,v%k),w(i//b),p:=1,n:=0,[n:=n+((p:=p*y%k)==x)for y in a[s:s//b*b+b]],[(n:=n+h[j][p][x],p:=f[j][p])for j in g(s//b+1,m)],n)[-1]for i,v,s,x in q]

class Solution:
    def resultArray(self, a: List[int], k: int, q: List[List[int]]) -> List[int]:
        s=setitem;g=range;l=len(a);b=isqrt(l//k)or 1;m=(l-1)//b+1;a=[v%k for v in a];h,f=([k*[0]for _ in g(m)]for _ in'..');w=lambda i:(v:=[0]*k,c:=1,[s(v,c:=c*y%k,v[c]+1)for y in a[i*b:i*b+b]],[(t:=[0]*k,[v[x]and s(t,u:=p*x%k,t[u]+v[x])for x in g(k)],s(f[i],p,p*c%k),s(h[i],p,t))for p in g(k)]);[w(i)for i in g(m)];return[l-z for _,_,z,_ in q]if k==1 else[(s(a,i,v%k),w(i//b),p:=1,n:=0,[n:=n+((p:=p*y%k)==x)for y in a[z:z//b*b+b]],[(n:=n+h[j][p][x],p:=f[j][p])for j in g(z//b+1,m)],n)[-1]for i,v,z,x in q]

test('''
3525. Find X Value of Array II
Hard
Topics
premium lock icon
Companies
Hint
You are given an array of positive integers nums and a positive integer k. You are also given a 2D array queries, where queries[i] = [indexi, valuei, starti, xi].

You are allowed to perform an operation once on nums, where you can remove any suffix from nums such that nums remains non-empty.

The x-value of nums for a given x is defined as the number of ways to perform this operation so that the product of the remaining elements leaves a remainder of x modulo k.

For each query in queries you need to determine the x-value of nums for xi after performing the following actions:

Update nums[indexi] to valuei. Only this step persists for the rest of the queries.
Remove the prefix nums[0..(starti - 1)] (where nums[0..(-1)] will be used to represent the empty prefix).
Return an array result of size queries.length where result[i] is the answer for the ith query.

A prefix of an array is a subarray that starts from the beginning of the array and extends to any point within it.

A suffix of an array is a subarray that starts at any point within the array and extends to the end of the array.

Note that the prefix and suffix to be chosen for the operation can be empty.

Note that x-value has a different definition in this version.

 

Example 1:

Input: nums = [1,2,3,4,5], k = 3, queries = [[2,2,0,2],[3,3,3,0],[0,1,0,1]]

Output: [2,2,2]

Explanation:

For query 0, nums becomes [1, 2, 2, 4, 5], and the empty prefix must be removed. The possible operations are:
Remove the suffix [2, 4, 5]. nums becomes [1, 2].
Remove the empty suffix. nums becomes [1, 2, 2, 4, 5] with a product 80, which gives remainder 2 when divided by 3.
For query 1, nums becomes [1, 2, 2, 3, 5], and the prefix [1, 2, 2] must be removed. The possible operations are:
Remove the empty suffix. nums becomes [3, 5].
Remove the suffix [5]. nums becomes [3].
For query 2, nums becomes [1, 2, 2, 3, 5], and the empty prefix must be removed. The possible operations are:
Remove the suffix [2, 2, 3, 5]. nums becomes [1].
Remove the suffix [3, 5]. nums becomes [1, 2, 2].
Example 2:

Input: nums = [1,2,4,8,16,32], k = 4, queries = [[0,2,0,2],[0,2,0,1]]

Output: [1,0]

Explanation:

For query 0, nums becomes [2, 2, 4, 8, 16, 32]. The only possible operation is:
Remove the suffix [2, 4, 8, 16, 32].
For query 1, nums becomes [2, 2, 4, 8, 16, 32]. There is no possible way to perform the operation.
Example 3:

Input: nums = [1,1,2,1,1], k = 2, queries = [[2,1,0,1]]

Output: [5]


Other examples:

Input: nums = [1], k = 2, queries = [[0,8,0,0]]
Output: [1]

Constraints:

1 <= nums[i] <= 109
1 <= nums.length <= 105
1 <= k <= 5
1 <= queries.length <= 2 * 104
queries[i] == [indexi, valuei, starti, xi]
0 <= indexi <= nums.length - 1
1 <= valuei <= 109
0 <= starti <= nums.length - 1
0 <= xi <= k - 1
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
4,043/13.1K
Acceptance Rate
30.9%
Topics
Senior Staff
Array
Math
Segment Tree
Weekly Contest 446
icon
Companies
Hint 1
Use a segment tree to efficiently maintain and merge product prefix information for the array nums.
Hint 2
In each segment tree node, store a frequency count of prefix product remainders for every x in the range [0, k - 1].
Hint 3
For each query, update nums[index] to value, then merge the segments corresponding to nums[start..n - 1] to compute the x-value for xi.
Similar Questions
Longest Uploaded Prefix
Medium
Minimum Sum of Values by Dividing Array
Hard
''')
