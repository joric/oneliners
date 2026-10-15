from lc import *

# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/solutions/4219769/binary-tree-based-solution-less-memory-t-pmri/?envType=daily-question&envId=2026-10-16

class Solution:
    def sumCounts(self, a: List[int]) -> int:
        p=10**9+7;d={}
        for i,n in enumerate(a):d.setdefault(n,[-1]).append(i)
        c={k:0 for k in d};t=[0,1<<(len(a)-1).bit_length(),None,None,0]
        def r(x):
            if x[1]-x[0]>1:
                m=(x[0]+x[1])>>1;x[2]=[x[0],m,None,None,0];x[3]=[m,x[1],None,None,0];r(x[2]);r(x[3])
        def u(x,y,z):
            if y==x[0] and z==x[1]:x[4]+=z-y;return x[4]
            k=(x[4]-x[2][4]-x[3][4])>>1;x[2][4]+=k;x[3][4]+=k;m=(x[0]+x[1])>>1;o=0
            if y<m:o+=u(x[2],y,min(m,z))
            if z>m:o+=u(x[3],max(m,y),z)
            x[4]+=z-y;return o
        r(t);s=0;f=0
        for n in a:
            y=d[n][c[n]]+1;c[n]+=1;z=d[n][c[n]]+1;s=(s+2*u(t,y,z)-(z-y))%p;f=(f+s)%p
        return f%p

# fenwick

class Solution:
    def sumCounts(self, a: List[int]) -> int:
        p=10**9+7;n=len(a);q=[-1]*n;m={};b=[0]*(n+2);c=[0]*(n+2);z=0;u=0;s=setitem
        any(s(q,i,m.get(a[i],-1))or s(m,a[i],i)for i in range(n))
        d=lambda t,i,v:i<=n+1 and (s(t,i,t[i]+v),d(t,i+(i&-i),v))[0]is None or d(t,i+(i&-i),v) if i<=n+1 else None
        e=lambda t,i:i>0 and (t[i]+e(t,i-(i&-i))) or 0
        f=lambda l,r,v:(d(b,l,v),d(b,r+1,-v),d(c,l,v*(l-1)),d(c,r+1,-v*r))
        g=lambda i:e(b,i)*i-e(c,i)
        h=lambda l,r:g(r)-g(l-1)
        all((l:=q[i]+2,r:=i+1,u:=(u+2*h(l,r)+r-l+1)%p,f(l,r,1),z:=(z+u)%p)for i in range(n))
        return z%p

class Solution:
    def sumCounts(self, a: List[int]) -> int:
        p=10**9+7;n=len(a);q=[-1]*n;m={};b=[0]*(n+2);c=[0]*(n+2);z=0;u=0;s=setitem
        any(s(q,i,m.get(a[i],-1))or s(m,a[i],i)for i in range(n))
        d=lambda t,i,v:i<=n+1 and(s(t,i,t[i]+v)or d(t,i+(i&-i),v))
        e=lambda t,i:i>0 and (t[i]+e(t,i-(i&-i))) or 0
        f=lambda l,r,v:(d(b,l,v),d(b,r+1,-v),d(c,l,v*(l-1)),d(c,r+1,-v*r))
        g=lambda i:e(b,i)*i-e(c,i)
        h=lambda l,r:g(r)-g(l-1)
        all((l:=q[i]+2,r:=i+1,u:=(u+2*h(l,r)+r-l+1)%p,f(l,r,1),z:=(z+u)%p)for i in range(n))
        return z%p

class Solution:
    def sumCounts(self, a: List[int]) -> int:
        p=10**9+7;n=len(a);q=[-1]*n;m={};b=[0]*(n+2);c=[0]*(n+2);z=0;u=0;s=setitem;d=lambda t,i,v:i<=n+1 and(s(t,i,t[i]+v)or d(t,i+(i&-i),v));e=lambda t,i:i>0 and t[i]+e(t,i-(i&-i))or 0;any([(s(q,i,m.get(a[i],-1)),s(m,a[i],i))for i in range(n)]);any([(l:=q[i]+2,r:=i+1,u:=(u+2*(e(b,r)*r-e(c,r)-e(b,l-1)*(l-1)+e(c,l-1))+r-l+1)%p,(d(b,l,1),d(b,r+1,-1),d(c,l,l-1),d(c,r+1,-r),z:=(z+u)%p))for i in range(n)]);return z%p

class Solution:
    def sumCounts(self, a: List[int]) -> int:
        p=10**9+7;n=len(a);m={};b=[0]*(n+2);c=b[:];z=u=0;s=setitem;d=lambda t,i,v:i<n+2 and(s(t,i,t[i]+v)or d(t,i+(i&-i),v));e=lambda t,i:i and t[i]+e(t,i-(i&-i));[(l:=m.get(a[i],-1)+2,r:=i+1,s(m,a[i],i),u:=(u+2*(e(b,r)*r-e(c,r)+e(c,l-1)-e(b,l-1)*(l-1))+r-l+1)%p,d(b,l,1),d(b,r+1,-1),d(c,l,l-1),d(c,r+1,-r),z:=(z+u)%p)for i in range(n)];return z%p

test('''
2916. Subarrays Distinct Element Sum of Squares II
Hard
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
5,600/22.9K
Acceptance Rate
24.5%
Topics
Principal
Array
Hash Table
Binary Indexed Tree
Segment Tree
Biweekly Contest 116
icon
Companies
Hint 1
Consider the sum of the count of distinct values of subarrays ending with index i, let’s call it sum. Now if you need the sum of all subarrays ending with index i + 1 think how it can be related to sum and what extra will be needed to add to this.
Hint 2
You can find that extra sum using the segment tree.
''')
