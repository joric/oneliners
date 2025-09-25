from lc import *

# https://leetcode.com/problems/triangle/discuss/38827/One-liner-in-Python/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def combine_rows(lower_row, upper_row):
            return [upper + min(lower_left, lower_right)
                    for upper, lower_left, lower_right in
                    zip(upper_row, lower_row, lower_row[1:])]
        return reduce(combine_rows, triangle[::-1])[0]

class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        a=t[-1];[a:=[min(a[i],a[i+1])+b[i]for i in range(len(a)-1)]for b in t[-2::-1]];return a[0]

class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        return reduce(lambda a,b:[f+min(d,e)for d,e,f in zip(a,a[1:],b)],t[::-1])[0]

class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        return reduce(lambda a,b:[*map(add,map(min,a,a[1:]),b)],t[::-1])[0]

test('''
120. Triangle
Medium

9619

561

Add to List

Share
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
Accepted
831,660
Submissions
1,443,410
''')
