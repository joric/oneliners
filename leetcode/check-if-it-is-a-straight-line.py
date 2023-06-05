from lc import *

class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        (x1,y1),(x2,y2)=c[:2];return all((x-x1)*(y2-y1)==(x2-x1)*(y-y1)for x,y in c[2:])

class Solution(object):
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        return all((c[1][1]-c[0][1])*(x-c[0][0]) == (y-c[0][1])*(c[1][0]-c[0][0]) for x, y in c[2:])

class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        v=(np:=__import__('numpy')).sort(np.linalg.eigvals(np.cov(c,rowvar=False)))[::-1];return np.allclose(v[1:], 0)

class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        u=(np:=__import__('numpy')).subtract(c[0],c[1]);return all(np.cross(np.subtract(c[0],x),u)==0 for x in c[2:])

class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        (i,j),(u,v)=c[:2];return all((x-i)*(v-j)==(u-i)*(y-j)for x,y in c[2:])

test('''
1232. Check If It Is a Straight Line
Easy

1345

183

Add to List

Share
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Input: coordinates = [[0,0],[0,1],[0,-1]]
Output: true

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
Accepted
151,912
Submissions
378,460
Seen this question in a real interview before?

Yes

No
If there're only 2 points, return true.
Check if all other points lie on the line defined by the first 2 points.
Use cross product to check collinearity.
''')

