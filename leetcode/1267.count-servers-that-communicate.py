from lc import *

# https://leetcode.com/problems/count-servers-that-communicate/solutions/6319218/one-line-solution/?envType=daily-question&envId=2025-01-23

class Solution:
    def countServers(self, g: List[List[int]]) -> int:
        p,q,e=[*map(sum,g)],[*map(sum,zip(*g))],enumerate;return sum(2<p[i]+q[j]for i,r in e(g)for j,v in e(r)if v)

test('''
1267. Count Servers that Communicate
Solved
Medium
Topics
Companies
Hint
You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
Seen this question in a real interview before?
1/5
Yes
No
Accepted
113.8K
Submissions
165.5K
Acceptance Rate
68.8%
Topics
Array
Depth-First Search
Breadth-First Search
Union Find
Matrix
Counting
Companies
Hint 1
Store number of computer in each row and column.
Hint 2
Count all servers that are not isolated.
''')
