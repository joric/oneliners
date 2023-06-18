from lc import *

# https://leetcode.com/problems/equal-row-and-column-pairs/discuss/2347364/Python-3-one-line-two-solutions

class Solution:
    def equalPairs(self, g: List[List[int]]) -> int:
        return sum(map(Counter(map(tuple,g)).__getitem__,zip(*g)))

class Solution:
    def equalPairs(self, g: List[List[int]]) -> int:
        return sum(r==c for c in map(list,zip(*g))for r in g)

class Solution:
    def equalPairs(self, g: List[List[int]]) -> int:
        return sum(r==[*c]for r in g for c in zip(*g))

class Solution:
    def equalPairs(self, g):
        return sum(Counter(zip(*g))[*c] for c in g)

test('''
2352. Equal Row and Column Pairs
Medium

557

27

Add to List

Share
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 10^5
Accepted
42,207
Submissions
59,643
Seen this question in a real interview before?

Yes

No
We can use nested loops to compare every row against every column.
Another loop is necessary to compare the row and column element by element.
It is also possible to hash the arrays and compare the hashed values instead.
''')

