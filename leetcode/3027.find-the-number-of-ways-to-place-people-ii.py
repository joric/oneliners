from lc import *

# biweekly-contest-123 Q4
# https://leetcode.com/contest/biweekly-contest-123/
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii
# similar to 3025 but with harder limits, 1000 and 10**9 instead of 50 and 50

class Solution:
    def numberOfPairs(self, p: List[List[int]]) -> int:
        r = 0
        p.sort(key=lambda p:(p[0],-p[1]))
        for i in range(len(p)):
            m = -inf
            for j in range(i+1,len(p)):
                if m<p[j][1]<=p[i][1]:
                    m = p[j][1]
                    r += 1
        return r

class Solution:
    def numberOfPairs(self, p: List[List[int]]) -> int:
        r=0;p.sort(key=lambda p:(p[0],-p[1]));[(m:=-inf,[m<p[j][1]<=p[i][1]and(m:=p[j][1],r:=r+1)for j in range(i+1,len(p))])for i in range(len(p))];return r

class Solution:
    def numberOfPairs(self, p: List[List[int]]) -> int:
        r,n=0,len(p);p.sort(key=lambda p:(p[0],-p[1]));[(m:=-inf,[m<(t:=p[j][1])<=p[i][1]and(m:=t,r:=r+1)for j in range(i+1,n)])for i in range(n)];return r

test('''
3027. Find the Number of Ways to Place People II
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

We define the right direction as positive x-axis (increasing x-coordinate) and the left direction as negative x-axis (decreasing x-coordinate). Similarly, we define the up direction as positive y-axis (increasing y-coordinate) and the down direction as negative y-axis (decreasing y-coordinate)

You have to place n people, including Alice and Bob, at these points such that there is exactly one person at every point. Alice wants to be alone with Bob, so Alice will build a rectangular fence with Alice's position as the upper left corner and Bob's position as the lower right corner of the fence (Note that the fence might not enclose any area, i.e. it can be a line). If any person other than Alice and Bob is either inside the fence or on the fence, Alice will be sad.

Return the number of pairs of points where you can place Alice and Bob, such that Alice does not become sad on building the fence.

Note that Alice can only build a fence with Alice's position as the upper left corner, and Bob's position as the lower right corner. For example, Alice cannot build either of the fences in the picture below with four corners (1, 1), (1, 3), (3, 1), and (3, 3), because:

With Alice at (3, 3) and Bob at (1, 1), Alice's position is not the upper left corner and Bob's position is not the lower right corner of the fence.
With Alice at (1, 3) and Bob at (1, 1), Bob's position is not the lower right corner of the fence.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 0
Explanation: There is no way to place Alice and Bob such that Alice can build a fence with Alice's position as the upper left corner and Bob's position as the lower right corner. Hence we return 0. 
Example 2:


Input: points = [[6,2],[4,4],[2,6]]
Output: 2
Explanation: There are two ways to place Alice and Bob such that Alice will not be sad:
- Place Alice at (4, 4) and Bob at (6, 2).
- Place Alice at (2, 6) and Bob at (4, 4).
You cannot place Alice at (2, 6) and Bob at (6, 2) because the person at (4, 4) will be inside the fence.
Example 3:


Input: points = [[3,1],[1,3],[1,1]]
Output: 2
Explanation: There are two ways to place Alice and Bob such that Alice will not be sad:
- Place Alice at (1, 1) and Bob at (3, 1).
- Place Alice at (1, 3) and Bob at (1, 1).
You cannot place Alice at (1, 3) and Bob at (3, 1) because the person at (1, 1) will be on the fence.
Note that it does not matter if the fence encloses any area, the first and second fences in the image are valid.
 

Constraints:

2 <= n <= 1000
points[i].length == 2
-109 <= points[i][0], points[i][1] <= 109
All points[i] are distinct.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
14,288/29.3K
Acceptance Rate
48.8%
Topics
Array
Math
Geometry
Sorting
Enumeration
Biweekly Contest 123
icon
Companies
Hint 1
Sort the points by x-coordinate in non-decreasing order and break the tie by sorting the y-coordinate in non-increasing order.
Hint 2
Now consider two points upper-left corner points[i] and lower-right corner points[j], such that i < j and points[i][0] <= points[j][0] and points[i][1] >= points[j][1].
Hint 3
Instead of brute force looping, we can save the largest y-coordinate that is no larger than points[i][1] when looping on j, say the value is m. And if m < points[j][1], the upper-left and lower-right corner pair is valid.
Hint 4
The actual values don’t matter, we can compress all x-coordinates and y-coordinates to the range [1, n]. Can we use prefix sum now?
''')
