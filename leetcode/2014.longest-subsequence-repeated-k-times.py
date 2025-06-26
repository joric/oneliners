from lc import *

# https://leetcode.com/problems/longest-subsequence-repeated-k-times/solutions/1471930/python-answer-is-not-so-long-explained/

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def isSubsequence(s, t):
            t = iter(t)
            return all(c in t for c in s)
        hot = "".join(el*(freq//k) for el, freq in Counter(s).items())
        combs = set()
        for l in range(len(hot) + 1):
            for cand in combinations(hot, l):
                for perm in permutations(cand):
                    combs.add("".join(perm))
        combs = sorted(combs, key = lambda x: (len(x), x), reverse = True)
        for c in combs:
            if isSubsequence(c*k, s):
                return c

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        h=''.join(i*(x//k)for i,x in Counter(s).items());v={''.join(t)for l in range(len(h)+1)for r in combinations(h,l)for t in permutations(r)};return next(c for c in sorted(v,key=lambda x:(len(x),x),reverse=True)if(t:=iter(s))and all(x in t for x in c*k))

test('''
2014. Longest Subsequence Repeated k Times
Hard
Topics
premium lock icon
Companies
Hint
You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.

For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

 

Example 1:

example 1
Input: s = "letsleetcode", k = 2
Output: "let"
Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
"let" is the lexicographically largest one.
Example 2:

Input: s = "bb", k = 2
Output: "b"
Explanation: The longest subsequence repeated 2 times is "b".
Example 3:

Input: s = "ab", k = 2
Output: ""
Explanation: There is no subsequence repeated 2 times. Empty string is returned.
 

Constraints:

n == s.length
2 <= n, k <= 2000
2 <= n < k * 8
s consists of lowercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
10,282/19K
Acceptance Rate
54.2%
Topics
String
Backtracking
Greedy
Counting
Enumeration
icon
Companies
Hint 1
The length of the longest subsequence does not exceed n/k. Do you know why?
Hint 2
Find the characters that could be included in the potential answer. A character occurring more than or equal to k times can be used in the answer up to (count of the character / k) times.
Hint 3
Try all possible candidates in reverse lexicographic order, and check the string for the subsequence condition.
Similar Questions
Longest Substring with At Least K Repeating Characters
Medium
''')
