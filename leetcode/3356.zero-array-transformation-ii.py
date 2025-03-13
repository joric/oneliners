from lc import *

# https://leetcode.com/problems/zero-array-transformation-ii/solutions/6053434/only-10-lines-of-code-why-fear-when-segment-tree-is-here/?envType=daily-question&envId=2025-03-13

class LazySegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the lazy segment tree with data"""
        self._default = default
        self._func = func

        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()
        self._lazy = [0] * (2 * _size)

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __len__(self):
        return self._len

    def _push(self, idx):
        """push query on idx to its children"""
        # Let the children know of the queries
        q, self._lazy[idx] = self._lazy[idx], 0

        self._lazy[2 * idx] += q
        self._lazy[2 * idx + 1] += q
        self.data[2 * idx] += q
        self.data[2 * idx + 1] += q

    def _update(self, idx):
        """updates the node idx to know of all queries applied to it via its ancestors"""
        for i in reversed(range(1, idx.bit_length())):
            self._push(idx >> i)

    def _build(self, idx):
        """make the changes to idx be known to its ancestors"""
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1]) + self._lazy[idx]
            idx >>= 1

    def add(self, start, stop, value):
        """lazily add value to [start, stop)"""
        start = start_copy = start + self._size
        stop = stop_copy = stop + self._size
        while start < stop:
            if start & 1:
                self._lazy[start] += value
                self.data[start] += value
                start += 1
            if stop & 1:
                stop -= 1
                self._lazy[stop] += value
                self.data[stop] += value
            start >>= 1
            stop >>= 1

        # Tell all nodes above of the updated area of the updates
        self._build(start_copy)
        self._build(stop_copy - 1)

    def query(self, start, stop, default=0):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        # Apply all the lazily stored queries
        self._update(start)
        self._update(stop - 1)

        res = default
        while start < stop:
            if start & 1:
                res = self._func(res, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res = self._func(res, self.data[stop])
            start >>= 1
            stop >>= 1
        return res

    def __repr__(self):
        return "LazySegmentTree({0})".format(self.data)

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        segtree = LazySegmentTree(nums)
        if segtree.query(0, n) <= 0:
            return 0
        for k, q in enumerate(queries):
            lx,rx,v = q[0],q[1],q[2]
            segtree.add(lx, rx+1, -v)
            if segtree.query(0,n) <= 0: 
                return k+1
        return -1

# https://leetcode.com/problems/zero-array-transformation-ii/editorial/?envType=daily-question&envId=2025-03-13

class Solution:
    def minZeroArray(self, a: List[int], q: List[List[int]]) -> int:
        s,k,d = 0,0,[0]*(len(a)+1)
        for i,c in enumerate(a):
            while c>s+d[i]:
                k += 1
                if k > len(q):
                    return -1
                l,r,x = q[k-1]
                if r>=i:
                    d[max(l,i)] += x
                    d[r+1] -= x
            s += d[i]
        return k


# https://leetcode.com/problems/zero-array-transformation-ii/solutions/6059272/python3-12-lines-bin-search/?envType=daily-question&envId=2025-03-13

class Solution:
    def minZeroArray(self, a: List[int], q: List[List[int]]) -> int:
        def f(k):
            c = Counter()
            for l,r,x in q[:k]:
                c[l] += x
                if r < len(a):
                    c[r+1]-= x
            for i,t in enumerate(a):
                c[i+1] += c[i]
                if t > c[i]:
                    return False
            return True
        return(i:=bisect_left(range(len(q)+1),1,key=f),-1)[i>len(q)]

class Solution:
    def minZeroArray(self, a: List[int], q: List[List[int]]) -> int:
        def f(k):
            c=Counter()
            [setitem(c,l,c[l]+x)or r<len(a)and setitem(c,r+1,c[r+1]-x)for l,r,x in q[:k]]
            return all(setitem(c,i+1,c[i+1]+c[i])or t<=c[i]for i,t in enumerate(a))
        return(i:=bisect_left(range(len(q)+1),1,key=f),-1)[i>len(q)]

class Solution:
    def minZeroArray(self, a: List[int], q: List[List[int]]) -> int:
        f=lambda k:(c:=Counter(),[setitem(c,l,c[l]+x)or r<len(a)and setitem(c,r+1,c[r+1]-x)for l,r,x in q[:k]])and all(setitem(c,i+1,c[i+1]+c[i])or t<=c[i]for i,t in enumerate(a));return(i:=bisect_left(range(len(q)+1),1,key=f),-1)[i>len(q)]

class Solution:
    def minZeroArray(self, a: List[int], q: List[List[int]]) -> int:
        s=setitem;f=lambda k:(c:=Counter(),[s(c,l,c[l]+x)or r<len(a)and s(c,r+1,c[r+1]-x)for l,r,x in q[:k]])and all(s(c,i+1,c[i+1]+c[i])or t<=c[i]for i,t in enumerate(a));return(i:=bisect_left(range(len(q)+1),1,key=f),-1)[i>len(q)]

test('''
3356. Zero Array Transformation II
Medium
Topics
Companies
Hint
You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
Example 2:

Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

Output: -1

Explanation:

For i = 0 (l = 1, r = 3, val = 2):
Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
The array will become [4, 1, 0, 0].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
The array will become [3, 0, 0, 0], which is not a Zero Array.
 

Other examples:

Input: nums = [1], queries = [[0,0,3],[0,0,2],[0,0,2],[0,0,3],[0,0,1],[0,0,5],[0,0,1],[0,0,5],[0,0,3],[0,0,5],[0,0,5],[0,0,2],[0,0,2],[0,0,2],[0,0,2]]
Output: 1


Input: nums = [0,10], queries = [[0,1,2],[0,0,2],[0,1,2],[1,1,4],[0,1,3],[1,1,4],[0,1,2],[0,1,2],[0,1,2],[0,0,2],[1,1,2],[0,0,2],[0,0,3],[1,1,3],[0,0,5]]
Output: 5

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 5 * 105
1 <= queries.length <= 105
queries[i].length == 3
0 <= li <= ri < nums.length
1 <= vali <= 5
Seen this question in a real interview before?
1/5
Yes
No
Accepted
21.6K
Submissions
57K
Acceptance Rate
38.0%
Topics
Array
Binary Search
Prefix Sum
Companies
Hint 1
Can we apply binary search here?
Hint 2
Utilize a difference array to optimize the processing of queries.
Similar Questions
Corporate Flight Bookings
Medium
Minimum Moves to Make Array Complementary
Medium
''')
