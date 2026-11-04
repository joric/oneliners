from lc import *

# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/editorial/?envType=daily-question&envId=2026-11-04

class Solution:
    def minOperations(self, a: List[int], x: int, k: int) -> int:
        n = len(a)
        l, r = SortedList(), SortedList()
        p = q = 0
        o = [0] * n
        for i, v in enumerate(a):
            if not l or v <= l[-1]:
                l.add(v); p += v
            else:
                r.add(v); q += v
            if i >= x:
                v = a[i - x]
                if v in l:
                    l.remove(v); p -= v
                else:
                    r.remove(v); q -= v
            if len(l) > len(r) + 1:
                v = l.pop(); r.add(v); p -= v; q += v
            elif len(l) < len(r):
                v = r.pop(0); l.add(v); p += v; q -= v
            if i >= x - 1:
                m = l[-1]
                o[i] = m * len(l) - p + q - m * len(r)
        d = [0] * (n + 1)
        for _ in range(k):
            c = [inf] * (n + 1)
            for i in range(x, n + 1):
                c[i] = min(c[i - 1], d[i - x] + o[i - 1])
            d = c
        return d[n]

class Solution:
    def minOperations(self, a: List[int], x: int, k: int) -> int:
        h=len;n=h(a);t=SortedList;s=setitem;l,r=t(),t();p=q=0;o=[0]*n;[((not l or v<=l[-1])and(l.add(v),p:=p+v,1)or(r.add(v),q:=q+v),i>=x and((w:=a[i-x])in l and(l.remove(w),p:=p-w,1)or(r.remove(w),q:=q-w)),h(l)>1+h(r)and(u:=l.pop(),r.add(u),p:=p-u,q:=q+u,1)or h(l)<h(r)and(u:=r.pop(0),l.add(u),p:=p+u,q:=q-u),i>=x-1 and s(o,i,(m:=l[-1])*h(l)-p+q-m*h(r)))for i,v in enumerate(a)];d=[0]*-~n;[d:=(c:=[inf]*-~n,[s(c,i,min(c[i-1],d[i-x]+o[i-1]))for i in range(x,-~n)],c)[2]for _ in range(k)];return d[n]

# shorter solution

class Solution:
    def minOperations(self, a: List[int], x: int, k: int) -> int:
        o,s=[0],SortedList([0]*x)
        f=lambda v,*_:max(s[x//2]-v,v-s[~x//2])
        for w,v in zip([0]*x+a,a):
            o.append(o[-1]-f(w)+f(v,s.remove(w),s.add(v)))
        return min(reduce(lambda d,j:accumulate(map(add,d,o[-~j*x:]),min),range(k),repeat(0)))

class Solution:
    def minOperations(self, a: List[int], x: int, k: int) -> int:
        o=[0];s=SortedList(o*x);f=lambda v,*_:max(s[x//2]-v,v-s[~x//2]);[o.append(o[-1]-f(w)+f(v,s.remove(w),s.add(v)))for w,v in zip(o*x+a,a)];return min(reduce(lambda d,j:accumulate(map(add,d,o[-~j*x:]),min),range(k),repeat(0)))

test('''
3505. Minimum Operations to Make Elements Within K Subarrays Equal
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and two integers, x and k. You can perform the following operation any number of times (including zero):

Increase or decrease any element of nums by 1.
Return the minimum number of operations needed to have at least k non-overlapping subarrays of size exactly x in nums, where all elements within each subarray are equal.

 

Example 1:

Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2

Output: 8

Explanation:

Use 3 operations to add 3 to nums[1] and use 2 operations to subtract 2 from nums[3]. The resulting array is [5, 1, 1, 1, 7, 3, 6, 4, -1].
Use 1 operation to add 1 to nums[5] and use 2 operations to subtract 2 from nums[6]. The resulting array is [5, 1, 1, 1, 7, 4, 4, 4, -1].
Now, all elements within each subarray [1, 1, 1] (from indices 1 to 3) and [4, 4, 4] (from indices 5 to 7) are equal. Since 8 total operations were used, 8 is the output.
Example 2:

Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2

Output: 3

Explanation:

Use 3 operations to subtract 3 from nums[4]. The resulting array is [9, -2, -2, -2, -2, 5].
Now, all elements within each subarray [-2, -2] (from indices 1 to 2) and [-2, -2] (from indices 3 to 4) are equal. Since 3 operations were used, 3 is the output.
 

Constraints:

2 <= nums.length <= 105
-106 <= nums[i] <= 106
2 <= x <= nums.length
1 <= k <= 15
2 <= k * x <= nums.length
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
5,051/17.4K
Acceptance Rate
29.0%
Topics
Principal
Array
Hash Table
Math
Dynamic Programming
Sliding Window
Heap (Priority Queue)
Weekly Contest 443
icon
Companies
Hint 1
Making every element of an x-sized window equal to its median is optimal.
Hint 2
Precalculate this for each window.
Similar Questions
Find Median from Data Stream
Hard
Minimum Moves to Equal Array Elements II
Medium
''')
