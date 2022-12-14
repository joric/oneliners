from lc import *

class Solution1:
    def generate(self, numRows):
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1,i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal

class Solution2:
    def generate(self, numRows):
            res = [[1]]
            for i in range(1, numRows):
                res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
            return res[:numRows]


class Solution3:
    def generate(self, numRows: int) -> List[List[int]]:
        return list(map(lambda i:list(map(lambda x:factorial(i)//factorial(x)//factorial(i-x),range(i+1))),range(numRows)))

class Solution:
    def generate(self, numRows):
        return reduce(lambda a,_:a+[list(map(lambda x,y:x+y,a[-1]+[0],[0]+a[-1]))],range(1,numRows),[[1]])[:numRows]

test('''
118. Pascal's Triangle
Easy

8267

275

Add to List

Share
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
''')
