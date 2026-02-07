from lc import *

# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/solutions/5555966/one-line-solution-using-functools-by-jhz-a6tw/?envType=daily-question&envId=2026-02-07

class Solution:
    def minimumDeletions(self, s: str) -> int:
        return s.count('b')-reduce(lambda a,b:max(0,a+(-1)**('a'==b)),s,0)

class Solution:
    def minimumDeletions(self, s: str) -> int:
        return s.count('b')-reduce(lambda a,b:max(0,a+1-2*(b<'b')),s,0)

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=b=0;[c>'a'and(b:=b+1)or(a:=min(a+1,b))for c in s];return a

# POTD 2026-02-07

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=b=0;[a:=min(a+(c<='a'),b:=b+(c>'a'))for c in s];return a

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=b=0;[a:=a+(a<(b:=b+(k:=c>'a')))-k for c in s];return a

class Solution:
    def minimumDeletions(self, s: str) -> int:
        a=b=0;[a:=a-(k:=c>'a')+(a<(b:=b+k))for c in s];return a

test('''
1653. Minimum Deletions to Make String Balanced
Medium

1323

38

Add to List

Share
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

 

Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.
 

Constraints:

1 <= s.length <= 105
s[i] is 'a' or 'b'​​.
Accepted
43,654
Submissions
74,190
''')