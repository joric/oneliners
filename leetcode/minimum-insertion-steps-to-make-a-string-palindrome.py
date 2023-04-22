from lc import *

class Solution:
    def minInsertions(self, s: str) -> int:
        @cache
        def f(l,r):
            if l>=r:
                return 0
            return f(l+1,r-1) if s[l]==s[r] else 1+min(f(l+1,r),f(l,r-1))
        return f(0,len(s)-1)

class Solution:
    def minInsertions(self, s: str) -> int:
        return (f:=cache(lambda l,r:int(l<r) and f(l+1,r-1) if s[l]==s[r] else 1+min(f(l+1,r),f(l,r-1))))(0,len(s)-1)

class Solution:
    @cache
    def minInsertions(self, s: str) -> int:
        if not s:
            return 0
        if s[0] == s[-1]:
            return self.minInsertions(s[1:-1])
        return 1 + min(self.minInsertions(s[1:]), self.minInsertions(s[:-1]))

# looks very similar to https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def minInsertions(self, s: str) -> int:
        return (f:=cache(lambda s:s and (f(s[1:-1]) if s[0]==s[-1] else 1+min(f(s[1:]),f(s[:-1]))) or 0))(s)

test('''
1312. Minimum Insertion Steps to Make a String Palindrome
Hard

3124

35

Add to List

Share
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

Example 4:
Input: s = "zzazz"
Output: 0

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
Accepted
77,460
Submissions
116,717
Seen this question in a real interview before?

Yes

No
Minimum Number of Moves to Make Palindrome
Hard
Is dynamic programming suitable for this problem ?
If we know the longest palindromic sub-sequence is x and the length of the string is n then, what is the answer to this problem? It is n - x as we need n - x insertions to make the remaining characters also palindrome.
''')

