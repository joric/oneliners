from lc import *

# https://leetcode.com/problems/distinct-subsequences-ii/solutions/192017/javacpython-dp-4-lines-on-time-o1-space-r51bq/?envType=daily-question&envId=2026

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        p = [0] * 26
        for c in s:
            p[ord(c)-ord('a')]=sum(p)+1
        return sum(p) % (10**9 + 7)


# https://leetcode.com/problems/distinct-subsequences-ii/solutions/296965/4-line-python-on-time-o1-space-by-chaoxu-4k6o/?envType=daily-question&envId=2026-09-07

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        p = {}
        for c in s:
            p[c] = sum(p.values(),1)
        return sum(p.values())%(10**9+7)

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        t=0;p={}
        for c in s:t,p[c]=t*2+1-p.get(c,0),t+1
        return t%(10**9+7)

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        return sum(reduce(lambda p,c:p|{c:sum(p.values(),1)},s,{}).values())%(10**9+7)

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        p={};[p:=p|{c:sum(p.values(),1)}for c in s];return sum(p.values())%(10**9+7)

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        p=[0]*123;exec("for c in s:p[ord(c)]=sum(p)+1");return sum(p)%(10**9+7)

test('''
940. Distinct Subsequences II
Hard
Topics
premium lock icon
Companies
Given a string s, return the number of distinct non-empty subsequences of s. Since the answer may be very large, return it modulo 109 + 7.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not.
 

Example 1:

Input: s = "abc"
Output: 7
Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc", and "abc".
Example 2:

Input: s = "aba"
Output: 6
Explanation: The 6 distinct subsequences are "a", "b", "ab", "aa", "ba", and "aba".
Example 3:

Input: s = "aaa"
Output: 3
Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
54,914/124.1K
Acceptance Rate
44.3%
Topics
Principal
String
Dynamic Programming
Weekly Contest 110
icon
Companies
Similar Questions
Number of Unique Good Subsequences
Hard
Count K-Subsequences of a String With Maximum Beauty
Hard
''')
