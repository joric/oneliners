from lc import *

# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/?envType=daily-question&envId=2025-09-08

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return next([a,n-a]for a in range(n)if'0'not in f'{a}{n-a}')

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return[[a,n-a]for a in range(n)if'0'not in f'{a}{n-a}'][0]

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return[x for a in range(n)if'0'not in str(x:=(a,n-a))][0]

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        return[x for a in range(n)if{'0'}-{*str(x:=(a,n-a))}][0]

test('''
1317. Convert Integer to the Sum of Two No-Zero Integers
Solved
Easy
Topics
premium lock icon
Companies
Hint
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

 

Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.
 

Constraints:

2 <= n <= 104
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
60,767/111.8K
Acceptance Rate
54.4%
Topics
Math
Weekly Contest 171
icon
Companies
Hint 1
Loop through all elements from 1 to n.
Hint 2
Choose A = i and B = n - i then check if A and B are both No-Zero integers.
''')
