from lc import *

# https://leetcode.com/problems/largest-triangle-area/solutions/838730/1-line-python-solution-using-triangle-area-formula/?envType=daily-question&envId=2025-09-27

class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        return max(abs(a*(d-f)+c*(f-b)+e*(b-d))for(a,b),(c,d),(e,f)in combinations(p,3))/2

test('''
812. Largest Triangle Area
Solved
Easy
Topics
premium lock icon
Companies
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
 

Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
68,784/109.9K
Acceptance Rate
62.6%
Topics
Array
Math
Geometry
Weekly Contest 79
icon
Companies
Similar Questions
Largest Perimeter Triangle
Easy
''')
