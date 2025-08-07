from lc import *

# https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/solutions/6080053/python3-12-lines-recursion-dp-t-s-76-64/?envType=daily-question&envId=2025-08-07

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:   
        @lru_cache(9000)
        def dp(row: int, col: int)-> int:
            if 0 <= col < row < n:                                  
                return fruits[row][col] + max(dp(row-1, col+1),
                                              dp(row  , col+1),
                                              dp(row+1, col+1))
            return 0
        n = len(fruits)
        diag = sum(map(lambda x:fruits[x][x], range(n)))    # <= 1)
        upper = dp(n - 1, 0)                                # <= 2)
        dp.cache_clear()                                    # <= 3)
        fruits = list(zip(*fruits))                         # 
        lower = dp(n - 1, 0)                                # 
        return diag + upper + lower                         # <= 4)

class Solution:
    def maxCollectedFruits(self, f: List[List[int]]) -> int:
        n,g=len(f),cache(lambda i,j:0<=j<i<n and f[i][j]+max(g(i-1,j+1),g(i,j+1),g(i+1,j+1))or 0);return sum(f[i][i]for i in range(n))+g(n-1,0)+(g.cache_clear(),f:=[*zip(*f)],g(n-1,0))[2]

test('''
3363. Find the Maximum Number of Fruits Collected
Hard
Topics
premium lock icon
Companies
Hint
There is a game dungeon comprised of n x n rooms arranged in a grid.

You are given a 2D array fruits of size n x n, where fruits[i][j] represents the number of fruits in the room (i, j). Three children will play in the game dungeon, with initial positions at the corner rooms (0, 0), (0, n - 1), and (n - 1, 0).

The children will make exactly n - 1 moves according to the following rules to reach the room (n - 1, n - 1):

The child starting from (0, 0) must move from their current room (i, j) to one of the rooms (i + 1, j + 1), (i + 1, j), and (i, j + 1) if the target room exists.
The child starting from (0, n - 1) must move from their current room (i, j) to one of the rooms (i + 1, j - 1), (i + 1, j), and (i + 1, j + 1) if the target room exists.
The child starting from (n - 1, 0) must move from their current room (i, j) to one of the rooms (i - 1, j + 1), (i, j + 1), and (i + 1, j + 1) if the target room exists.
When a child enters a room, they will collect all the fruits there. If two or more children enter the same room, only one child will collect the fruits, and the room will be emptied after they leave.

Return the maximum number of fruits the children can collect from the dungeon.

 

Example 1:

Input: fruits = [[1,2,3,4],[5,6,8,7],[9,10,11,12],[13,14,15,16]]

Output: 100

Explanation:



In this example:

The 1st child (green) moves on the path (0,0) -> (1,1) -> (2,2) -> (3, 3).
The 2nd child (red) moves on the path (0,3) -> (1,2) -> (2,3) -> (3, 3).
The 3rd child (blue) moves on the path (3,0) -> (3,1) -> (3,2) -> (3, 3).
In total they collect 1 + 6 + 11 + 16 + 4 + 8 + 12 + 13 + 14 + 15 = 100 fruits.

Example 2:

Input: fruits = [[1,1],[1,1]]

Output: 4

Explanation:

In this example:

The 1st child moves on the path (0,0) -> (1,1).
The 2nd child moves on the path (0,1) -> (1,1).
The 3rd child moves on the path (1,0) -> (1,1).
In total they collect 1 + 1 + 1 + 1 = 4 fruits.

 

Constraints:

2 <= n == fruits.length == fruits[i].length <= 1000
0 <= fruits[i][j] <= 1000
Seen this question in a real interview before?
1/5
Yes
No
Accepted
5,631/11.9K
Acceptance Rate
47.4%
Topics
Array
Dynamic Programming
Matrix
Biweekly Contest 144
icon
Companies
Hint 1
The child at (0, 0) has only one possible path.
Hint 2
The other two children won’t intersect its path.
Hint 3
Use Dynamic Programming.
''')
