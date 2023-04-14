from lc import *

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def f(i,j):
            if i>=len(s) or j<0:
                return 0
            return s[i]==s[j] and 1+f(i+1,j-1) or max(f(i+1,j),f(i,j-1))
        return f(0,len(s)-1)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return (f:=cache(lambda i,j:s[i]==s[j] and 1+f(i+1,j-1) or max(f(i+1,j),f(i,j-1)) if not(i>=len(s) or j<0) else 0))(0,len(s)-1)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return (f:=cache(lambda i,j:s[i]==s[j] and 1+f(i+1,j-1) or max(f(i+1,j),f(i,j-1)) if max(i,~j)<len(s) else 0))(0,-1)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def f(s):
            if len(s)<2:
                return len(s)
            return s[0]==s[-1] and 2+f(s[1:-1]) or max(f(s[1:]),f(s[:-1]))
        return f(s)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return (f:=cache(lambda s:len(s) if len(s)<=1 else f(s[1:-1])+2 if s[0]==s[-1] else max(f(s[1:]),f(s[:-1]))))(s)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return (f:=cache(lambda s:s[0]==s[-1] and 2+f(s[1:-1]) or max(f(s[1:]),f(s[:-1])) if s[1:] else len(s)))(s)

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return (f:=cache(lambda s:s[1:] and max(2+f(s[s.find(c,1):s.rfind(c)]) for c in s) or len(s)-1))('#'+s)

test('''

516. Longest Palindromic Subsequence
Medium

7518

280

Add to List

Share
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Example 3:

Input: s = "a"
Output: 1

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
Accepted
346,624
Submissions
564,698
Seen this question in a real interview before?

Yes

No
Longest Palindromic Substring
Medium
Palindromic Substrings
Medium
Count Different Palindromic Subsequences
Hard
Longest Common Subsequence
Medium
Longest Palindromic Subsequence II
Medium
Maximize Palindrome Length From Subsequences
Hard
Maximum Product of the Length of Two Palindromic Subsequences
Medium
''')

