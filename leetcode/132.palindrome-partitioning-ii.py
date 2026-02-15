from lc import *

# https://leetcode.com/problems/palindrome-partitioning-ii

class Solution:
    def minCut(self, s: str) -> int:
        cut = [x for x in range(-1,len(s))]
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if s[i:j] == s[j:i:-1]:
                    cut[j+1] = min(cut[j+1],cut[i]+1)
        return cut[-1]

class Solution:
    def minCut(self, s: str) -> int:
        n=len(s);c=[*range(-1,n)];[setitem(c,j+1,min(c[j+1],c[i]+1))for i in range(n)for j in range(i,n)if s[i:j]==s[j:i:-1]];return c[-1]

# https://leetcode.com/problems/palindrome-partitioning-ii/solutions/5449411/recursion-with-memoization-by-cxtra-sadr/

class Solution:
    def minCut(self, s: str) -> int:
        def isPalindrome(s):
            return s == s[::-1]
        def DP(s, start, memo):
            if start == len(s) or isPalindrome(s[start:]):
                return 0
            if start in memo:
                return memo[start]
            min_cuts = float('inf')
            for i in range(start, len(s)):
                if isPalindrome(s[start:i+1]):
                    min_cuts = min(min_cuts, DP(s, i+1, memo) + 1)
            memo[start] = min_cuts
            return min_cuts
        memo = {}
        return DP(s, 0, memo)

class Solution:
    def minCut(self, s: str) -> int:
        return(f:=cache(lambda s,i:s[i:]!=s[i:][::-1]and min(1+f(s,j+1)for j in range(i,len(s))if s[i:j+1]==s[i:j+1][::-1])or 0))(s,0)

test('''
132. Palindrome Partitioning II
Solved
Hard
Topics
premium lock icon
Companies
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
393,808/1.1M
Acceptance Rate
36.5%
Topics
String
Dynamic Programming
icon
Companies
Similar Questions
Palindrome Partitioning
Medium
Palindrome Partitioning IV
Hard
Maximum Number of Non-overlapping Palindrome Substrings
Hard
Number of Great Partitions
Hard
''')
