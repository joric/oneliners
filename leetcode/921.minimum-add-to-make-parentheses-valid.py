from lc import *

# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/2093360/1-line-Python-not-optimize-but-fun

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        return len(reduce(lambda a,b:b if not a else a[:-1] if b==')'and a[-1]=='('else a+b,s))if s else 0

# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/3453688/One-line-(stupid)-solution.-For-fun!

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        [s:=s.replace('()','')for _ in[0]*999];return len(s)

test('''
921. Minimum Add to Make Parentheses Valid
Medium

4134

208

Add to List

Share
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
 

Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.
Accepted
386,560
Submissions
516,654
''')
