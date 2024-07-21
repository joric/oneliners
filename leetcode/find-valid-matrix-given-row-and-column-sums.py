from lc import *

# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/discuss/876845/JavaC%2B%2BPython-Easy-and-Concise-with-Prove

class Solution:
    def restoreMatrix(self, r: List[int], c: List[int]) -> List[List[int]]:
        m, n = len(r), len(c)
        a = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                a[i][j] = min(r[i], c[j])
                r[i] -= a[i][j]
                c[j] -= a[i][j]
        return a

# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/discuss/877105/Python3-100-time-solution-and-5-line-solution

class Solution:
    def restoreMatrix(self, r: List[int], c: List[int]) -> List[List[int]]:
        def f(i,j):
            x = min(r[i], c[j])
            r[i],c[j] = r[i]-x, c[j]-x
            return x
        return [[f(i,j) for j in range(len(c))] for i in range(len(r))]

class Solution:
    def restoreMatrix(self, r: List[int], c: List[int]) -> List[List[int]]:
        return[[(lambda i,j:(x:=min(r[i],c[j]),setitem(r,i,r[i]-x),setitem(c,j,c[j]-x))[0])(i,j)for j in range(len(c))]for i in range(len(r))]

class Solution:
    def restoreMatrix(self, r: List[int], c: List[int]) -> List[List[int]]:
        return[[(x:=min(r[i],c[j]),setitem(r,i,r[i]-x),setitem(c,j,c[j]-x))[0]for j in range(len(c))]for i in range(len(r))]

test('''
1605. Find Valid Matrix Given Row and Column Sums
Medium

1640

56

Add to List

Share
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

 

Example 1:

Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation: 
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]
Example 2:

Input: rowSum = [5,7,10], colSum = [8,6,8]
Output:  [[5,0,0],
          [3,4,0],
          [0,2,8]]

#Output: [[0,5,0], # TODO can't write check with modified args, deepcopy args
#         [6,1,0],
#         [2,0,8]]

Constraints:

1 <= rowSum.length, colSum.length <= 500
0 <= rowSum[i], colSum[i] <= 108
sum(rowSum) == sum(colSum)
Accepted
68,180
Submissions
84,522
''')
