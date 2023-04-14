from lc import *

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return (f:=cache(lambda s:len(s) if len(s)<=1 else f(s[1:-1])+2 if s[0]==s[-1] else max(f(s[1:]),f(s[:-1]))))(s)

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

