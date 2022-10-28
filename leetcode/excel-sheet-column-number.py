from lc import *

class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum((ord(s[i])-64)*26**(len(s)-i-1) for i in range(len(s)))

test('''
171. Excel Sheet Column Number
Easy

3723

302

Add to List

Share
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

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

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
''')