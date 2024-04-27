from lc import *

# Q1. https://leetcode.com/contest/biweekly-contest-129/
# https://leetcode.com/problems/make-a-square-with-the-same-color

# https://leetcode.com/problems/make-a-square-with-the-same-color/discuss/5080163/Python-3-oror-4-lines-Counter-oror-TS%3A-23-ms-16.7-MB

class Solution:
    def canMakeSquare(self, g: List[List[str]]) -> bool:
        return any(2<max(Counter((g[i][j]+g[i][j+1]+g[i+1][j]+g[i+1][j+1])).values())for i,j in product((0,1),(0,1)))

# https://leetcode.com/problems/make-a-square-with-the-same-color/discuss/5081338/Simple-Python-solution

class Solution:
    def canMakeSquare(self, g: List[List[str]]) -> bool:
        m=__import__('numpy').array(g)
        for i in(0,1):
            for j in(0,1):
                if (m[i:i+2,j:j+2]<'W').sum()!=2:
                    return True
        return False

class Solution:
    def canMakeSquare(self, g: List[List[str]]) -> bool:
        m=__import__('numpy').array(g);return any(2-(m[i:i+2,j:j+2]<'W').sum()for i in(0,1)for j in(0,1))

class Solution:
    def canMakeSquare(self, g: List[List[str]]) -> bool:
        r=(0,1);return any(2-sum('W'>g[i+x][j+y]for x in r for y in r)for i in r for j in r)

class Solution:
    def canMakeSquare(self, g: List[List[str]]) -> bool:
        p=[*product(*[[0,1]]*2)];return any(2-sum('W'>g[i+x][j+y]for x,y in p)for i,j in p)

test('''
3127. Make a Square with the Same Color
Easy

0

0

Add to List

Share
You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'. Character 'W' represents the white color, and character 'B' represents the black color.

Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where all cells are of the same color.
Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.

Example 1:

Input: grid = [["B","W","B"],["B","W","W"],["B","W","B"]]

Output: true

Explanation:

It can be done by changing the color of the grid[0][2].

Example 2:

Input: grid = [["B","W","B"],["W","B","W"],["B","W","B"]]

Output: false

Explanation:

It cannot be done by changing at most one cell.

Example 3:

Input: grid = [["B","W","B"],["B","W","W"],["B","W","W"]]

Output: true

Explanation:

The grid already contains a 2 x 2 square of the same color.
 

More examples:

Input: grid = [["B","B","B"],["B","B","B"],["B","B","B"]]
Output: true

Input: grid = [["B","B","B"],["B","W","B"],["B","B","B"]]
Output: true

Input: grid = [["W","W","W"],["W","W","W"],["B","B","B"]]
Output: true

Constraints:

grid.length == 3
grid[i].length == 3
grid[i][j] is either 'W' or 'B'.
Accepted
13,872
Submissions
30,298
''')
