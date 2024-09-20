from lc import *

# https://leetcode.com/problems/shortest-palindrome/discuss/60099/AC-in-288-ms-simple-brute-force

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r=s[::-1]
        for i in range(len(s)+1):
            if s.startswith(r[i:]):
                return r[:i]+s

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r=s[::-1];return next(r[:i]+s for i in range(len(s)+1)if s.startswith(r[i:]))

# another solution

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        return s[max(i for i in range(len(s)+1)if s[:i]==s[i-1::-1]):][::-1]+s

test('''
214. Shortest Palindrome
Hard

3854

253

Add to List

Share
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Other examples:

Input: s = ""
Output: ""

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
Accepted
213,212
Submissions
598,014
''')
