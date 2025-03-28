from lc import *

# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid

class Solution:
    def minOperations(self, g: List[List[int]], x: int) -> int:
        m=median(a:=reduce(add,g));return[int(sum(abs(v-m) for v in a)/x),-1][any((v-a[0])%x for v in a)]

test('''
2033. Minimum Operations to Make a Uni-Value Grid
Solved
Medium
Topics
Companies
Hint
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

A uni-value grid is a grid where all the elements of it are equal.

Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

 

Example 1:


Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.
Example 2:


Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.
Example 3:


Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= x, grid[i][j] <= 104
Seen this question in a real interview before?
1/5
Yes
No
Accepted
132.9K
Submissions
196.9K
Acceptance Rate
67.5%
Topics
Array
Math
Sorting
Matrix
Companies
Hint 1
Is it possible to make two integers a and b equal if they have different remainders dividing by x?
Hint 2
If it is possible, which number should you select to minimize the number of operations?
Hint 3
What if the elements are sorted?
Similar Questions
Minimum Moves to Equal Array Elements II
Medium
''')
