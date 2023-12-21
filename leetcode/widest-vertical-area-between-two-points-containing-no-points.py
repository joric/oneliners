from lc import *

# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/discuss/4340708/One-line-solution
# similar to https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores

class Solution:
    def maxWidthOfVerticalArea(self, p: List[List[int]]) -> int:
        return max(b-a for a,b in pairwise(sorted(next(zip(*p)))))

class Solution:
    def maxWidthOfVerticalArea(self, p: List[List[int]]) -> int:
        p=sorted(next(zip(*p)));return max(map(sub,p[1:],p))

test('''
1637. Widest Vertical Area Between Two Points Containing No Points
Medium

333

739

Add to List

Share
Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.

 

Example 1:

​
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.
Example 2:

Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3
 

Constraints:

n == points.length
2 <= n <= 10^5
points[i].length == 2
0 <= xi, yi <= 10^9
Accepted
45,489
Submissions
53,718
''')
