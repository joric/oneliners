from lc import *

# https://leetcode.com/problems/distinct-subsequences/discuss/319994/short-and-sweet-python-76ms

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        p = [0]*(len(t)+1)
        p[0] = 1
        for i in range(0, len(s)):
            for j in range(len(t),0,-1):
                if s[i]==t[j-1]:
                    p[j] += p[j-1]
        return p[-1]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        p=[0]*len(t)
        for c in s:
            d = 1
            p = [((c==j)*d)+(d:=i) for i,j in zip(p,t)]
        return p[-1]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        p=[0]*len(t);all((d:=1,p:=[((c==j)*d)+(d:=i)for i,j in zip(p,t)])for c in s);return p[-1]

# https://leetcode.com/problems/distinct-subsequences/discuss/1472589/Python-short-dp-solution-explained

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def f(i,j):
            if i == -1: return j == -1
            if j == -1: return j == -1
            return f(i-1,j)+(s[i]==t[j])*f(i-1,j-1)
        return f(len(s)-1,len(t)-1)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return(f:=cache(lambda i,j:j<0 if(i<0 or j<0)else f(i-1,j)+(s[i]==t[j])*f(i-1,j-1)))(len(s)-1,len(t)-1)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return(f:=cache(lambda i,j:f(i-1,j)+(s[i]==t[j])*f(i-1,j-1)if i>=0<=j else j<0))(len(s)-1,len(t)-1)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return+(f:=cache(lambda i,j:s[i:]and t[j:]and f(i+1,j)+(s[i]==t[j])*f(i+1,j+1)or not t[j:]))(0,0)

# Memory Limit Exceeded
class Solution:
    @cache
    def numDistinct(self, s: str, t: str) -> int:
        return s and t and self.numDistinct(s[1:],t)+(s[0]==t[0])*self.numDistinct(s[1:],t[1:])or+(''==t)

# Memory Limit Exceeded
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return+(f:=cache(lambda s,t:s and t and f(s[1:],t)+(s[0]==t[0])*f(s[1:],t[1:])or''==t))(s,t)

test('''
115. Distinct Subsequences
Hard

6423

282

Add to List

Share
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 
Example 3:

Input: s = "b", t = "a"
Output: 0

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
Accepted
366,915
Submissions
794,122
''')
