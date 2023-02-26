from lc import *

# classic 2d dp
class Solution:
    def minDistance(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range (1, m+1):
            for j in range (1, n+1):
                dp[i][j] = dp[i-1][j-1] if a[i-1]==b[j-1] else 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))
        return dp[m][n]

# recursive dp
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(a, b):
            if not len(a) or not len(b):
                return len(a) or len(b)
            if a[0] == b[0]:
                return dp(a[1:], b[1:])
            insert = 1 + dp(a, b[1:])
            delete = 1 + dp(a[1:], b)
            replace = 1 + dp(a[1:], b[1:])
            return min(insert, delete, replace)
        return dp(word1, word2)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return (f:=cache(lambda a,b:(len(a) or len(b)) if (not len(a) or not len(b)) else f(a[1:], b[1:]) if a[0]==b[0] else 1 + min(f(a, b[1:]), f(a[1:], b), f(a[1:], b[1:]))))(word1, word2)

# does not work on leetcode, no nltk
# class Solution: minDistance = __import__('nltk').distance

class Solution:
    def minDistance(self, a: str, b: str) -> int:
        return (f:=cache(lambda i,j,n=len(a),m=len(b):abs(m-j-n+i) if i==n or j==m else f(i+1,j+1) if a[i]==b[j] else 1+min(f(i+1,j+1),f(i+1,j),f(i,j+1))))(0,0)

class Solution:
    def minDistance(self, a: str, b: str) -> int:
        return (f:=cache(lambda a,b:(f(a[1:],b[1:]) if a[0]==b[0] else 1+min(f(a,b[1:]),f(a[1:],b),f(a[1:],b[1:]))) if a and b else len(a) or len(b)))(a,b)

# https://leetcode.com/problems/edit-distance/discuss/3232797/Python-3-one-line-O(min(mn)-memory

class Solution:
    def minDistance(self, a: str, b: str) -> int:
        m,n = len(a),len(b)
        if m<n:
            a,b,m,n = b,a,n,m
        dp = [*range(n+1)]
        for i in range(1,m+1):
            p,dp[0] = dp[0],i
            for j in range(1,n+1):
                p,dp[j] = dp[j],min(min(dp[j-1],dp[j])+1,p+(a[i-1]!=b[j-1]))
        return dp[n]

class Solution:
    def minDistance(self, a: str, b: str) -> int:
        return self.minDistance(b,a) if (m:=len(a))<(n:=len(b)) else (dp:=[*range(n+1)],all((p:=dp[0],setitem(dp,0,i),all((t:=dp[j],setitem(dp,j,min(min(dp[j-1],dp[j])+1,p+(a[i-1]!=b[j-1]))),p:=t) for j in range(1,n+1))) for i in range(1,m+1)),dp[n])[-1]

test('''
72. Edit Distance

Hard

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
''')
