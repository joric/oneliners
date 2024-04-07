from lc import *

# https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/JavaC%2B%2BPython-One-Pass-Count-the-Open-Parenthesis

class Solution:
    def checkValidString(self, s: str) -> bool:
        i=j=0
        for c in s:
            i += 1 if c=='(' else -1
            j += 1 if c!=')' else -1
            if j < 0:
                break
            i=max(i,0)
        return i==0

class Solution:
    def checkValidString(self, s: str) -> bool:
        i=j=0
        for c in s:
            i=max(0,i+(c=='(')*2-1)
            if(j:=j+(c!=')')*2-1)<0:
                return 0
        return i<1

# can't do next() because the stopiteration value is initialized first (uncoditional)
#class Solution:
#    def checkValidString(self, s: str) -> bool:
#        i=j=0;return next((0 for c in s if(i:=max(0,i+(c=='(')*2-1),(j:=j+(c!=')')*2-1)<0)[1]),i<1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        i=j=0;all((i:=i+(c=='(')*2-1,j:=j+(c!=')')*2-1)and j>=0 and[i:=max(i,0)]for c in s);return i==0

test('''
678. Valid Parenthesis String
Medium

5168

141

Add to List

Share
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
 

Other examples:

Input: s = "(((((()*)(*)*))())())(()())())))((**)))))(()())()"
Output: false

Input: s = "("
Output: false

Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
Accepted
255,272
Submissions
731,624
''')
