from lc import *

# https://leetcode.com/problems/valid-palindrome-ii/discuss/107720/C%2B%2BJavaPython-Easy-and-Concise

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        while i < len(s) / 2 and s[i] == s[-(i + 1)]: i += 1
        # slice the string into a smaller palindrome from i to len(s) - i
        s = s[i:len(s) - i]
        # check if both variations of 1) remove first character 2) remove last character    will yeild to a palindrome
        return s[1:] == s[1:][::-1] or s[:-1] == s[:-1][::-1]

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s);i=next((i for i in range(n)if s[i]!=s[~i]),n);s=s[i:n-i];return s[1:]==s[1:][::-1]or s[:-1]==s[:-1][::-1]

class Solution:
    def validPalindrome(self, s: str) -> bool:
        n=len(s);i=next((i for i in range(n)if s[i]!=s[~i]),n);s=s[i:n-i];return any(t==t[::-1]for t in(s[1:],s[:-1]))

test('''
680. Valid Palindrome II
Easy

8165

436

Add to List

Share
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
Accepted
752,359
Submissions
1,842,331
''')
