from lc import *

# https://leetcode.com/problems/first-completely-painted-row-or-column/solutions/6306014/one-line-solution/?envType=daily-question&envId=2025-01-20

class Solution:
    def firstCompleteIndex(self, a: List[int], g: List[List[int]]) -> int:
        d = {v:i for i,v in enumerate(a)}
        q = [[d[v] for v in r] for r in g]
        return min(map(max, q + [*zip(*q)]))

class Solution:
    def firstCompleteIndex(self, a: List[int], g: List[List[int]]) -> int:
        return (d:=dict(zip(a,count()))) and min(map(max,(q:=[[*map(d.get,r)] for r in g])+[*zip(*q)]))

class Solution:
    def firstCompleteIndex(self, a: List[int], g: List[List[int]]) -> int:
        d=dict(zip(a,count()));q=[[*map(d.get,r)]for r in g];return min(map(max,q+[*zip(*q)]))

test('''
2661. First Completely Painted Row or Column
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

Return the smallest index i at which either a row or a column will be completely painted in mat.

 

Example 1:

image explanation for example 1
Input: arr = [1,3,4,2], mat = [[1,4],[2,3]]
Output: 2
Explanation: The moves are shown in order, and both the first row and second column of the matrix become fully painted at arr[2].
Example 2:

image explanation for example 2
Input: arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]
Output: 3
Explanation: The second column becomes fully painted at arr[3].
 

Constraints:

m == mat.length
n = mat[i].length
arr.length == m * n
1 <= m, n <= 105
1 <= m * n <= 105
1 <= arr[i], mat[r][c] <= m * n
All the integers of arr are unique.
All the integers of mat are unique.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
138.4K
Submissions
214.4K
Acceptance Rate
64.5%
Topics
Array
Hash Table
Matrix
Companies
Hint 1
Can we use a frequency array?
Hint 2
Pre-process the positions of the values in the matrix.
Hint 3
Traverse the array and increment the corresponding row and column frequency using the pre-processed positions.
Hint 4
If the row frequency becomes equal to the number of columns, or vice-versa return the current index.
Similar Questions
Check if Every Row and Column Contains All Numbers
Easy
Difference Between Ones and Zeros in Row and Column
Medium
''')

