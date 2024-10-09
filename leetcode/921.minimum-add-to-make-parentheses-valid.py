from lc import *

# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/181132/C%2B%2BJavaPython-Straight-Forward-One-Pass

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left = right = 0
        for i in s:
            if right == 0 and i == ')':
                left += 1
            else:
                right += 1 if i == '(' else -1
        return left + right

# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/2093360/1-line-Python-not-optimize-but-fun

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        return len(reduce(lambda a,b:b if not a else a[:-1] if b==')'and a[-1]=='('else a+b,s))if s else 0
# js

# return s.split('').reduce((t,c)=>(c=='('||t.length==0||t[t.length-1]==')'?t.push(c):t.pop(),t),[]).length;


# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/3453688/One-line-(stupid)-solution.-For-fun!

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        return 1+s.find('()')and self.minAddToMakeValid(s.replace('()',''))or len(s)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        return(f:=lambda s:1+s.find('()')and f(s.replace('()',''))or len(s))(s)

# updated 2024-10-09 (POTD)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        [s:=s.replace('()','')for _ in s];return len(s)

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
