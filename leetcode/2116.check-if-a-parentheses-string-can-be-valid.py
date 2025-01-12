from lc import *

# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/solutions/2931919/python3-solution-clean-concise/?envType=daily-question&envId=2025-01-12

class Solution:
    def canBeValid(self, s: str, l: str) -> bool:
        a=b=0
        for i,j in zip(s,l):
            a -= 1 if a and (j == '0' or i == ')') else -1
            b += 1 if j == '0' or i == '(' else -1
            if b < 0: return False
        return a == 0

class Solution:
    def canBeValid(self, s: str, l: str) -> bool:
        a=b=0;any((a:=a+(-1,1)[a and(j<'1'or'('<i)],b:=b+(-1,1)[j<'1'or')'>i],b<0)[2]for i,j in zip(s,l));return a==0

class Solution:
    def canBeValid(self, s: str, l: str) -> bool:
        a=b=0;any((a:=a+1-2*(a and(j<'1'or'('<i)),b:=b-1+2*(j<'1'or')'>i),b<0)[2]for i,j in zip(s,l));return a==0

test('''
2116. Check if a Parentheses String Can Be Valid
Medium
Topics
Companies
Hint
A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:

It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,

If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false.

 

Example 1:


Input: s = "))()))", locked = "010100"
Output: true
Explanation: locked[1] == '1' and locked[3] == '1', so we cannot change s[1] or s[3].
We change s[0] and s[4] to '(' while leaving s[2] and s[5] unchanged to make s valid.
Example 2:

Input: s = "()()", locked = "0000"
Output: true
Explanation: We do not need to make any changes because s is already valid.
Example 3:

Input: s = ")", locked = "0"
Output: false
Explanation: locked permits us to change s[0]. 
Changing s[0] to either '(' or ')' will not make s valid.
 

Other examples:

Input: s = "))))(())((()))))((()((((((())())((()))((((())()()))(()", locked = "101100101111110000000101000101001010110001110000000101"
Output: false

Constraints:

n == s.length == locked.length
1 <= n <= 105
s[i] is either '(' or ')'.
locked[i] is either '0' or '1'.
''')
