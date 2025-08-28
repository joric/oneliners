from lc import *

# https://leetcode.com/problems/sort-matrix-by-diagonals/solutions/7113503/three-simple-lines-of-code/?envType=daily-question&envId=2025-08-28

class Solution:
    def sortMatrix(self, g: List[List[int]]) -> List[List[int]]:
        r,d = range(len(g)),defaultdict(SortedList)
        for i,j in product(r,r): d[i-j].add(g[i][j])
        for i,j in product(r,r): g[i][j] = d[i-j].pop(-(i>=j))
        return g

class Solution:
    def sortMatrix(self, g: List[List[int]]) -> List[List[int]]:
        r = range(len(g))
        d = {k:[v for _,v in g][::1-(k<0)*2] for k,g in groupby(sorted(
            (i-j,g[i][j]) for i,j in product(r,r)),itemgetter(0))}
        return [[d[i-j].pop() for j in r] for i in r]

class Solution:
    def sortMatrix(self, g: List[List[int]]) -> List[List[int]]:
        r,d=range(len(g)),defaultdict(SortedList);[d[i-j].add(g[i][j])for i,j in product(r,r)];return[[d[i-j].pop(-(i>=j))for j in r]for i in r]

test('''
3446. Sort Matrix by Diagonals
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
 

Example 1:

Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output: [[8,2,3],[9,6,7],[4,5,1]]

Explanation:



The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

[1, 8, 6] becomes [8, 6, 1].
[9, 5] and [4] remain unchanged.
The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

[7, 2] becomes [2, 7].
[3] remains unchanged.
Example 2:

Input: grid = [[0,1],[1,2]]

Output: [[2,1],[1,0]]

Explanation:



The diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.

Example 3:

Input: grid = [[1]]

Output: [[1]]

Explanation:

Diagonals with exactly one element are already in order, so no changes are needed.

 

Constraints:

grid.length == grid[i].length == n
1 <= n <= 10
-105 <= grid[i][j] <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
30,285/42.6K
Acceptance Rate
71.0%
Topics
Array
Sorting
Matrix
Weekly Contest 436
icon
Companies
Hint 1
Use a data structure to store all values in each diagonal.
Hint 2
Sort and replace them in the matrix.
Similar Questions
Sort the Matrix Diagonally
Medium
''')
