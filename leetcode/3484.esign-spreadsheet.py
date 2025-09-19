from lc import *

# https://leetcode.com/problems/design-spreadsheet/solutions/7203813/clean-explanation-example-walkthrough-c-python-java/?envType=daily-question&envId=2025-09-19

class Spreadsheet:
    def __init__(self, r: int):
        self.t = {}
    def setCell(self, c: str, v: int) -> None:
        self.t[c] = v
    def resetCell(self, c: str) -> None:
        self.t[c] = 0
    def getValue(self, f: str) -> int:
        return next((sum(self.t.get(a,0)if a[0].isupper()else int(a)for a in(f[1:i],f[i+1:]))for i in range(1,len(f))if f[i]=='+'),0)

# https://leetcode.com/problems/design-spreadsheet/solutions/7204325/solution-of-the-day/?envType=daily-question&envId=2025-09-19

class Spreadsheet:
    def __init__(self, r: int):
        self.d = {}
    def setCell(self, c: str, v: int) -> None:
        self.d[c] = v
    def resetCell(self, c: str) -> None:
        self.d[c] = 0
    def getValue(self, f: str) -> int:
        return sum(self.d.get(c,c.isdigit()and int(c))for c in f.split('=')[1].split('+'))

Spreadsheet=type('',(),{'__init__':lambda s,r:setattr(s,'d',{})or None,'setCell':lambda s,c,v:setitem(s.d,c,v),'resetCell':lambda s,c:setitem(s.d,c,0),'getValue':lambda s,f:sum(s.d.get(c,c.isdigit()and int(c))for c in f.split('=')[1].split('+'))})

test('''
3484. Design Spreadsheet
Medium
Topics
premium lock icon
Companies
Hint
A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. Each cell in the spreadsheet can hold an integer value between 0 and 105.

Implement the Spreadsheet class:

Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and the specified number of rows. All cells are initially set to 0.
void setCell(String cell, int value) Sets the value of the specified cell. The cell reference is provided in the format "AX" (e.g., "A1", "B10"), where the letter represents the column (from 'A' to 'Z') and the number represents a 1-indexed row.
void resetCell(String cell) Resets the specified cell to 0.
int getValue(String formula) Evaluates a formula of the form "=X+Y", where X and Y are either cell references or non-negative integers, and returns the computed sum.
Note: If getValue references a cell that has not been explicitly set using setCell, its value is considered 0.

 

Example 1:

Input:
["Spreadsheet", "getValue", "setCell", "getValue", "setCell", "getValue", "resetCell", "getValue"]
[[3], ["=5+7"], ["A1", 10], ["=A1+6"], ["B2", 15], ["=A1+B2"], ["A1"], ["=A1+B2"]]

Output:
[null, 12, null, 16, null, 25, null, 15]

Explanation

Spreadsheet spreadsheet = new Spreadsheet(3); // Initializes a spreadsheet with 3 rows and 26 columns
spreadsheet.getValue("=5+7"); // returns 12 (5+7)
spreadsheet.setCell("A1", 10); // sets A1 to 10
spreadsheet.getValue("=A1+6"); // returns 16 (10+6)
spreadsheet.setCell("B2", 15); // sets B2 to 15
spreadsheet.getValue("=A1+B2"); // returns 25 (10+15)
spreadsheet.resetCell("A1"); // resets A1 to 0
spreadsheet.getValue("=A1+B2"); // returns 15 (0+15)
 

Constraints:

1 <= rows <= 103
0 <= value <= 105
The formula is always in the format "=X+Y", where X and Y are either valid cell references or non-negative integers with values less than or equal to 105.
Each cell reference consists of a capital letter from 'A' to 'Z' followed by a row number between 1 and rows.
At most 104 calls will be made in total to setCell, resetCell, and getValue.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
53,230/74K
Acceptance Rate
71.9%
Topics
Array
Hash Table
String
Design
Matrix
Biweekly Contest 152
icon
Companies
Hint 1
Use a hashmap to represent the cells, where the key is the cell reference (e.g., "A1") and the value is the integer stored in the cell.
Hint 2
For setCell, simply assign the given value to the specified cell in the hashmap.
Hint 3
For resetCell, set the value of the specified cell to 0 in the hashmap.
Hint 4
For getValue, find the values of the operands from the hashmap and return their sum.
Similar Questions
Excel Sheet Column Title
Easy
''', Spreadsheet)
