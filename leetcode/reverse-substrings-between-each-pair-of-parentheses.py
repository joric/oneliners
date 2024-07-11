from lc import *

# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/discuss/382563/Two-Solutions-in-Python-3-(beats-100.0-)-(three-lines)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        d=[i for i,j in enumerate(s)if j=='('];return next((s for _ in s if not(d and(s:=(lambda x,y:s[0:x]+s[x+1:y][::-1]+s[y+1:])(d[-1],s.index(')',d.pop()+1))))),s)

# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/discuss/383219/Java-Solution-1-line-for-fun

class Solution:
    def reverseParentheses(self, s: str) -> str:
        return s if s.rfind('(')<0 else self.reverseParentheses(s[0:s.rfind('(')]+s[s.rfind('(')+1:s.find(')',s.rfind('('))][::-1]+s[s.find(')',s.rfind('('))+1:] )

class Solution:
    def reverseParentheses(self, s: str) -> str:
        i = s.rfind('(')
        j = s.find(')', i)
        return s if i<0 else self.reverseParentheses(s[:i]+s[i+1:j][::-1]+s[j+1:])

class Solution:
    def reverseParentheses(self, s: str) -> str:
        return(f:=lambda s:0>(i:=s.rfind('('))and s or f(s[:i]+s[i+1:(j:=s.find(')',i))][::-1]+s[j+1:]))(s)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        return(f:=lambda s:~(i:=s.rfind('('))and f(s[:i]+s[i+1:(j:=s.find(')',i))][::-1]+s[j+1:])or s)(s)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        return(f:=lambda s:~(i:=s.rfind('('))and f(s[:i]+s[(j:=s.find(')',i))-1:i:-1]+s[j+1:])or s)(s)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        return(f:=lambda s:~(j:=s.find(')',i:=s.rfind('(')))and f(s[:i]+s[j-1:i:-1]+s[j+1:])or s)(s)

# regexp solution

class Solution:
    def reverseParentheses(self, s: str) -> str:
        return reduce(lambda s,_:re.sub(r'\(([^()]*)\)',lambda m:m[1][::-1],s),s,s)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        [s:=re.sub(r'\(([^()]*)\)',lambda m:m[1][::-1],s)for _ in s];return s

# non-raw strings give invalid escape sequence '\(', but still work

class Solution:
    def reverseParentheses(self, s: str) -> str:
        [s:=re.sub('\(([^()]*)\)',lambda m:m[1][::-1],s)for _ in s];return s

test('''
1190. Reverse Substrings Between Each Pair of Parentheses
Medium

1885

56

Add to List

Share
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 

Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
Accepted
76,037
Submissions
113,951
''')
