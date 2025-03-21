from lc import *

# Q1. https://leetcode.com/contest/biweekly-contest-128/
# https://leetcode.com/problems/score-of-a-string

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(x)-ord(y))for x,y in zip(s,s[1:]))

# updated 2024-06-01

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(map(abs,starmap(sub,pairwise(map(ord,s)))))

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(x)-ord(y))for x,y in pairwise(s))

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(x-y)for x,y in pairwise(map(ord,s)))

class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(map(abs,map(sub,s:=s.encode(),s[1:])))

test('''
3110. Score of a String
Easy

1

0

Add to List

Share
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.

 

Example 1:

Input: s = "hello"

Output: 13

Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:

Input: s = "zaz"

Output: 50

Explanation:

The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
Accepted
21,172
Submissions
22,450
''')