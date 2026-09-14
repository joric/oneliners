from lc import *

# https://leetcode.com/problems/rectangle-overlap/solutions/132340/cjavapython-1-line-solution-1d-to-2d-by-93h52/?envType=daily-question&envId=2026-09-14

class Solution:
    def isRectangleOverlap(self, a: List[int], b: List[int]) -> bool:
        return a[0]<b[2]and b[0]<a[2]and a[1]<b[3]and b[1]<a[3]

class Solution:
    def isRectangleOverlap(self, a: List[int], b: List[int]) -> bool:
        return all(map(lt,a[:2]+b[:2],b[2:]+a[2:]))

class Solution:
    def isRectangleOverlap(self, a: List[int], b: List[int]) -> bool:
        return all(map(lt,a[:2]+b,b[2:]+a[2:]))

test('''
836. Rectangle Overlap
Easy
Topics
premium lock icon
Companies
An axis-aligned rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) is the coordinate of its bottom-left corner, and (x2, y2) is the coordinate of its top-right corner. Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

Two rectangles overlap if the area of their intersection is positive. To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two axis-aligned rectangles rec1 and rec2, return true if they overlap, otherwise return false.

 

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true
Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false
Example 3:

Input: rec1 = [0,0,1,1], rec2 = [2,2,3,3]
Output: false
 

Constraints:

rec1.length == 4
rec2.length == 4
-109 <= rec1[i], rec2[i] <= 109
rec1 and rec2 represent a valid rectangle with a non-zero area.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
190,847/405.4K
Acceptance Rate
47.1%
Topics
Mid Level
Math
Geometry
Weekly Contest 85
icon
Companies
Similar Questions
Rectangle Area
Medium
''')
