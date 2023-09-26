from lc import *

# https://leetcode.com/problems/remove-duplicate-letters/discuss/76787/Some-Python-solutions

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d,r = {c: i for i, c in enumerate(s)},''
        for i, c in enumerate(s):
            if c not in r:
                while c < r[-1:] and i < d[r[-1]]:
                    r = r[:-1]
                r += c
        return r

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for c in sorted(set(s)):
            x = s[s.index(c):]
            if set(x)==set(s):
                return c+self.removeDuplicateLetters(x.replace(c,''))
        return ''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        def f(s):
            for c in sorted(set(s)):
                x = s[s.index(c):]
                if set(x)==set(s):
                    return c+f(x.replace(c,''))
            return ''
        return f(s)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return(f:=lambda s:next((c+f(x.replace(c,''))for c in sorted(set(s))if set(x:=s[s.index(c):])==set(s)),''))(s)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        return(f:=lambda s:next((c+f(x.replace(c,''))for c in sorted({*s})if set(x:=s[s.index(c):])=={*s}),''))(s)

test('''
316. Remove Duplicate Letters
Medium

7510

489

Add to List

Share
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 10^4
s consists of lowercase English letters.
 

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

Accepted
255,637
Submissions
549,748
''')

