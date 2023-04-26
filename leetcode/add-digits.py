from lc import *

class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            num = sum
        return num

class Solution:
    def addDigits(self, num):
        return 0 if num == 0 else (num - 1) % 9 + 1

class Solution:
    def addDigits(self, num):
        return (num - 1) - int((num-1)/9) * 9 + 1

class Solution:
    def addDigits(self, num):
        return num - int((num-1)/9) * 9

class Solution:
    def addDigits(self, num):
        return num and (num - 1) % 9 + 1

test('''
258. Add Digits
Easy

3490

1797

Add to List

Share
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Example 3:
Input: num = 9
Output: 9


Constraints:

0 <= num <= 231 - 1
 

Follow up: Could you do it without any loop/recursion in O(1) runtime?

Accepted
579,794
Submissions
899,169
Seen this question in a real interview before?

Yes

No
A naive implementation of the above process is trivial. Could you come up with other methods?
What are all the possible results?
How do they occur, periodically or randomly?
You may find this Wikipedia article useful.
''')

