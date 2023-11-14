from lc import *

# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/discuss/1330178/Python-Straight-Forward-Solution

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i + 1: j]))
        return res

# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/discuss/1330207/Python-3-one-line

class Solution:
  def countPalindromicSubsequence(self, s: str) -> int:
    return sum(len(set(s[s.find(c)+1:s.rfind(c)]))for c in ascii_lowercase if s.find(c)<s.rfind(c))

# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/discuss/3662795/Python-1-Liner

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum(len(set(s[s.find(c)+1:s.rfind(c)]))for c in set(s))

# 5 chars shorter

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum(len({*s[s.find(c)+1:s.rfind(c)]})for c in{*s})

test('''
1930. Unique Length-3 Palindromic Subsequences
Medium

974

32

Add to List

Share
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 10^5
s consists of only lowercase English letters.
Accepted
42,928
Submissions
72,853
''')

