from lc import *

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/discuss/2034481/Python-One-Liner-(-Just-For-Fun!!-)

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        return (p:=inf) and sum( ((p:=e) or 1) and 1 if not s<=p<=e else 0 for s,e in sorted(points,key=itemgetter(1)))

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        return (p:=inf) and sum(not s<=p<=e and bool(p:=e) for s,e in sorted(points,key=itemgetter(1)))

# another solution

class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        s,c = 0,inf
        for a,b in sorted(p):
            if a>c:
                s += 1
                c = b
            else:
                c = min(c,b)
        return s+1

class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        c=inf;return 1+sum((c:=(min(c,b),b)[t:=a>c])*0+t for a,b in sorted(p))

# updated 2024-03-18

class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        c=inf;return sum(not(a<=c<=b or(c:=b)==0)for a,b in sorted(p,key=itemgetter(1)))

class Solution:
    def findMinArrowShots(self, p: List[List[int]]) -> int:
        c=inf;return sum(c>b and(c:=a)*0+1 for a,b in[*sorted(p)][::-1])

test('''
452. Minimum Number of Arrows to Burst Balloons
Medium

3974

116

Add to List

Share
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
 

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.

Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
 

Constraints:

1 <= points.length <= 10^5
points[i].length == 2
-2^31 <= xstart < xend <= 2^31 - 1

''')