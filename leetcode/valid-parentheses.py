from Leetcode import *

class Solution1:
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
        return (s.count('()') +s.count('[]') +s.count('{}'))*2==len(s)


test(Solution,'''
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
