from lc import *

# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/solutions/2017992/python-simple-dfs-with-cache-by-icomplex-wg95/?envType=daily-question&envId=2026-09-29

class Solution:
    def hasValidPath(self, g: List[List[str]]) -> bool:
        m,n=len(g),len(g[0]);f=cache(lambda x,y,r:(r:=r+(g[x][y]<")")*2-1)>=0 and(x==m-1 and y==n-1 and r==0 or x<m-1 and f(x+1,y,r) or y<n-1 and f(x,y+1,r)));return f(0,0,0)

class Solution:
    def hasValidPath(self, g: List[List[str]]) -> bool:
        m,n=len(g),len(g[0]);f=cache(lambda x,y,k:x<m and y<n and(v:=k+(g[x][y]<')')*2-1)>=0 and(x+y==m+n-2 and v<1 or f(x+1,y,v)or f(x,y+1,v)));return f(0,0,0)

class Solution:
    def hasValidPath(self, g: List[List[str]]) -> bool:
        m,n=len(g),len(g[0]);f=cache(lambda x,y,k:x<m and y<n and-1<(v:=k+(g[x][y]<')')*2-1)and((x+y+2==m+n)>v or f(x+1,y,v)or f(x,y+1,v)));return f(0,0,0)

class Solution:
    def hasValidPath(self, g: List[List[str]]) -> bool:
        return(f:=cache(lambda x,y,k,m=len(g),n=len(g[0]):x<m and y<n and-1<(v:=k+(g[x][y]<')')*2-1)and((x+y+2==m+n)>v or f(x+1,y,v)or f(x,y+1,v))))(0,0,0)

class Solution:
    def hasValidPath(self, g: List[List[str]]) -> bool:
        return(f:=cache(lambda x,y,k,m=len(g),n=len(g[0]):x<m*(y<n)and-1<(v:=k+(g[x][y]<')')*2-1)and(v<(x+y+2==m+n)or f(x+1,y,v)or f(x,y+1,v))))(0,0,0)

test('''
2267. Check if There Is a Valid Parentheses String Path
Hard
Topics
premium lock icon
Companies
Hint
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given an m x n matrix of parentheses grid. A valid parentheses string path in the grid is a path satisfying all of the following conditions:

The path starts from the upper left cell (0, 0).
The path ends at the bottom-right cell (m - 1, n - 1).
The path only ever moves down or right.
The resulting parentheses string formed by the path is valid.
Return true if there exists a valid parentheses string path in the grid. Otherwise, return false.

 

Example 1:


Input: grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
Output: true
Explanation: The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.
Example 2:


Input: grid = [[")",")"],["(","("]]
Output: false
Explanation: The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is either '(' or ')'.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
21,768/53.3K
Acceptance Rate
40.9%
Topics
Senior Staff
Array
Dynamic Programming
Matrix
Bracket Sequences
Weekly Contest 292
icon
Companies
Hint 1
What observations can you make about the number of open brackets and close brackets for any prefix of a valid bracket sequence?
Hint 2
The number of open brackets must always be greater than or equal to the number of close brackets.
Hint 3
Could you use dynamic programming?
Similar Questions
Check if There is a Valid Path in a Grid
Medium
Check if a Parentheses String Can Be Valid
Medium
''')
