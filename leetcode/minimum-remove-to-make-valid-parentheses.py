from lc import *

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/501550/Python-5-lines

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        p = []
        for i, c in enumerate(s):
            if c==')' and len(p) and s[p[-1]]=='(':
                p.pop()
            elif c in '()':
                p.append(i)
        return ''.join(c for i,c in enumerate(s) if i not in p)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        p,e=[],enumerate;[p.pop()if c==')'and p and s[p[-1]]=='('else c in'()'and p.append(i)for i,c in e(s)];return''.join(c for i,c in e(s)if i not in p)

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/419466/Constant-Space-Solution

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        i,j,k=0,s.count(')'),''
        for c in s:
            if c=='(':
                if i==j:
                    continue
                i+=1
            elif c==')':
                j-=1
                if i==0:
                    continue
                i-=1
            k+=c
        return k

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        i,j,k=0,s.count(')'),'';all([i-j and(i:=i+1,k:=k+c)if c=='('else(j:=j-1,i and(i:=i-1,k:=k+c))if c==')'else(k:=k+c)]for c in s);return k

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        i,j=0,s.count(')');return''.join((t:=1,c=='('and(t:=i<j)and(i:=i+1),c==')'and(j:=j-1,(t:=i>0)and(i:=i-1)),c*t)[3]for c in s)

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/4982331/one-line-solution

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        q=0;return''.join(''.join((q:=q+(c=='(')-(c==')'),c)[1]for c in s if')'!=c or q).rsplit('(',q))

test('''
1249. Minimum Remove to Make Valid Parentheses
Medium

6154

122

Add to List

Share
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
Accepted
593,761
Submissions
882,003
''')
