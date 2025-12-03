from lc import *

# https://leetcode.com/problems/count-number-of-trapezoids-ii/solutions/6980653/python-parallel-lines-and-midpoints-by-a-5gr1/?envType=daily-question&envId=2025-12-03

class Solution:
    def countTrapezoids(self, A: List[List[int]]) -> int:
        slopes = Counter()
        lines = Counter()
        mids = Counter()
        midlines = Counter()

        for (x1, y1), (x2, y2) in combinations(A, 2):
            dx, dy = x2 - x1, y2 - y1
            g = gcd(dx, dy)
            dx, dy = dx // g, dy // g
            if dx < 0 or (dx == 0 and dy < 0):
                dx, dy = -dx, -dy

            inter = dx * y1 - dy * x1
            slopes[dx, dy] += 1
            lines[dx, dy, inter] += 1
            mids[x1 + x2, y1 + y2] += 1
            midlines[x1 + x2, y1 + y2, dx, dy, inter] += 1

        ans = sum(comb(v, 2) for v in slopes.values())
        ans -= sum(comb(v, 2) for v in lines.values())
        ans -= sum(comb(v, 2) for v in mids.values())
        ans += sum(comb(v, 2) for v in midlines.values())
        return ans

class Solution:
    def countTrapezoids(self, p: List[List[int]]) -> int:
        t=[Counter()for _ in[0]*4];
        for(a,b),(c,d)in combinations(p,2):
            (u:=c-a,v:=d-b,g:=gcd(u,v),u:=u//g,v:=v//g,(u<0 or u==0>v)and(u:=-u,v:=-v),i:=u*b-v*a,r:=(a+c,b+d))
            [t[j].update([p])for j,p in enumerate(((u,v),(u,v,i),r,(*r,u,v,i)))]
        return sum((1,-1,-1,1)[j]*sum(comb(v,2)for v in p.values())for j,p in enumerate(t))

class Solution:
    def countTrapezoids(self, p: List[List[int]]) -> int:
        t=[Counter()for _ in[0]*4];[(u:=c-a,v:=d-b,g:=gcd(u,v),u:=u//g,v:=v//g,(u<0 or u==0>v)and(u:=-u,v:=-v),i:=u*b-v*a,r:=(a+c,b+d),[t[j].update([p])for j,p in enumerate(((u,v),(u,v,i),r,(*r,u,v,i)))])for(a,b),(c,d)in combinations(p,2)];return sum((1,-1,-1,1)[j]*sum(comb(v,2)for v in p.values())for j,p in enumerate(t))

test('''
3625. Count Number of Trapezoids II
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.

A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.

 

Example 1:

Input: points = [[-3,2],[3,0],[2,3],[3,2],[2,-3]]

Output: 2

Explanation:



There are two distinct ways to pick four points that form a trapezoid:

The points [-3,2], [2,3], [3,2], [2,-3] form one trapezoid.
The points [2,3], [3,2], [3,0], [2,-3] form another trapezoid.
Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:



There is only one trapezoid which can be formed.

Other examples:

Input: points = [[34,88],[-62,-38],[26,88],[91,88],[47,-38]]
Output: 3

Input: points = [[71,-89],[-75,-89],[-9,11],[-24,-89],[-51,-89],[-77,-89],[42,11]]
Output: 10

Constraints:

4 <= points.length <= 500
–1000 <= xi, yi <= 1000
All points are pairwise distinct.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
4,804/35K
Acceptance Rate
13.7%
Topics
Array
Hash Table
Math
Geometry
Weekly Contest 459
icon
Companies
Hint 1
Hash every point-pair by its reduced slope (dy,dx) (normalize with GCD and fix signs).
Hint 2
In each slope-bucket of size k, there are C(k,2) ways to pick two segments as the trapezoid's parallel bases.
Hint 3
Skip any base-pair that shares an endpoint since it would not form a quadrilateral.
Hint 4
Subtract one count for each parallelogram. Each parallelogram was counted once for each of its two parallel-side pairs, so after subtracting once, every quadrilateral with at least one pair of parallel sides, including parallelograms, contributes exactly one to the final total.
Hint 5
Final answer = total valid base-pairs minus parallelogram overcounts.
''')
