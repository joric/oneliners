from lc import *

# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, a: str, b: str) -> bool:
        return a in b+b and len(b)==len(a)

class Solution:
    def rotateString(self, a: str, b: str) -> bool:
        return len(a)==len(b)and a in b+b

test('''
796. Rotate String
Easy

3741

212

Add to List

Share
Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

For example, if s = "abcde", then it will be "bcdea" after one shift.
 

Example 1:

Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:

Input: s = "abcde", goal = "abced"
Output: false
 

Constraints:

1 <= s.length, goal.length <= 100
s and goal consist of lowercase English letters.
Accepted
389,780
Submissions
652,200
''')
