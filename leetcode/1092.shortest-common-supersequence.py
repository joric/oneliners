from lc import *

# https://leetcode.com/problems/shortest-common-supersequence/discuss/677141/Solutions-under-10-lines.-No-tricks-and-interview-friendly.

class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
       @lru_cache(maxsize=10000)
       def solve(i,j):
            if i == len(s1): return s2[j:]
            if j == len(s2): return s1[i:]
            if s1[i] == s2[j]: return s1[i]+solve(i+1,j+1)
            return min(s1[i]+solve(i+1,j),s2[j]+solve(i,j+1),key=len)
       return solve(0,0)

class Solution:
    def shortestCommonSupersequence(self, a: str, b: str) -> str:
        return(f:=lru_cache(9**5)(lambda i,j:a[i:]and b[j:]and(a[i]==b[j]and a[i]+f(i+1,j+1)or min(a[i]+f(i+1,j),b[j]+f(i,j+1),key=len))or a[i:]or b[j:]))(0,0)

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
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
Accepted
134,847
Submissions
226,404
''')
