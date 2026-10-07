from lc import *

# https://leetcode.com/problems/remove-outermost-parentheses/solutions/2779120/python-one-line-by-norelaxation-6apy/?envType=daily-question&envId=2026-10-08

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        return(lambda p:''.join(s[i]for i in range(len(s))if p[i]and p[i+1]))([*accumulate(map(lambda x:1 if x=='('else-1,s),initial=0)])

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        return(lambda p:''.join(c for c,a,b in zip(s,p,p[1:])if a*b))([*accumulate(s,lambda a,c:a+81-2*ord(c),initial=0)])

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        t = ''
        k = 0
        o = ''
        for c in s:
            k += 1 if c=='(' else -1
            o += c
            if k==0:
                t += o[1:-1]
                o = ''
        return t

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        return''.join(c for c,d in zip(s,accumulate(2*(c<')')-1for c in s))if d>(c<')'))

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        t=0;return''.join(c for c in s if(t:=t+81-2*ord(c))>(c<')'))

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        d=0;return''.join(c for c in s if(d:=d+2*(t:=c<')')-1)>t)

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        d=0;return''.join(c for c in s if d*(d:=d-1+(c<')')*2))

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        d=0;return''.join(c for c in s if d*(d:=d+(c<')')-.5))

test('''
1021. Remove Outermost Parentheses
Solved
Easy
Topics
premium lock icon
Companies
Hint
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
760,356/868.8K
Acceptance Rate
87.5%
Topics
Staff
String
Stack
Bracket Sequences
Weekly Contest 131
icon
Companies
Hint 1
Can you find the primitive decomposition? The number of ( and ) characters must be equal.
''')
