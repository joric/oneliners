from lc import *

# https://leetcode.com/problems/circle-and-rectangle-overlapping/description/?envType=daily-question&envId=2026-09-19

class Solution:
    def checkOverlap(self, r: int, x: int, y: int, a: int, b: int, c: int, d: int) -> bool:
        return(x-max(a,min(x,c)))**2+(y-max(b,min(y,d)))**2<=r*r

class Solution:
    def checkOverlap(self, r: int, x: int, y: int, a: int, b: int, c: int, d: int) -> bool:
        return hypot(x-max(a,min(x,c)),y-max(b,min(y,d)))<=r

class Solution:
    def checkOverlap(self, r: int, x: int, y: int, a: int, b: int, c: int, d: int) -> bool:
        return max(0,a-x,x-c)**2+max(0,b-y,y-d)**2<=r*r

test('''
1401. Circle and Rectangle Overlapping
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.

 

Example 1:


Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).
Example 2:

Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false
Example 3:


Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true
 

Constraints:

1 <= radius <= 2000
-104 <= xCenter, yCenter <= 104
-104 <= x1 < x2 <= 104
-104 <= y1 < y2 <= 104
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
25,747/50.9K
Acceptance Rate
50.6%
Topics
Staff
Math
Geometry
Biweekly Contest 23
icon
Companies
Hint 1
Locate the closest point of the square to the circle, you can then find the distance from this point to the center of the circle and check if this is less than or equal to the radius.
''')
