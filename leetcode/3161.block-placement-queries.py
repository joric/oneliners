from lc import *

# https://leetcode.com/problems/block-placement-queries/solutions/8290843/block-placement-queries-by-leetcode-4gh0/?envType=daily-question&envId=2026-05-30

# Segment Tree

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx = 50000

        st = SortedList([0, mx])
        for q in queries:
            if q[0] == 1:
                st.add(q[1])

        bt = [0] * (mx + 1)

        def update(x: int, v: int) -> None:
            while x < len(bt):
                if v > bt[x]:
                    bt[x] = v
                x += x & -x

        def query(x: int) -> int:
            res = 0
            while x > 0:
                if bt[x] > res:
                    res = bt[x]
                x -= x & -x
            return res

        pre = 0
        for x in st:
            if x == 0:
                continue
            update(x, x - pre)
            pre = x

        ans = []
        for q in reversed(queries):
            if q[0] == 2:
                x, sz = q[1], q[2]
                idx = st.bisect_left(x)
                if idx < len(st) and st[idx] == x:
                    pre_val = x
                else:
                    pre_val = st[idx - 1]
                max_space = query(pre_val)
                max_space = max(max_space, x - pre_val)
                ans.append(max_space >= sz)
            else:
                x = q[1]
                idx = st.bisect_left(x)
                pre_val = st[idx - 1]
                nxt = st[idx + 1]
                update(nxt, nxt - pre_val)
                st.discard(x)

        return ans[::-1]


# https://leetcode.com/problems/block-placement-queries/solutions/5295649/block-placement-queries-python3-sol-by-t-90us/?envType=daily-question&envId=2026-05-30

class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        bit, res = [0] * (min(50000, 3 * len(queries)) + 1), []
        
        def bit_range(p, down=True):
            while p >= 0 and p < len(bit):
                yield p
                p = (p & (p + 1)) - 1 if down else p | (p + 1)
        
        def get_max(p: int) -> int:
            return max(bit[i] for i in bit_range(p))
        
        def update(p, val):
            for idx in bit_range(p, False):
                bit[idx] = max(bit[idx], val)

        blocks = [0] + sorted([x for t, x, *sz in queries if t == 1])
        for i, b in enumerate(blocks[1:]):
            update(b, b - blocks[i])

        for t, x, *sz in reversed(queries):
            p = bisect_left(blocks, x)
            if t == 1:
                if p + 1 < len(blocks):
                    update(blocks[p + 1], blocks[p + 1] - blocks[p - 1])
                del blocks[p]
            else:
                res.append(x - blocks[p - 1] >= sz[0] or get_max(x) >= sz[0])
        return res[::-1]


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        bit, res = [0] * (min(50000, 3 * len(queries)) + 1), []

        e=lambda p,d=1:[p]+e((p&(p+1))-1 if d else p|(p+1),d)if 0<=p<len(bit)else[]

        def update(p, val):
            for i in e(p,0):
                bit[i] = max(b[i], val)

        blocks = [0] + sorted([x for t, x, *sz in queries if t == 1])
        for i, b in enumerate(blocks[1:]):
            update(b, b - blocks[i])

        for t, x, *sz in reversed(queries):
            p = bisect_left(blocks, x)
            if t == 1:
                if p + 1 < len(blocks):
                    update(blocks[p + 1], blocks[p + 1] - blocks[p - 1])
                del blocks[p]
            else:
                res.append(x - blocks[p - 1] >= sz[0] or max(bit[i] for i in e(x)) >= sz[0])
        return res[::-1]

class Solution:
    def getResults(self, q: List[List[int]]) -> List[bool]:
        r=[]
        b=[0]*(min(9**5,3*len(q))+1)
        e=lambda p,u=1:[p]+e((p&(p+1))-1 if u else p|(p+1),u)if 0<=p<len(b)else[]
        u=lambda p,x:[setitem(b,i,max(b[i],x))for i in e(p,0)]
        d=[0]+sorted([x for t,x,*s in q if t<2])
        [u(x,x-d[i])for i,x in enumerate(d[1:])]
        [(p:=bisect_left(d,x),t<2 and(p+1<len(d)and u(d[p+1],d[p+1]-d[p-1]),d.pop(p))or r.append(x-d[p-1]>=s[0]or max(b[i]for i in e(x))>=s[0]))for t, x, *s in q[::-1]]
        return r[::-1]

class Solution:
    def getResults(self, q: List[List[int]]) -> List[bool]:
        r=[];b=[0]*(min(9**5,3*len(q))+1);e=lambda p,u=1:[p]+e((p&(p+1))-1 if u else p|(p+1),u)if 0<=p<len(b)else[];u=lambda p,x:[setitem(b,i,max(b[i],x))for i in e(p,0)];d=[0]+sorted([x for t,x,*s in q if t<2]);[u(x,x-d[i])for i,x in enumerate(d[1:])];[(p:=bisect_left(d,x),t<2 and(p+1<len(d)and u(d[p+1],d[p+1]-d[p-1]),d.pop(p))or r.append(x-d[p-1]>=s[0]or max(b[i]for i in e(x))>=s[0]))for t, x, *s in q[::-1]];return r[::-1]

class Solution:
    def getResults(self, q: List[List[int]]) -> List[bool]:
        r,b,e=[],Counter(),lambda p,u=1:[p]+e((p&(p+1))-1 if u else p|(p+1),u)if 0<=p<10**5 else[];u=lambda p,x:[setitem(b,i,max(b[i],x))for i in e(p,0)];d=[0]+sorted([x for t,x,*s in q if t<2]);[u(x,x-d[i])for i,x in enumerate(d[1:])];[(p:=bisect_left(d,x),t<2 and(p+1<len(d)and u(d[p+1],d[p+1]-d[p-1]),d.pop(p))or(r.append(x-d[p-1]>=s[0]or max(b[i]for i in e(x))>=s[0])))for t,x,*s in q[::-1]];return r[::-1]

class Solution:
    def getResults(self, q: List[List[int]]) -> List[bool]:
        r,b,e=[],Counter(),lambda p,u=1:[p]+e((p&(p+1))-1 if u else p|(p+1),u)if 0<=p<10**5 else[];u=lambda p,x:[setitem(b,i,max(b[i],x))for i in e(p,0)];d=[0]+sorted(x for t,x,*s in q if t<2);[u(x,x-y)for y,x in zip(d,d[1:])];[(p:=bisect_left(d,x),t<2 and(d[p+1:]and u(d[p+1],d[p+1]-d[p-1]),d.pop(p))or r.append(max([x-d[p-1]]+[b[i]for i in e(x)])>=s[0]))for t,x,*s in q[::-1]];return r[::-1]

class Solution:
    def getResults(self, q: List[List[int]]) -> List[bool]:
        r,b,e=[],Counter(),lambda p,u=1:1e5>p>=0 and[p]+e(u and~-(p&(p+1))or p|(p+1),u)or[];u=lambda p,x:[setitem(b,i,max(b[i],x))for i in e(p,0)];d=[0]+sorted(x for t,x,*s in q if t<2);[u(x,x-y)for y,x in zip(d,d[1:])];[(p:=bisect_left(d,x),t<2 and(d[p+1:]and u(d[p+1],d[p+1]-d[p-1]),d.pop(p))or r.append(max([x-d[p-1]]+[b[i]for i in e(x)])>=s[0]))for t,x,*s in q[::-1]];return r[::-1]

test('''
3161. Block Placement Queries
Hard
Topics
premium lock icon
Companies
Hint
There exists an infinite number line, with its origin at 0 and extending towards the positive x-axis.

You are given a 2D array queries, which contains two types of queries:

For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x from the origin. It is guaranteed that there is no obstacle at distance x when the query is asked.
For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to place a block of size sz anywhere in the range [0, x] on the line, such that the block entirely lies in the range [0, x]. A block cannot be placed if it intersects with any obstacle, but it may touch it. Note that you do not actually place the block. Queries are separate.
Return a boolean array results, where results[i] is true if you can place the block specified in the ith query of type 2, and false otherwise.

 

Example 1:

Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]

Output: [false,true,true]

Explanation:



For query 0, place an obstacle at x = 2. A block of size at most 2 can be placed before x = 3.

Example 2:

Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]

Output: [true,true,false]

Explanation:



Place an obstacle at x = 7 for query 0. A block of size at most 7 can be placed before x = 7.
Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can be placed before x = 7, and a block of size at most 2 before x = 2.
 

Constraints:

1 <= queries.length <= 15 * 104
2 <= queries[i].length <= 3
1 <= queries[i][0] <= 2
1 <= x, sz <= min(5 * 104, 3 * queries.length)
The input is generated such that for queries of type 1, no obstacle exists at distance x when the query is asked.
The input is generated such that there is at least one query of type 2.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
13,082/69.8K
Acceptance Rate
18.7%
Topics
Principal
Array
Binary Search
Binary Indexed Tree
Segment Tree
Biweekly Contest 131
icon
Companies
Hint 1
Let d[x] be the distance of the next obstacle after x.
Hint 2
For each query of type 2, we just need to check if max(d[0], d[1], d[2], …d[x - sz]) > sz.
Hint 3
Use segment tree to maintain d[x].
Similar Questions
Building Boxes
Hard
Fruits Into Baskets III
Medium
''')
