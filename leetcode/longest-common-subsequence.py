from lc import *

class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def f(a,b):
            if len(a)==0 or len(b)==0:
                return 0
            if a[0]==b[0]:
                return 1 + f(a[1:], text2[1:])
            else:
                return max(f(a, b[1:]), f(a[1:], b))
        return f(text1, text2)

class Solution:
    @cache
    def longestCommonSubsequence(self, a: str, b: str, i=0, j=0) -> int:
        return 0 if i==len(a) or j==len(b) else 1+self.longestCommonSubsequence(a,b,i+1,j+1) if a[i]==b[j] else max(self.longestCommonSubsequence(a,b,i+1,j), self.longestCommonSubsequence(a,b,i,j+1))

# https://leetcode.com/problems/longest-common-subsequence/solutions/2912811/python-3-one-line/
# memory limit exceeded

class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        return(f:=cache(lambda a,b:a and b and(a[0]==b[0]and 1+f(a[1:],b[1:])or max(f(a,b[1:]),f(a[1:],b)))or 0))(a,b)

# working

class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        return(f:=cache(lambda i,j:a[i:]and b[j:]and(a[i]==b[j]and 1+f(i+1,j+1)or max(f(i+1,j),f(i,j+1)))or 0))(0,0)

test('''

1143. Longest Common Subsequence
Medium
9K
103
Companies
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

''')

