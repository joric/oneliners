from lc import *

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range (n//2, 0, -1):
            d = n // i
            if d*i == n:
                if s[:i]*d == s:
                    return True
        return False

# https://leetcode.com/problems/repeated-substring-pattern/discuss/826417/rust-oneliner

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in(s+s)[1:-1]

test('''
459. Repeated Substring Pattern
Easy

4761

425

Add to List

Share
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 10^4
s consists of lowercase English letters.
''')
