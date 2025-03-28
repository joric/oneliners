from lc import *

# TLE https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/6052964/Swift-or-Brute-force

class Solution:
    def shortestSubarray(self, a: List[int], k: int) -> int:
        n,t=len(a),inf
        for i in range(n):
            s = 0
            for j in range(i,n):
                s += a[j]
                if s>=k:
                    t = min(t,j-i+1)
                if s<=0 or s>=k:
                    break
        return(-1,t)[t<inf]

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/349161/Python-7-line-heap

class Solution:
    def shortestSubarray(self, a: List[int], k: int) -> int:
        h,t,s=[(0,-1)],inf,0
        for i,x in enumerate(a):
            s += x
            while h and s-k>=h[0][0]:
                t = min(t,i-heappop(h)[1])
            heappush(h,(s,i))
        return(-1,t)[t<inf]

class Solution:
    def shortestSubarray(self, a: List[int], k: int) -> int:
        h,t,s=[(0,-1)],inf,0;[(s:=s+x,all(h and s-k>=h[0][0]and(t:=min(t,i-heappop(h)[1]))for _ in a),heappush(h,(s,i)))for i,x in enumerate(a)];return(-1,t)[t<inf]

# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/discuss/6053014/Python-3-6-lines-an-extremely-simple-solution

class Solution:
    def shortestSubarray(self, a: List[int], k: int) -> int:
        h,t=[],inf
        for i,s in enumerate(accumulate(a, initial=0)):
            while h and s-k>=h[0][0]:
                t = min(t,i-heappop(h)[1])
            heappush(h,(s,i))
        return(-1,t)[t<inf]

class Solution:
    def shortestSubarray(self, a: List[int], k: int) -> int:
        h,t=[],inf;[(all(h and s-k>=h[0][0]and(t:=min(t,i-heappop(h)[1]))for _ in a),heappush(h,(s,i)))for i,s in enumerate(accumulate([0]+a))];return(-1,t)[t<inf]

test('''
862. Shortest Subarray with Sum at Least K
Hard

4441

122

Add to List

Share
Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
1 <= k <= 109
Accepted
115,530
Submissions
426,470
''')

