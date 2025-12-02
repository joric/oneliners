from lc import *

# https://leetcode.com/problems/count-number-of-trapezoids-i/solutions/6987245/python3-combinatorics-and-algebra-ts-95-uh6yz/

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        counts = Counter(y for _, y in points).values()
        horizCnts = [comb(c,2) for c in counts]
        totalCnt = sum(horizCnts)
        squares = sum(map(mul, horizCnts, horizCnts))
        ans = (totalCnt * totalCnt//2) %1_000_000_007
        ans-= (squares//2) %1_000_000_007
        return ans %1_000_000_007

class Solution:
    def countTrapezoids(self, p: List[List[int]]) -> int:
        h=[comb(c,2)for c in Counter(y for _,y in p).values()];return((sum(h)**2-sum(map(mul,h,h)))//2)%(10**9+7)

# https://leetcode.com/problems/count-number-of-trapezoids-i/solutions/7386223/two-simple-lines-of-code-by-mikposp-famp/?envType=daily-question&envId=2025-12-02

class Solution:
    def countTrapezoids(self, a: List[List[int]]) -> int:
        b = [comb(v,2) for v in Counter(y for _,y in a).values()]
        return sum(map(mul,b[1:],accumulate(b)))%(10**9+7)

class Solution:
    def countTrapezoids(self, a: List[List[int]]) -> int:
        return sum(map(mul,(t:=[comb(v,2)for v in Counter(y for _,y in a).values()])[1:],accumulate(t)))%(10**9+7)

class Solution:
    def countTrapezoids(self, a: List[List[int]]) -> int:
        b=[comb(v,2)for v in Counter(y for _,y in a).values()];return sum(map(mul,b[1:],accumulate(b)))%(10**9+7)

# https://leetcode.com/problems/count-number-of-trapezoids-i/solutions/6980432/4-lines-of-code-python-beats-100-by-yjxz-hdlg/?envType=daily-question&envId=2025-12-02

class Solution:
    def countTrapezoids(self, p: List[List[int]]) -> int:
        t=r=0
        for n in Counter(y for _,y in p).values():
            c = comb(n,2)
            r += t*c
            t += c
        return r%(10**9+7)

class Solution:
    def countTrapezoids(self, p: List[List[int]]) -> int:
        t=0;return sum(c*((t:=t+c)-c)for c in[comb(n,2)for n in Counter(y for _,y in p).values()])%(10**9+7)

class Solution:
    def countTrapezoids(self, p: List[List[int]]) -> int:
        t=0;return sum((c:=comb(n,2))*((t:=t+c)-c)for n in Counter(y for _,y in p).values())%(10**9+7)

test('''
3623. Count Number of Trapezoids I
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3

Explanation:



There are three distinct ways to pick four points that form a horizontal trapezoid:

Using points [1,0], [2,0], [3,2], and [2,2].
Using points [2,0], [3,0], [3,2], and [2,2].
Using points [1,0], [3,0], [3,2], and [2,2].
Example 2:

Input: points = [[0,0],[1,0],[0,1],[2,1]]

Output: 1

Explanation:



There is only one horizontal trapezoid that can be formed.

Other examples:

Input: pointes = [[-99,-79],[30,-60],[-70,-60],[61,50]]
Output: 0

Constraints:

4 <= points.length <= 105
–108 <= xi, yi <= 108
All points are pairwise distinct.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
31,233/93.2K
Acceptance Rate
33.5%
Topics
Array
Hash Table
Math
Geometry
Weekly Contest 459
icon
Companies
Hint 1
For a line parallel to the x‑axis, all its points must share the same y‑coordinate.
Hint 2
Group the points by their y‑coordinate.
Hint 3
Choose two distinct groups (two horizontal lines), and from each group select two points to form a trapezoid.
''')
