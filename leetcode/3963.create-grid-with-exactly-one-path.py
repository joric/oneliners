from lc import *

# https://leetcode.com/problems/create-grid-with-exactly-one-path/solutions/8575470/one-line-solution-by-mikposp-wb58/?envType=daily-question&envId=2026-10-27

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return['.'*n]+['#'*(n-1)+'.']*(m-1)

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return['.'*n]+['#'*~-n+'.']*~-m

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return['.'+'#'*~-n]*~-m+['.'*n]

test('''
3963. Create Grid With Exactly One Path
Easy
premium lock icon
Companies
Hint
You are given two integers m and n, representing the number of rows and columns of a grid.

Construct any m x n grid consisting only of the characters '.' and '#', where:

'.' represents a free cell.
'#' represents an obstacle cell.
A valid path is a sequence of free cells that:

Starts at the top-left cell (0, 0).
Ends at the bottom-right cell (m - 1, n - 1).
Moves only:
Right, from (i, j) to (i, j + 1), or
Down, from (i, j) to (i + 1, j).
Return any grid such that there is exactly one valid path from the top-left cell to the bottom-right cell.

 

Example 1:

Input: m = 2, n = 3

Output: ["..#","#.."]

Explanation:



The only valid path is: (0,0) → (0,1) → (1,1) → (1,2)

Example 2:

Input: m = 3, n = 3

Output: ["..#","#..","##."]

Explanation:



The only valid path is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2)

Example 3:

Input: m = 1, n = 4

Output: ["...."]

Explanation:

The only valid path is: (0,0) → (0,1) → (0,2) → (0,3)

 

Constraints:

1 <= m, n <= 25
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
41,483/54.7K
Acceptance Rate
75.9%
Topics
Mid Level
Biweekly Contest 185
icon
Companies
Hint 1
It is enough to leave one simple route made of free cells and block every other cell.
Hint 2
There are many routes to choose from. What is the simplest one you can think of?
Hint 3
One possible route: Go right while possible, then go down till you reach the destination.
Similar Questions
Create Grid With Exactly K Paths I
Medium
''',check=lambda res,exp,m,n:len(res)==m and all(len(r)==n and set(r)<={'.','#'}for r in res)and reduce(lambda p,r:list(accumulate(zip(p,r),lambda a,x:(x[0]+a)*(x[1]=='.'),initial=0))[1:],res,[1]+[0]*(n-1))[-1]==1)
