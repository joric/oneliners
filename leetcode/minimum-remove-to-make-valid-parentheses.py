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
