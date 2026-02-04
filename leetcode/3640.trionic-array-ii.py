from lc import *

# https://leetcode.com/problems/trionic-array-ii/solutions/7040545/python3-five-states-ts-119-ms-30-mb-by-s-8l9m/

class Solution:
    def maxSumTrionic(self, a: List[int]) -> int:
        j = p = q = 0
        n, o = len(a), -inf
        s, x = a[0], inf

        for i, (l, r) in enumerate(pairwise(a)):
            if l>r:
                s += r

                if x>l:
                    x = l
                    continue

                p = i

                while j<q or j+1-p<0>a[j]:
                    s -= a[j]
                    j += 1

            elif l<r:
                s += r
                if x>l:
                    q = i
                if j<p<q<=i and s>o:
                    o = s
            else:
                s = r
                j = i+1
            x = l
        return o

class Solution:
    def maxSumTrionic(self, a: List[int]) -> int:
        j=p=q=0;n=len(a);s=a[0];o=-inf;x=inf
        for i,(l,r)in enumerate(pairwise(a)):
            if l>r:
                [s:=s+r,x>l and[x:=l]or(p:=i,all((j<q or j+1-p<0>a[j])and(s:=s-a[j],j:=j+1)for _ in a))]
            elif l<r:
                [s:=s+r,(x>l and[q:=i],(j<p<q<=i and s>o and(o:=s)))]
            else:
                (s:=r,j:=i+1)
            (x:=l)
        return o

class Solution:
    def maxSumTrionic(self, a: List[int]) -> int:
        j=p=q=0;n=len(a);s=a[0];o=-inf;x=inf;[(l>r and[s:=s+r,x>l and[x:=l]or(p:=i,all((j<q or j+1-p<0>a[j])and(s:=s-a[j],j:=j+1)for _ in a))]or l<r and[s:=s+r,(x>l and[q:=i],(j<p<q<=i and s>o and(o:=s)))]or[s:=r,j:=i+1],x:=l)for i,(l,r)in enumerate(pairwise(a))];return o

class Solution:
    def maxSumTrionic(self, a: List[int]) -> int:
        j=p=q=0;n=len(a);s=a[0];o=-inf;x=inf
        for i,(l,r)in enumerate(pairwise(a)):
            if l>r:
                [s:=s+r,x>l and[x:=l]or(p:=i,all((j<q or j+1-p<0>a[j])and(s:=s-a[j],j:=j+1)for _ in a))]
            elif l<r:
                [s:=s+r,(x>l and[q:=i],o:=(o,s)[j<p<q<=i and s>o])]
            else:
                (s:=r,j:=i+1)
            (x:=l)
        return o

class Solution:
    def maxSumTrionic(self, a: List[int]) -> int:
        j=p=q=0;s=a[0];o,x=-inf,inf;[(l==r and[s:=r,j:=i+1]or(s:=s+r,l>r and(x>l and[x:=l]or(p:=i,all((j<q or a[j]<0>j-p+1)and(s:=s-a[j],j:=j+1)for _ in a)))or(x>l and[q:=i],j<p<q<=i and s>o and(o:=s))),x:=l)for i,(l,r)in enumerate(zip(a,a[1:]))];return o

class Solution:
    def maxSumTrionic(self, a: List[int]) -> int:
        j=p=q=0;s=a[0];o,x=-inf,inf;[(l==r and[s:=r,j:=i+1]or(s:=s+r,l>r and(x>l and[x:=l]or(p:=i,all((j<q or a[j]<0>j-p+1)and(s:=s-a[j],j:=j+1)for _ in a)))or(x>l and[q:=i],j<p<q<=i and s>o and(o:=s))),x:=l)for i,(l,r)in enumerate(pairwise(a))];return o

class Solution:
    def maxSumTrionic(self, a: List[int]) -> int:
        j=p=q=0;s=a[0];o,x=-inf,inf;[(l==r and[s:=r,j:=i+1]or(s:=s+r,l>r and(x>l and[x:=l]or(p:=i,all((j<q or a[j]<0>j-p+1)and(s:=s-a[j],j:=j+1)for _ in a)))or(x>l and[q:=i],o:=(o,s)[j<p<q<=i!=s>o])),x:=l)for i,(l,r)in enumerate(pairwise(a))];return o

test('''
3640. Trionic Array II
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n.

A trionic subarray is a contiguous subarray nums[l...r] (with 0 <= l < r < n) for which there exist indices l < p < q < r such that:

nums[l...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...r] is strictly increasing.
Return the maximum sum of any trionic subarray in nums.

 

Example 1:

Input: nums = [0,-2,-1,-3,0,2,-1]

Output: -4

Explanation:

Pick l = 1, p = 2, q = 3, r = 5:

nums[l...p] = nums[1...2] = [-2, -1] is strictly increasing (-2 < -1).
nums[p...q] = nums[2...3] = [-1, -3] is strictly decreasing (-1 > -3)
nums[q...r] = nums[3...5] = [-3, 0, 2] is strictly increasing (-3 < 0 < 2).
Sum = (-2) + (-1) + (-3) + 0 + 2 = -4.
Example 2:

Input: nums = [1,4,2,7]

Output: 14

Explanation:

Pick l = 0, p = 1, q = 2, r = 3:

nums[l...p] = nums[0...1] = [1, 4] is strictly increasing (1 < 4).
nums[p...q] = nums[1...2] = [4, 2] is strictly decreasing (4 > 2).
nums[q...r] = nums[2...3] = [2, 7] is strictly increasing (2 < 7).
Sum = 1 + 4 + 2 + 7 = 14.

Other examples:

Input: nums = [1,4,2,2,3,1,2]
Output: 8

Input: nums = [2,993,-791,-635,-569]
Output: -431

Constraints:

4 <= n = nums.length <= 105
-109 <= nums[i] <= 109
It is guaranteed that at least one trionic subarray exists.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
14,766/48.8K
Acceptance Rate
30.3%
Topics
Array
Dynamic Programming
Weekly Contest 461
icon
Companies
Hint 1
Use dynamic programming
Hint 2
Let four arrays dp0...dp3 where dpk[i] is the max sum of a subarray ending at i after finishing k of the four phases (start -> inc -> dec -> inc)
Hint 3
Process each i>0
Hint 4
If nums[i] > nums[i‑1], set dp1[i]=max(dp1[i‑1]+nums[i], dp0[i‑1]+nums[i]), dp3[i]=max(dp3[i‑1]+nums[i], dp2[i‑1]+nums[i])
Hint 5
If nums[i] < nums[i‑1], set dp2[i]=max(dp2[i‑1]+nums[i], dp1[i‑1]+nums[i])
Hint 6
Always carry over dp0[i]=dp0[i‑1]+nums[i] when nums[i]>nums[i‑1]
Hint 7
Return the maximum value in dp3
''')
