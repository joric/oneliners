from Leetcode import *

class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        stack, result = [(-1, ')')], 0
        for i, paren in enumerate(s):
            if paren == ')' and stack[-1][1] == '(':
                stack.pop()
                result = max(result, i - stack[-1][0])
            else:
                stack.append((i, paren))
        return result

class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        def fn(a,b):
            r, s = a
            i, p = b
            return (max(r,i-s[-2][0]), s[:-1]) if p==')' and s[-1][1]=='(' else (r, s+[(i,p)])
        return reduce(fn, enumerate(s), (0,[(-1, ')')]))[0]

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return reduce(lambda a,i:(a[0],a[1]+[i]) if s[i]=='(' else ((a[0],[i]) if len(a[1])==1 else (max(a[0],i-a[1][-2]),a[1][:-1])),range(len(s)),(0,[-1]))[0]

test(Solution,'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

''')
