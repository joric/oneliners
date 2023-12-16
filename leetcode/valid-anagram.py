from lc import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return reduce(eq,map(Counter,(s,t)))

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=Counter;return c(s)==c(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=sorted;return c(s)==c(t)

test('''
242. Valid Anagram
Easy

11155

354

Add to List

Share
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Accepted
2,888,387
Submissions
4,541,671
''')
