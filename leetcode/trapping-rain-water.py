from lc import *

# https://leetcode.com/problems/trapping-rain-water
# https://www.hackerrank.com/contests/knitopencontest/challenges/rain-harvester/problem

class Solution:
    def trap(self, h: List[int]) -> int:
        v=w=l=0;r=len(h)-1
        while l<r:
            if h[l]<h[r]:
                m = h[l]
                l +=1
            else:
                m = h[r]
                r -= 1
            v = max(v,m)
            w += v - m
        return w

class Solution:
    def trap(self, h: List[int]) -> int:
        v=w=l=0;r=len(h)-1
        while l<r:
            m = h[(l:=l+1)-1 if h[l]<h[r]else(r:=r-1)+1]
            v = max(v,m)
            w = w+v-m
        return w

class Solution:
    def trap(self, h: List[int]) -> int:
        v=w=l=0;r=len(h)-1;return next(w for _ in h if not(l<r and(m:=h[(l:=l+1)-1 if h[l]<h[r]else(r:=r-1)+1],v:=max(v,m),w:=w+v-m)))

# borderline TLE, 9678 ms
# https://leetcode.com/problems/trapping-rain-water/discuss/3848508/One-Line-Simple-Pyhton-Code

class Solution:
    def trap(self, h: List[int]) -> int:
        return sum(min(max(h[:i+1]),max(h[i:]))-x for i,x in enumerate(h))

# updated 2024-04-12
# https://leetcode.com/problems/trapping-rain-water/discuss/3848508/One-Line-Simple-Pyhton-Code

class Solution:
    def trap(self, h: List[int]) -> int:
        l,r=[*accumulate(h,max)],[*accumulate(h[::-1],max)][::-1]
        return sum([max(0,min(l[i],r[i])-x)for i,x in enumerate(h)])

class Solution:
    def trap(self, h: List[int]) -> int:
        a=accumulate;return sum(min(x)-h[i]for i,x in enumerate(zip(a(h,max),[*a(h[::-1],max)][::-1])))

class Solution:
    def trap(self, h: List[int]) -> int:
        a=accumulate;return sum(map(min,zip(a(h,max),[*a(h[::-1],max)][::-1])))-sum(h)

class Solution:
    def trap(self, h: List[int]) -> int:
        a=accumulate;return sum(map(min,a(h,max),[*a(h[::-1],max)][::-1]))-sum(h)

test('''
42. Trapping Rain Water

Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
1 <= n <= 2 * 10**4
0 <= height[i] <= 10**5
''')
