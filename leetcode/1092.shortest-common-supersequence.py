from lc import *

# https://leetcode.com/problems/shortest-common-supersequence/discuss/677141/Solutions-under-10-lines.-No-tricks-and-interview-friendly.

class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        @lru_cache(10000)
        def f(i,j):
            if i == len(a): return b[j:]
            if j == len(b): return a[i:]
            if a[i] == b[j]: return a[i]+f(i+1,j+1)
            return min(a[i]+f(i+1,j),b[j]+f(i,j+1),key=len)
        return f(0,0)

class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        return(f:=lru_cache(9**5)(lambda i,j:a[i:]and b[j:]and(a[i]==b[j]and a[i]+f(i+1,j+1)or min(a[i]+f(i+1,j),b[j]+f(i,j+1),key=len))or a[i:]or b[j:]))(0,0)

class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        @lru_cache(10000)
        def f(a,b):
            if not a: return b
            if not b: return a
            if a[0]==b[0]: return a[0]+f(a[1:],b[1:])
            return min(a[0]+f(a[1:],b), b[0]+f(a,b[1:]),key=len)
        return f(a,b)

class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        return(f:=lru_cache(9**5)(lambda a,b:a and b and(a[0]==b[0]and a[0]+f(a[1:],b[1:])or min(a[0]+f(a[1:],b),b[0]+f(a,b[1:]),key=len))or a or b))(a,b)

class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        return(f:=lru_cache(9**5)(lambda a,b:a and b and((c:=a[0])==b[0]and c+f(a[1:],b[1:])or min(c+f(a[1:],b),b[0]+f(a,b[1:]),key=len))or a or b))(a,b)

test('''
1092. Shortest Common Supersequence
Hard

4943

72

Add to List

Share
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.
Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 

Other examples:

Input: str1 = "bbbaaaba", str2 = "bbababbb"
Output: "bbbaaababbb"

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
Accepted
134,847
Submissions
226,404
''')
