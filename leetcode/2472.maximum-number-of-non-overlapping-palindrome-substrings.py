from lc import *

# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/solutions/2809337/pythonc-recursive-iterative-dp-solutions-00eg/?envType=daily-question&envId=2026-09-15

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        def pal(i, j):                                        # [a] if you dare to solve hard problems then you
            if j > len(s) : return False                      #     probably know many ways to test palindromes;
            return s[i:j] == s[i:j][::-1]                     #     this one is for clarity, not for speed
        @lru_cache(None)                                      # [b] this recursive function finds the maximal
        def dfs(i):                                           #     number of non-overlapping palindroms in
            if i + k > len(s) : return 0                      #     the string 's' if we start at position 'i';
            m = dfs(i+1)                                      # [c] we consider cases when there is a palindrome 
            if pal(i,i+k)   : m = max(m, 1 + dfs(i+k))        #     of length k/k+1 at the i-th position or when
            if pal(i,i+k+1) : m = max(m, 1 + dfs(i+k+1))      #     there is no such palindrome (and we take the
            return m                                          #     number of palindromes for the i+1-th position)
        return dfs(0)

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        return reduce(lambda l,j:(l[0]+1,j)if(i:=j-k)>=l[1]and(a:=s[i:j])==a[::-1]or l[1]<i and(a:=s[i-1:j])==a[::-1]else l,range(k,len(s)+1),(0,0))[0]

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        return(f:=lambda p:k<=len(p)and((a:=p[:k])==a[::-1]and-~f(p[k:])or p[k:]and(b:=a+p[k])==b[::-1]and-~f(p[k+1:])or f(p[1:])))(s)|0

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        return+(f:=lambda s:k<=len(s)and(s[:k]==s[k-1::-1]and-~f(s[k:])or s[:k+1]==s[k::-1]and-~f(s[k+1:])or f(s[1:])))(s)

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        return+(f:=cache(lambda s:k<=len(s)and next((-~f(s[j:])for j in(k,k+1)if s[:j]==s[j-1::-1]),f(s[1:]))))(s)

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        return+(f:=cache(lambda s:k<=len(s)and[*[-~f(s[j:])for j in(k,k+1)if s[:j]==s[j-1::-1]],f(s[1:])][0]))(s)

test('''
2472. Maximum Number of Non-overlapping Palindrome Substrings
Hard
Topics
premium lock icon
Companies
Hint
You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.
 

Constraints:

1 <= k <= s.length <= 2000
s consists of lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
27,992/61.8K
Acceptance Rate
45.3%
Topics
Senior Staff
Two Pointers
String
Dynamic Programming
Greedy
Weekly Contest 319
icon
Companies
Hint 1
Try to use dynamic programming to solve the problem.
Hint 2
let dp[i] be the answer for the prefix s[0…i].
Hint 3
The final answer to the problem will be dp[n-1]. How do you compute this dp?
Similar Questions
Longest Palindromic Substring
Medium
Palindrome Partitioning
Medium
Palindrome Partitioning II
Hard
Palindrome Partitioning III
Hard
Maximum Number of Non-Overlapping Substrings
Hard
Palindrome Partitioning IV
Hard
''')
