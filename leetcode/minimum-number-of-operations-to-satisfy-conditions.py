from lc import *

# Q3. https://leetcode.com/contest/weekly-contest-394/
# https://leetcode.com/problems/minimum-number-of-operations-to-satisfy-conditions/

# jeffreyhu8
class Solution:
    def minimumOperations(self, g: List[List[int]]) -> int:
        n,d = len(g),[0]*10
        for v in zip(*g):
            c = Counter(v)
            d = [min(d[j]for j in range(10)if i!=j)+(n-c[i])for i in range(10)]
        return min(d)

class Solution:
    def minimumOperations(self, g: List[List[int]]) -> int:
        n,d=len(g),[0]*10;[(c:=Counter(v),d:=[min(d[j]for j in range(10)if i!=j)+(n-c[i])for i in range(10)])[1] for v in zip(*g)];return min(d)

test('''
3122. Minimum Number of Operations to Satisfy Conditions
Medium

25

4

Add to List

Share
You are given a 2D matrix grid of size m x n. In one operation, you can change the value of any cell to any non-negative number. You need to perform some operations such that each cell grid[i][j] is:

Equal to the cell below it, i.e. grid[i][j] == grid[i + 1][j] (if it exists).
Different from the cell to its right, i.e. grid[i][j] != grid[i][j + 1] (if it exists).
Return the minimum number of operations needed.

 

Example 1:

Input: grid = [[1,0,2],[1,0,2]]

Output: 0

Explanation:



All the cells in the matrix already satisfy the properties.

Example 2:

Input: grid = [[1,1,1],[0,0,0]]

Output: 3

Explanation:



The matrix becomes [[1,0,1],[1,0,1]] which satisfies the properties, by doing these 3 operations:

Change grid[1][0] to 1.
Change grid[0][1] to 0.
Change grid[1][2] to 1.
Example 3:

Input: grid = [[1],[2],[3]]

Output: 2

Explanation:



There is a single column. We can change the value to 1 in each cell using 2 operations.

 

Constraints:

1 <= n, m <= 1000
0 <= grid[i][j] <= 9
Accepted
4,954
Submissions
17,291
''')
