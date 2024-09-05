from lc import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]*(rowIndex+1)
        for i in range(1, len(dp)):
            dp[i] = dp[i-1] * (rowIndex - i + 1) // i 
        return dp

class Solution:
    def getRow(self, i: int) -> List[int]:
        f=factorial;return[f(i)//f(x)//f(i-x)for x in range(i+1)]

# O(n)
class Solution:
    def getRow(self, i: int) -> List[int]:
        return[a:=1]+[a:=a*(i-k)//(k+1)for k in range(i)]

# O(n) 2x faster
class Solution:
    def getRow(self, i: int) -> List[int]:
        r=[a:=1]+[a:=a*(i-k)//(k+1)for k in range(i>>1)];return r+r[::-1][1^i&1:]

# https://leetcode.com/problems/pascals-triangle-ii/discuss/207686/One-Line-Python-using-numpy

from numpy.polynomial.polynomial import polypow
class Solution(object):
    def getRow(self, i: int) -> List[int]:
        return[int(x)for x in polypow((1,1),i)]

# https://leetcode.com/problems/pascals-triangle-ii/discuss/788411/One-Line-Python-Using-Math

class Solution:
    def getRow(self, i: int) -> List[int]:
        return[comb(i,x)for x in range(i+1)]

test('''
119. Pascal's Triangle II
Easy

4187

312

Add to List

Share
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
''')