from lc import *

# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, result = [(-1, ')')], 0
        for i, paren in enumerate(s):
            if paren == ')' and stack[-1][1] == '(':
                stack.pop()
                result = max(result, i - stack[-1][0])
            else:
                stack.append((i, paren))
        return result

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        def fn(a,b):
            r, s = a
            i, p = b
            return (max(r,i-s[-2][0]), s[:-1]) if p==')' and s[-1][1]=='(' else (r, s+[(i,p)])
        return reduce(fn, enumerate(s), (0,[(-1, ')')]))[0]

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return reduce(lambda a,i:(a[0],a[1]+[i]) if s[i]=='(' else ((a[0],[i]) if len(a[1])==1 else (max(a[0],i-a[1][-2]),a[1][:-1])),range(len(s)),(0,[-1]))[0]

# POTD 2026-10-02

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return reduce(lambda a,b:(max(a[0],b[0]-a[1][-2][0]), a[1][:-1]) if b[1]==')' and a[1][-1][1]=='(' else (a[0], a[1]+[(b)]), enumerate(s), (0,[(-1, ')')]))[0]

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return reduce(lambda a,i:(a[0],a[1]+[i])if s[i]<')'else(max(a[0],i-a[1][-2]),a[1][:-1])if a[1][1:]else(a[0],[i]),range(len(s)),(0,[-1]))[0]

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        t=[-1];r=[0];[t.append(i)if c<')'else(t.pop(),t or t.append(i),r.append(i-t[-1]))for i,c in enumerate(s)];return max(r)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        a=list.append;t=[-1];r=[0];[a(t,i)if c<')'else(t.pop(),t or a(t,i),a(r,i-t[-1]))for i,c in enumerate(s)];return max(r)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        while s!=(s:=re.sub(r"\((g*)\)",r"g\1g",s)):0
        return max(map(len,re.findall("g+",s)+[""]))

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        return max(map(len,re.findall("g+",reduce(lambda x,_:re.sub(r"\((g*)\)",r"g\1g",x),s,s))+[""]))

class Solution: # TLE
    def longestValidParentheses(self, s: str) -> int:
        [s:=re.sub("\((g*)\)",r"g\1g",s)for _ in s];return max(map(len,re.findall("g*",s)))

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        all(s<(s:=re.sub('\((g*)\)','g\\1g',s))for _ in s);return max(map(len,re.findall('g*',s)))

test('''
32. Longest Valid Parentheses
Hard

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
