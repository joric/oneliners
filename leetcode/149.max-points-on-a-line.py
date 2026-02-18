from lc import *

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        c = defaultdict(set)
        for p1, p2 in combinations(map(tuple, points), 2):
            m = inf if p1[0] == p2[0] else (p1[1]-p2[1]) / (p1[0]-p2[0])
            b = p1[0] if p1[0] == p2[0] else p1[1]-m*p1[0]
            c[(m, b)].update([p1, p2])
        return max((len(c[x]) for x in c), default=1)


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i,(x1,y1) in enumerate(points):
            c = Counter()
            for x2,y2 in points[i+1:]:
                c += Counter([(y1-y2)/(x1-x2) if x1-x2 else inf])
            res = max(list(c.values())+[res])
        return 1 + res

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        return 1 + reduce(lambda r,x:(f:=lambda i,a,r: max(list(reduce(lambda c,b:c+Counter({(a[1]-b[1])/(a[0]-b[0])
            if a[0]-b[0] else inf:1}), points[i+1:],Counter()).values())+[r]))(x[0],x[1],r), enumerate(points), 0)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        return 1 + reduce(lambda r,x: max(list(reduce(lambda c,b:c+Counter([(x[1][1]-b[1])/(x[1][0]-b[0])
            if x[1][0]-b[0] else inf]), points[x[0]+1:],Counter()).values())+[r]), enumerate(points), 0)

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        return (r:=0) or [r:=max(list(Counter([(y1-y2)/(x1-x2) if x1-x2 else inf for x2,y2
            in points[i+1:]]).values())+[r]) for i,(x1,y1) in enumerate(points)] and 1 + r

class Solution:
    def maxPoints(self, p: List[List[int]]) -> int:
        r=0;[r:=max([*Counter((b-d)/(a-c)if a-c else inf for c,d in p[i+1:]).values(),r])for i,(a,b) in enumerate(p)];return-~r

test('''
149. Max Points on a Line
Hard

1607

246

Add to List

Share
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Example 3:

Input: points = [[0,0]]
Output: 1

Constraints:

1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.
''')