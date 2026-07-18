from lc import *

# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/?envType=daily-question&envId=2026-07-19

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d = {c: i for i, c in enumerate(s)}
        q = []
        for i, c in enumerate(s):
            if c in q:
                continue
            while q and q[-1]>c and i<d[q[-1]]:
                q.pop()
            q.append(c)
        return "".join(q)

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        q=[''];[c in q or([q.pop()for x in q[:]if c<q[-1]and i<s.rfind(q[-1])],q.append(c))for i,c in enumerate(s)];return''.join(q)

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        return s and(c:=min(x for x in s if{*s[s.find(x):]}=={*s}))+self.smallestSubsequence(s[s.find(c):].replace(c,''))

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        q=[''];[c in q or([q.pop()for x in q[:]if c<q[-1]in s[i:]],q.append(c))for i,c in enumerate(s)];return''.join(q)

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        return(f:=lambda s:s and(c:=min(x for x in s if{*s[s.find(x):]}=={*s}))+f(s[s.find(c):].replace(c,'')))(s)

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        return(f:=lambda s:s and(c:=min(s[:min(map(s.rfind,s))+1]))+f(s[s.find(c):].replace(c,'')))(s)

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        return(f:=lambda s:s and(c:=min(s[:min(map(s.rfind,s))+1]))+f(re.sub(c,'',s[s.find(c):])))(s)

test('''
1081. Smallest Subsequence of Distinct Characters
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
 

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
100,941/158.4K
Acceptance Rate
63.7%
Topics
Senior Staff
String
Stack
Greedy
Monotonic Stack
Weekly Contest 140
icon
Companies
Hint 1
Greedily try to add one missing character. How to check if adding some character will not cause problems ? Use bit-masks to check whether you will be able to complete the sub-sequence if you add the character at some index i.
Similar Questions
Find the Most Competitive Subsequence
Medium
''')
