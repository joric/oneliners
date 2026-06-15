from lc import *

# https://leetcode.com/problems/process-string-with-special-operations-i/description/?envType=daily-question&envId=2026-06-16

class Solution:
    def processStr(self, s: str) -> str:
        return reduce(lambda r,c:r[:-1]if c=='*'else r+r if c=='#'else r[::-1]if c=='%'else r+c,s,'')

class Solution:
    def processStr(self, s: str) -> str:
        r='';[r:= r[:-1]if c=='*'else r+r if c=='#'else r[::-1]if c=='%'else r+c for c in s];return r

class Solution:
    def processStr(self, s: str) -> str:
        return reduce(lambda r,c:(r[:-1],r*2,r[::-1],r+c)['*#%'.find(c)],s,'')

class Solution:
    def processStr(self, s: str) -> str:
        r='';[r:=(r[:-1],r*2,r[::-1],r+c)['*#%'.find(c)]for c in s];return r

test('''
3612. Process String with Special Operations I
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.

Build a new string result by processing s according to the following rules from left to right:

If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.
Return the final string result after processing all characters in s.

 

Example 1:

Input: s = "a#b%*"

Output: "ba"

Explanation:

i   s[i]    Operation   Current result
0   'a' Append 'a'  "a"
1   '#' Duplicate result    "aa"
2   'b' Append 'b'  "aab"
3   '%' Reverse result  "baa"
4   '*' Remove the last character   "ba"
Thus, the final result is "ba".

Example 2:

Input: s = "z*#"

Output: ""

Explanation:

i   s[i]    Operation   Current result
0   'z' Append 'z'  "z"
1   '*' Remove the last character   ""
2   '#' Duplicate the string    ""
Thus, the final result is "".

 

Constraints:

1 <= s.length <= 20
s consists of only lowercase English letters and special characters *, #, and %.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
49,075/75.4K
Acceptance Rate
65.1%
Topics
Senior
String
Simulation
Weekly Contest 458
icon
Companies
Hint 1
Simulate as described
''')
