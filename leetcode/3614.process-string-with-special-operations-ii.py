from lc import *

# https://leetcode.com/problems/process-string-with-special-operations-ii/solutions/6951646/javacpython-reverse-by-lee215-8fz9/

class Solution:
    def processStr(self, s: str, k: int) -> str:
        l = 0

        for c in s:
            if c == '*':
                l = max(0, l - 1)
            elif c == '#':
                l *= 2
            elif c == '%':
                continue
            else:
                l += 1

        if k >= l:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            c = s[i]
            if c == '*':
                l += 1
            elif c == '#':
                l //= 2
                if k >= l:
                    k -= l
            elif c == '%':
                k = l - 1 - k
            else:
                l -= 1
                if l == k:
                    return c


class Solution:
    def processStr(self, s: str, k: int) -> str:
        l=0
        for c in s:l=(max(0,l-1),l*2,l,l+1)['*#%'.find(c)]
        if k>=l:return'.'
        for c in s[::-1]:
            if c=='*':l+=1
            elif c=='#':l//=2;k-=l*(k>=l)
            elif c=='%':k=l-1-k
            elif(l:=l-1)==k:return c

class Solution:
    def processStr(self, s: str, k: int) -> str:
        l=0;[l:=(max(0,l-1),l*2,l,l+1)['*#%'.find(c)]for c in s];return'.'if k>=l else next(c for c in s[::-1]if[t:=((l+1,k),(l//2,k%(l//2or 1)),(l,~k+l),(l-1,k))['*#%'.find(c)],l:=t[0],k:=t[1]]and c>'*'and l==k)

class Solution:
    def processStr(self, s: str, k: int) -> str:
        l=0;[l:=(max(0,l-1),l*2,l,l+1)['*#%'.find(c)]for c in s];return k>=l and'.'or next(c for c in s[::-1]if[t:=((l+1,k),(l//2,k%(l//2or 1)),(l,~k+l),(l-1,k))['*#%'.find(c)],l:=t[0],k:=t[1]]!='*'<c!=l==k)

test('''
3614. Process String with Special Operations II
Hard
Topics
premium lock icon
Companies
Hint
You are given a string s consisting of lowercase English letters and the special characters: '*', '#', and '%'.

You are also given an integer k.

Build a new string result by processing s according to the following rules from left to right:

If the letter is a lowercase English letter append it to result.
A '*' removes the last character from result, if it exists.
A '#' duplicates the current result and appends it to itself.
A '%' reverses the current result.
Return the kth character of the final string result. If k is out of the bounds of result, return '.'.

 

Example 1:

Input: s = "a#b%*", k = 1

Output: "a"

Explanation:

i   s[i]    Operation   Current result
0   'a' Append 'a'  "a"
1   '#' Duplicate result    "aa"
2   'b' Append 'b'  "aab"
3   '%' Reverse result  "baa"
4   '*' Remove the last character   "ba"
The final result is "ba". The character at index k = 1 is 'a'.

Example 2:

Input: s = "cd%#*#", k = 3

Output: "d"

Explanation:

i   s[i]    Operation   Current result
0   'c' Append 'c'  "c"
1   'd' Append 'd'  "cd"
2   '%' Reverse result  "dc"
3   '#' Duplicate result    "dcdc"
4   '*' Remove the last character   "dcd"
5   '#' Duplicate result    "dcddcd"
The final result is "dcddcd". The character at index k = 3 is 'd'.

Example 3:

Input: s = "z*#", k = 0

Output: "."

Explanation:

i   s[i]    Operation   Current result
0   'z' Append 'z'  "z"
1   '*' Remove the last character   ""
2   '#' Duplicate the string    ""
The final result is "". Since index k = 0 is out of bounds, the output is '.'.

 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters and special characters '*', '#', and '%'.
0 <= k <= 1015
The length of result after processing s will not exceed 1015.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
11,303/65.6K
Acceptance Rate
17.2%
Topics
Senior Staff
String
Simulation
Weekly Contest 458
icon
Companies
Hint 1
Track the length of the string after each operation on s.
Hint 2
Walk backwards through s, undoing each # by using modulus on the tracked lengths, and undoing each % by mirroring across the midpoint, to pinpoint the kth character.
''')
