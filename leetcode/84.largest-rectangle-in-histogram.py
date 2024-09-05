from lc import *

# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/4020253/8-Lines-solution.

class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        r = 0
        h += [0]
        q = [-1]
        for i in range(len(h)):
            while h[i] < h[q[-1]]:
                r = max(r, h[q.pop()]*(i-q[-1]-1))
            q.append(i)
        return r

class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        h+=[0];r,q=0,[-1];[(all(h[i]<h[q[-1]]and(r:=max(r,h[q.pop()]*(i-q[-1]-1)))for _ in h),q.append(i))for i in range(len(h))];return r

test('''
84. Largest Rectangle in Histogram
Hard

16794

263

Add to List

Share
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
Accepted
859,676
Submissions
1,942,904
''')