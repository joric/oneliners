from lc import *

# https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def splitNum(num):           
            num = [int(d) for d in str(num)]
            pow = len(num)-1
            res = []
            for n in num:
                res.append(n*10**pow)
                pow -= 1
            return res     
        n1 = splitNum(num1)
        n2 = splitNum(num2)
        return str(sum([x*y for x in n1 for y in n2]))

class Solution:
    def multiply(self, a: str, b: str) -> str:
        return str(int(a)*int(b))

test('''
43. Multiply Strings
Medium

7115

3380

Add to List

Share
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
Accepted
844,820
Submissions
2,065,171
''')
