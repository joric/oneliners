from lc import *

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        while columnNumber > 0:
            result.append(capitals[(columnNumber-1)%26])
            columnNumber = (columnNumber-1) // 26
        result.reverse()
        return ''.join(result)

class Solution:
    def convertToTitle(self, n: int) -> str:
        return self.convertToTitle((n-1)//26)+chr(65+(n-1)%26) if n>0 else ''

class Solution:
    def convertToTitle(self, n: int) -> str:
        return n>0and self.convertToTitle((n-1)//26)+chr(65+(n-1)%26)or''

class Solution:
    def convertToTitle(self, n: int) -> str:
        return(f:=lambda n:n>0and f((n-1)//26)+chr(65+(n-1)%26)or'')(n)

test('''
168. Excel Sheet Column Title
Easy

4121

585

Add to List

Share
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnNumber = 1
Output: "A"
Example 2:

Input: columnNumber = 28
Output: "AB"
Example 3:

Input: columnNumber = 701
Output: "ZY"
 

Constraints:

1 <= columnNumber <= 2^31 - 1
''')

