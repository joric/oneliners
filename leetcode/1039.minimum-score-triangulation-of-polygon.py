from lc import *

# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/solutions/3516984/5-line-recursive-solution-shortest-solution/?envType=daily-question&envId=2025-09-29

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        @cache 
        def optimal(start, end):
            if end - start == 1: return 0
            return min(optimal(start,k) + values[start]*values[k]*values[end] + optimal(k, end) for k in range(start+1, end))
        return(optimal(0, len(values)-1))

class Solution:
    def minScoreTriangulation(self, v: List[int]) -> int:
        return(f:=cache(lambda a:2<len(a)and min(f(a[:k+1])+a[0]*a[k]*a[-1]+f(a[k:])for k in range(1,len(a)-1))))(tuple(v))

class Solution:
    def minScoreTriangulation(self, v: List[int]) -> int:
        return(f:=cache(lambda i,j:j-i>1 and min(f(i,k)+v[i]*v[k]*v[j]+f(k,j)for k in range(i+1,j))))(0,len(v)-1)

test('''
1039. Minimum Score Triangulation of Polygon
Solved
Medium
Topics
premium lock icon
Companies
Hint
You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.

Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.

You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.

Return the minimum possible score that you can achieve with some triangulation of the polygon.

 

Example 1:


Input: values = [1,2,3]

Output: 6

Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:


Input: values = [3,7,4,5]

Output: 144

Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.

Example 3:


Input: values = [1,3,1,4,1,5]

Output: 13

Explanation: The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.

 

Constraints:

n == values.length
3 <= n <= 50
1 <= values[i] <= 100
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
65,651/108.2K
Acceptance Rate
60.7%
Topics
Array
Dynamic Programming
Weekly Contest 135
icon
Companies
Hint 1
Without loss of generality, there is a triangle that uses adjacent vertices A[0] and A[N-1] (where N = A.length). Depending on your choice K of it, this breaks down the triangulation into two subproblems A[1:K] and A[K+1:N-1].
''')
