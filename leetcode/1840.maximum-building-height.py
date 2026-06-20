from lc import *

# https://leetcode.com/problems/maximum-building-height/solutions/2936632/python-6-lines-by-mfatihuslu-v92x/?envType=daily-question&envId=2026-06-20

class Solution:
    def maxBuilding(self, n: int, a: List[List[int]]) -> int:
        a.sort(key=lambda i:i[0]+i[1])
        ans, b = 0, [1,0]
        for r in a:
            ans = max(ans,(min(2*n-b[0]+b[1],r[0]+r[1])-(b[0]-b[1]))//2)
            if b[0]-b[1] < r[0]-r[1]: b = [r[0],r[1]]
        return max(ans,n-b[0]+b[1])

class Solution:
    def maxBuilding(self, n: int, a: List[List[int]]) -> int:
        m=max;s,d=0,1;[s:=m(s,(min(2*n-d,x+y)-d)//2)+0*(d:=m(d,x-y))for x,y in sorted(a,key=sum)];return m(s,n-d)

test('''
1840. Maximum Building Height
Hard
Topics
premium lock icon
Companies
Hint
You want to build n new buildings in a city. The new buildings will be built in a line and are labeled from 1 to n.

However, there are city restrictions on the heights of the new buildings:

The height of each building must be a non-negative integer.
The height of the first building must be 0.
The height difference between any two adjacent buildings cannot exceed 1.
Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi, maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.

It is guaranteed that each building will appear at most once in restrictions, and building 1 will not be in restrictions.

Return the maximum possible height of the tallest building.

 

Example 1:


Input: n = 5, restrictions = [[2,1],[4,1]]
Output: 2
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.
Example 2:


Input: n = 6, restrictions = []
Output: 5
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.
Example 3:


Input: n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
Output: 5
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a height of 5.
 

Constraints:

2 <= n <= 109
0 <= restrictions.length <= min(n - 1, 105)
2 <= idi <= n
idi is unique.
0 <= maxHeighti <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
9,896/25.6K
Acceptance Rate
38.7%
Topics
Senior Staff
Array
Math
Sorting
Weekly Contest 238
icon
Companies
Hint 1
Is it possible to find the max height if given the height range of a particular building?
Hint 2
You can find the height range of a restricted building by doing 2 passes from the left and right.
Similar Questions
Find Maximum Value in a Constrained Sequence
Medium
''')
