from lc import *

# https://leetcode.com/problems/longest-palindrome/discuss/89587/What-are-the-odds-(Python-and-C%2B%2B)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        o=sum(v&1 for v in Counter(s).values());return len(s)-o+bool(o)

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s);o=sum(1&c[v]for v in c);return len(s)-o+(o>0)

# updated 2024-06-04

class Solution:
    def longestPalindrome(self, s: str) -> int:
        c=Counter(s);return min(len(s),sum(-2&c[v]for v in c)+1)

test('''
409. Longest Palindrome
Easy

4805

306

Add to List

Share
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
''')
