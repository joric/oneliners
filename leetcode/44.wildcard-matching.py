from lc import *

# https://leetcode.com/problems/wildcard-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]

# https://leetcode.com/problems/wildcard-matching/discuss/1299187/python-in-3-readable-lines

class Solution:
    @cache
    def isMatch(self, s: str, p: str) -> bool:
        if p=='' or s=='': return p==s or set(p)=={'*'}
        if s[0]==p[0] or p[0]=='?': return self.isMatch(s[1:],p[1:])
        return p[0]=='*' and (self.isMatch(s[1:],p[1:]) or self.isMatch(s[1:],p) or self.isMatch(s,p[1:]))

# https://leetcode.com/problems/wildcard-matching/discuss/4355649/Simple-one-line-solution-using-python

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return __import__('fnmatch').fnmatch(s,p)

test('''
44. Wildcard Matching
Hard

8333

357

Add to List

Share
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
 

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
Accepted
616,655
Submissions
2,159,193
''')
