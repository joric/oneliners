from lc import *

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        e = sorted([(a,-x,b) for a,b,x in buildings]+[*{(b,0,None) for _,b,_ in buildings}])
        r = [[0, 0]]
        h = [(0, inf)]
        for x,n,b in e:
            while x>=h[0][1]:
                heappop(h)
            if n: 
                heappush(h,(n,b))
            if r[-1][1] + h[0][0]:
                r.append([x,-h[0][0]])
        return r[1:]

from sortedcontainers import SortedList

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        h = SortedList([0])
        s = []
        for x,y in sorted((x,y) for a,b,x in buildings for x, y in ((a,-x), (b,x))):
            if y<=0:
                h.add(y)
            else:
                h.remove(-y)
            if not s or -h[0] != s[-1][1]:
                s.append([x, -h[0]])
        return s

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        return (h:=__import__('sortedcontainers').SortedList([0]),s:=[],[(h.add(y) if y<=0 else h.remove(-y),(not s or -h[0]!=s[-1][1]) and s.append([x,-h[0]])) for x,y in sorted((x,y) for a,b,x in buildings for x, y in ((a,-x),(b,x)))],s)[-1]

test('''

218. The Skyline Problem
Hard

5174

240

Add to List

Share
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

 

Example 1:


Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]
 

Constraints:

1 <= buildings.length <= 10^4
0 <= lefti < righti <= 2^31 - 1
1 <= heighti <= 231 - 1
buildings is sorted by lefti in non-decreasing order.

''')