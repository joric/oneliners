from lc import *

# https://leetcode.com/problems/isomorphic-strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s,t)))==len(set(s))==len(set(t))

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len({*map(len,({*zip(s,t)},{*s},{*t}))})<2

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len({*zip(s,t)})==len({*s})==len({*t})

# https://leetcode.com/problems/isomorphic-strings/discuss/295802/1-line-python

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return eq(*[[*map(x.index,x)]for x in(s,t)])

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return[*map(s.index,s)]==[*map(t.index,t)]

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return[*map(s.find,s)]==[*map(t.find,t)]

test('''
205. Isomorphic Strings
Easy

6319

1342

Add to List

Share
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 10^4
t.length == s.length
s and t consist of any valid ascii character.

Accepted
835,963
Submissions
1,951,241
''')