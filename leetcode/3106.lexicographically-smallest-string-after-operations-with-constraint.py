from lc import *

# Q2. https://leetcode.com/contest/weekly-contest-392
# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        out = ''
        for c in s:
            v = ord(c) - ord('a')
            dist = min(v, 26 - v)
            if dist <= k:
                k -= dist
                out += 'a'
                continue
            while k:
                v -= 1
                k -= 1
            out += chr(ord('a') + v)
        return out

# https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/discuss/4986998/6-Liner-Solution-oror-Very-Easy-oror-Python3

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        r = ''
        for c in map(ord,s):
            m = min(c-ord('a'),ord('z')-c+1)
            r += k<m and chr(c-k) or 'a'
            k -= min(k,m)
        return r

class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        r='';[(r:=r+(k<(m:=min(c-97,123-c))and chr(c-k)or'a'),k:=k-min(k,m))for c in map(ord,s)];return r

test('''
3106. Lexicographically Smallest String After Operations With Constraint
Medium

3

1

Add to List

Share
You are given a string s and an integer k.

Define a function distance(s1, s2) between two strings s1 and s2 of the same length n as:

The sum of the minimum distance between s1[i] and s2[i] when the characters from 'a' to 'z' are placed in a cyclic order, for all i in the range [0, n - 1].
For example, distance("ab", "cd") == 4, and distance("a", "z") == 1.

You can change any letter of s to any other lowercase English letter, any number of times.

Return a string denoting the lexicographically smallest string t you can get after some changes, such that distance(s, t) <= k.

 

Example 1:

Input: s = "zbbz", k = 3

Output: "aaaz"

Explanation:

Change s to "aaaz". The distance between "zbbz" and "aaaz" is equal to k = 3.

Example 2:

Input: s = "xaxcd", k = 4

Output: "aawcd"

Explanation:

The distance between "xaxcd" and "aawcd" is equal to k = 4.

Example 3:

Input: s = "lol", k = 0

Output: "lol"

Explanation:

It's impossible to change any character as k = 0.

 

Constraints:

1 <= s.length <= 100
0 <= k <= 2000
s consists only of lowercase English letters.
Accepted
11,591
Submissions
20,629
''')