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
132. Palindrome Partitioning

Examples:

Input: s = "bababcbadcede"
Output: 4

Explanation: If we do 4 partitions in the following way, each substring of the partition will be a palindrome.
bab | abcba | d | c | ede.

Input: s = "aab"
Output: 1 

Explanation: If we do 1 partition in the following way, each substring of the partition will be a palindrome.
aa | b.
''')
