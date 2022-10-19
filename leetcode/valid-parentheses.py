from Leetcode import *

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

test(Solution,'''
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
''')
