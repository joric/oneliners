from lc import *

# https://www.hackerrank.com/contests/knitopencontest/challenges/rain-harvester/problem

class Solution0:
    def trap(self, v: List[int]) -> int:
        lm,rm,l,r,res = 0,0,0,len(v)-1,0
        while l < r:
            lm = max(lm, v[l])
            rm = max(rm, v[r])
            if lm > rm:
                res += rm - v[r]
                r -= 1
            else:
                res += lm - v[l]
                l += 1
        return res

#TLE
class Solution:
    def trap(self, v: List[int]) -> int:
        return sum(max(0, (min(max(v[:i]), max(v[i+1:]))-v[i])) for i in range(1, len(v)-1))


class Solution:
    def trap(self, v: List[int]) -> int:
        return sum(min((a:=[c:=h if i==0 else max(c,h) for i,h in enumerate(v)] if i==0 else a)[len(v)-1-i],c:=h if i==0 else max(c,h))-h for i,h in enumerate(reversed(v)))

class Solution:
    def trap(self, v: List[int]) -> int:
        l = list(accumulate(v, max))
        r = list(accumulate(v[::-1], max))[::-1]
        return sum([max(0,min(l[i],r[i])-v[i]) for i in range(len(v))])

class Solution:
    def trap(self, v: List[int]) -> int:
        l = list(accumulate(v, max))
        r = list(accumulate(v[::-1], max))[::-1]
        return sum([max(0,min(l[i],r[i])-v[i]) for i in range(len(v))])

class Solution:
    def trap(self, v: List[int]) -> int:
        return sum([max(0,min([*accumulate(v, max)][i],[*accumulate(v[::-1],max)][::-1][i])-v[i]) for i in range(len(v))])


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
