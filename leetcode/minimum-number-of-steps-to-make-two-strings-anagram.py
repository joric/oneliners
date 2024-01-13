from lc import *

# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a,b=map(Counter,(s,t));return sum(abs(a[c]-b[c])for c in'abcdefghijklmnopqrstuvwxyz')//2

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a,b=map(Counter,(s,t));return sum(max(a[c]-b[c],0)for c in a)

test('''
1347. Minimum Number of Steps to Make Two Strings Anagram
Medium

2017

84

Add to List

Share
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
 

Constraints:

1 <= s.length <= 5 * 10^4
s.length == t.length
s and t consist of lowercase English letters only.
Accepted
149,359
Submissions
190,301
''')


