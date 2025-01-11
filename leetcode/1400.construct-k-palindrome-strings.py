from lc import *

# https://leetcode.com/problems/construct-k-palindrome-strings/solutions/563379/java-c-python-straight-forward/?envType=daily-question&envId=2025-01-11

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(i&1 for i in Counter(s).values())<=k<=len(s)

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c=Counter(s);return sum(1&c[k]for k in c)<=k<=len(s)

test('''
1400. Construct K Palindrome Strings
Solved
Medium
Topics
Companies
Hint
Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

 

Example 1:

Input: s = "annabelle", k = 2
Output: true
Explanation: You can construct two palindromes using all characters in s.
Some possible constructions "anna" + "elble", "anbna" + "elle", "anellena" + "b"
Example 2:

Input: s = "leetcode", k = 3
Output: false
Explanation: It is impossible to construct 3 palindromes using all the characters of s.
Example 3:

Input: s = "true", k = 4
Output: true
Explanation: The only possible solution is to put each character in a separate string.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= 105
''')
