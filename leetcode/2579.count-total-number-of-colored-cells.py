from lc import *

# https://leetcode.com/problems/count-total-number-of-colored-cells/solutions/4469467/one-line-mathematical-solution-very-easy/?envType=daily-question&envId=2025-03-05

class Solution:
    def coloredCells(self, n: int) -> int:
        return(n**2-n)*2+1

class Solution:
    def coloredCells(self, n: int) -> int:
        return n*(n-1)*2+1

class Solution:
    def coloredCells(self, n: int) -> int:
        return~-n*n*2+1

test('''
2579. Count Total Number of Colored Cells
Solved
Medium
Topics
Companies
Hint
There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

At the first minute, color any arbitrary unit cell blue.
Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.


Return the number of colored cells at the end of n minutes.

 

Example 1:

Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
Example 2:

Input: n = 2
Output: 5
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 
 

Constraints:

1 <= n <= 105
Seen this question in a real interview before?
1/5
Yes
No
Accepted
29.2K
Submissions
50.2K
Acceptance Rate
58.2%
Topics
Math
Companies
Hint 1
Derive a mathematical relation between total number of colored cells and the time elapsed in minutes.
Similar Questions
Minimum Cuts to Divide a Circle
Easy
''')
