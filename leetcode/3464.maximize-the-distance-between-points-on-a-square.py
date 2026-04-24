from lc import *

# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/solutions/6475567/python3-flatten-and-bisect_left-ts-88-99-369r/?envType=daily-question&envId=2026-04-25

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        def flatten(p: list) -> int:
            x, y = p
            if y == 0   : return x
            if x == side: return side + y
            if y == side: return 3 * side  - x
            if x == 0   : return 4 * side  - y
        def notValid(mnDist: int) -> bool:
            for i, num in enumerate(arr):
                ptr, cnt = i, 1
                while cnt < k:
                    j = bisect_left(arr, arr[ptr] + mnDist)
                    if j == len(points): break
                    ptr = j
                    cnt += 1
                    if mnDist + arr[ptr] > num + 4 * side:
                        cnt = 0
                        break
                if cnt == k:
                    return False
            return True
        arr = sorted(map(flatten, points))
        firstFalse = bisect_left(range(0, side + 1), True, key = notValid)
        return firstFalse - 1

class Solution:
    def maxDistance(self, s: int, p: List[List[int]], k: int) -> int:
        def f(d):
            a=sorted(x if y==0 else s+y if x==s else 3*s-x if y==s else 4*s-y for x,y in p)
            for i,n in enumerate(a):
                t=i
                c=1
                while c<k:
                    j = bisect_left(a, a[t] + d)
                    if j==len(p):
                        break
                    t = j
                    c = c+1
                    if d+a[t]>n+4*s:
                        c = 0
                        break
                if c==k:
                    return False
            return True
        return bisect_left(range(0,s+1),1,key=f)-1

class Solution:
    def maxDistance(self, s: int, p: List[List[int]], k: int) -> int:
        def f(d):
            a=sorted(x if y==0 else s+y if x==s else 3*s-x if y==s else 4*s-y for x,y in p)
            for i,n in enumerate(a):
                c=(g:=lambda t,c:c if c>=k else((j:=bisect_left(a,a[t]+d))==len(p)and c)or(d+a[j]>n+4*s and 0)or g(j,c+1))(i,1)
                if c==k:
                    return False
            return True
        return bisect_left(range(0,s+1),1,key=f)-1

class Solution:
    def maxDistance(self, s: int, p: List[List[int]], k: int) -> int:
        return bisect_left(range(s+1),1,key=(f:=lambda d,a=sorted(x if y==0 else s+y if x==s else 3*s-x if y==s else 4*s-y for x,y in p):all((g:=lambda t,c:c if c>=k else((j:=bisect_left(a,a[t]+d))==len(p)and c or(d+a[j]>n+4*s and-1)or g(j,c+1)))(i,1)!=k for i,n in enumerate(a))))-1

class Solution:
    def maxDistance(self, s: int, p: List[List[int]], k: int) -> int:
        b=bisect_left;return b(range(s+1),1,key=lambda d,a=sorted(x+y if 0 in(y,s-x)else 4*s-x-y for x,y in p):all((g:=lambda t,c:(c==k or(j:=b(a,a[t]+d))==len(a))and c or(d+a[j]>n+4*s and-1)or g(j,c+1))(i,1)<k for i,n in enumerate(a)))-1

test('''
3464. Maximize the Distance Between Points on a Square
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer side, representing the edge length of a square with corners at (0, 0), (0, side), (side, 0), and (side, side) on a Cartesian plane.

You are also given a positive integer k and a 2D integer array points, where points[i] = [xi, yi] represents the coordinate of a point lying on the boundary of the square.

You need to select k elements among points such that the minimum Manhattan distance between any two points is maximized.

Return the maximum possible minimum Manhattan distance between the selected k points.

The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|.

 

Example 1:

Input: side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4

Output: 2

Explanation:



Select all four points.

Example 2:

Input: side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4

Output: 1

Explanation:



Select the points (0, 0), (2, 0), (2, 2), and (2, 1).

Example 3:

Input: side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5

Output: 1

Explanation:



Select the points (0, 0), (0, 1), (0, 2), (1, 2), and (2, 2).

Other examples:

Input: side = 9, points = [[8,0],[5,9],[2,0],[4,9],[0,1]], k = 4
Output: 3

Constraints:

1 <= side <= 109
4 <= points.length <= min(4 * side, 15 * 103)
points[i] == [xi, yi]
The input is generated such that:
points[i] lies on the boundary of the square.
All points[i] are unique.
4 <= k <= min(25, points.length)
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
4,623/19.1K
Acceptance Rate
24.3%
Topics
Principal
Array
Math
Binary Search
Geometry
Sorting
Weekly Contest 438
icon
Companies
Hint 1
Can we use binary search for this problem?
Hint 2
Think of the coordinates on a straight line in clockwise order.
Hint 3
Binary search on the minimum Manhattan distance x.
Hint 4
During the binary search, for each coordinate, find the immediate next coordinate with distance >= x.
Hint 5
Greedily select up to k coordinates.
Similar Questions
Maximum Number of Integers to Choose From a Range II
Medium
Maximum Points Inside the Square
Medium
''')
