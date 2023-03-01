from lc import *

class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        for c in s:
            if c == '{':
                q.append('}')
            elif c == '(':
                q.append(')')
            elif c == '[':
                q.append(']')
            else:
                if not q or q[-1]!=c:
                    return False
                q.pop()
        return not q

class Solution:
    def isValid(self, s: str) -> bool:
        s,i,m = list(s), 0, {'(':')','[':']', '{':'}'}
        for c in s:
            if c in m:
                s[i] = m[c]
                i += 1
            elif i==0:
                return False
            else:
                i -= 1
                if c != s[i]:
                    return False
        return i == 0

class Solution:
    def isValid(self, s: str) -> bool:
        stack, brackets = [], {'(':')', '{':'}', '[':']'}
        for c in s:
            if c in brackets:
                stack.append(brackets[c])
            elif not stack or c != stack.pop():
                return False
        return not stack

class Solution:
    def isValid(self, s: str) -> bool:
        return (x := []) or not (b := {'(':')','{':'}','[':']'}) or (not (sum([1 for c in s if (c not in b or x.append(b[c])) and not (x and c==x.pop())]) or x))

# https://www.python.org/dev/peps/pep-0572
class Solution:
    def isValid(self, s: str) -> bool:
        while True:
            q, s = s, s.replace('()','').replace('{}','').replace('[]','')
            if q == s: return s == ''

class Solution:
    def isValid(self, s: str) -> bool:
        return s=='' if s==(s:=s.replace('()','').replace('{}','').replace('[]','')) else self.isValid(s)

test('''
20. Valid Parentheses

Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 10**4
s consists of parentheses only '()[]{}'.

''')
