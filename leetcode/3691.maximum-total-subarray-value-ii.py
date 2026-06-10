from lc import *

# https://leetcode.com/problems/maximum-total-subarray-value-ii/solutions/7232248/simple-python-solution-beats-100-by-user-zhpx/?envType=daily-question&envId=2026-06-10

class Solution:
    def maxTotalValue(self, a: list[int], k: int) -> int:
        n = len(a)
        d = [0]*(n+1)
        f = lambda l,r:min(p[l][j:=d[r-l+1]],p[r-(1<<j)+1][j])-max(q[l][j],q[r-(1<<j)+1][j])

        for i in range(2, n+1):
            d[i] = d[i//2]+1

        p = [[0]*(d[n]+1) for _ in range(n)]
        q = [[0]*(d[n]+1) for _ in range(n)]

        for i in range(n):
            p[i][0], q[i][0] = a[i], a[i]

        for j in range(0, n.bit_length() - 1):
            for i in range(0, n - (1 << (j + 1)) + 1):
                p[i][j + 1] = min(p[i][j], p[i + (1 << j)][j])
                q[i][j + 1] = max(q[i][j], q[i + (1 << j)][j])

        h = []
        for l in range(n):
            heappush(h,(f(l,n-1),l,n-1))

        t = 0
        for _ in range(k):
            v,l,r = heappop(h)
            t -= v
            if r > l:
                heappush(h,(f(l,r-1),l,r-1))

        return t

class Solution:
    def maxTotalValue(self, a: list[int], k: int) -> int:
        n=len(a);d=[0]*-~n;h=[];s=setitem;p=heappush;r=range;
        [s(d,i,d[i//2]+1)for i in r(2,n+1)];w=[[[0]*-~d[n]for _ in r(n)]for _ in(0,1)];
        z=[*zip(w,(min,max))];f=lambda l,r:sub(*[m(t[l][j:=d[r-l+1]],t[r-(1<<j)+1][j])for t,m in z]);
        [s(t[i],0,a[i])for i in r(n)for t in w];[s(t[i],j+1,m(t[i][j],t[i+2**j][j]))for j in r(n.bit_length()-1)for i in r(0,n-(2**-~j)+1)for t,m in z];
        [p(h,(f(l,n-1),l,n-1))for l in r(n)];return-sum((lambda v,l,r:r>l and p(h,(f(l,r-1),l,r-1))or v)(*heappop(h))for _ in r(k))

class Solution:
    def maxTotalValue(self, a: list[int], k: int) -> int:
        n=len(a);b=int.bit_length;d=~-b(n);h=[];p=heappush;r=range;z=[([[x]+d*[0]for x in a],m)for m in(min,max)];f=lambda x,y:sub(*[m(t[x][j:=~-b(y-x+1)],t[y-2**j+1][j])for t,m in z]);[setitem(t[i],j+1,m(t[i][j],t[i+2**j][j]))for j in r(d)for i in r(n-2**-~j+1)for t,m in z];[p(h,(f(i,n-1),i,n-1))for i in r(n)];return-sum((lambda v,x,y:y>x and p(h,(f(x,y-1),x,y-1))or v)(*heappop(h))for _ in r(k))

class Solution:
    def maxTotalValue(self, a: list[int], k: int) -> int:
        n=len(a);b=int.bit_length;d=~-b(n);h=[];p=heappush;r=range;z=[([[x]+d*[0]for x in a],m)for m in(min,max)];f=lambda x,y:sub(*[m(t[x][j:=~-b(y-x)],t[y-2**j][j])for t,m in z]);[setitem(t[i],j+1,m(t[i][j],t[i+2**j][j]))for j in r(d)for i in r(n-2**-~j+1)for t,m in z];[p(h,(f(i,n),i,n-1))for i in r(n)];return-sum((lambda v,x,y:y>x and p(h,(f(x,y),x,y-1))or v)(*heappop(h))for _ in r(k))

class Solution:
    def maxTotalValue(self, a: list[int], k: int) -> int:
        n=len(a);b=int.bit_length;r=range;z=[([[x]*b(n)for x in a],m)for m in(min,max)];f=lambda x,y:sub(*[m(t[x][j:=~-b(y-x)],t[y-2**j][j])for t,m in z]);[setitem(t[i],j+1,m(t[i][j],t[i+2**j][j]))for t,m in z for j in r(~-b(n))for i in r(n-2**-~j+1)];heapify(h:=[(f(i,n),i,n-1)for i in r(n)]);return-sum((lambda v,x,y:y>x and heappush(h,(f(x,y),x,y-1))or v)(*heappop(h))for _ in r(k))

test('''
3691. Maximum Total Subarray Value II
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n and an integer k.

You must select exactly k distinct non-empty subarrays nums[l..r] of nums. Subarrays may overlap, but the exact same subarray (same l and r) cannot be chosen more than once.

The value of a subarray nums[l..r] is defined as: max(nums[l..r]) - min(nums[l..r]).

The total value is the sum of the values of all chosen subarrays.

Return the maximum possible total value you can achieve.

 

Example 1:

Input: nums = [1,3,2], k = 2

Output: 4

Explanation:

One optimal approach is:

Choose nums[0..1] = [1, 3]. The maximum is 3 and the minimum is 1, giving a value of 3 - 1 = 2.
Choose nums[0..2] = [1, 3, 2]. The maximum is still 3 and the minimum is still 1, so the value is also 3 - 1 = 2.
Adding these gives 2 + 2 = 4.

Example 2:

Input: nums = [4,2,5,1], k = 3

Output: 12

Explanation:

One optimal approach is:

Choose nums[0..3] = [4, 2, 5, 1]. The maximum is 5 and the minimum is 1, giving a value of 5 - 1 = 4.
Choose nums[1..3] = [2, 5, 1]. The maximum is 5 and the minimum is 1, so the value is also 4.
Choose nums[2..3] = [5, 1]. The maximum is 5 and the minimum is 1, so the value is again 4.
Adding these gives 4 + 4 + 4 = 12.

 

Constraints:

1 <= n == nums.length <= 5 * 10​​​​​​​4
0 <= nums[i] <= 109
1 <= k <= min(105, n * (n + 1) / 2)
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
12,954/56.9K
Acceptance Rate
22.7%
Topics
Principal
Array
Greedy
Segment Tree
Heap (Priority Queue)
Weekly Contest 468
icon
Companies
Hint 1
For fixed l, the sequence v(l,r)=max(nums[l..r])−min(nums[l..r]) is non-increasing as r moves left.
Hint 2
Build RMQs (sparse tables) for range max/min so each v(l,r) is queryable in O(1).
Hint 3
Use a max-heap with v(l,n-1) for all l; pop the largest k times, and after popping an entry from (l,r) push (l,r-1) if r>l.
''')
