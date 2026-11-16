from lc import *

# https://leetcode.com/problems/minimum-changes-to-make-k-semi-palindromes/solutions/4194487/python-dp-solution-by-lee215-7l7t/?envType=daily-question&envId=2026-11-17

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        div = defaultdict(lambda: [1])
        n = len(s)
        for d in range(2, n):
             for v in range(d + d, n + 1, d):
                div[v].append(d)

        def change(i, j):
            return min(semi(i, j, d) for d in div[j - i])

        @cache
        def semi(i, j, d):
            if i >= j: return 0
            return semi(i + d, j - d, d) + sum(s[i + ii] != s[j - d + ii] for ii in range(d))

        @cache
        def dp(i, k):
            if k == 1:
                return change(0, i)
            return min(dp(j, k - 1) + change(j, i) for j in range((k - 1) * 2, i - 1))

        return dp(n, k)

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        f=cache(lambda t,k:min(f(t[:j],k-1)+f(t[j:],0)for j in range(k*2,len(t)-1))if k else min(sum(c>t[p%d*2-p-d]for p,c in enumerate(t))for d in range(1,len(t))if len(t)%d<1));return f(s,k-1)

test('''
2911. Minimum Changes to Make K Semi-palindromes
Hard
Topics
premium lock icon
Companies
Hint
Given a string s and an integer k, partition s into k substrings such that the letter changes needed to make each substring a semi-palindrome are minimized.

Return the minimum number of letter changes required.

A semi-palindrome is a special type of string that can be divided into palindromes based on a repeating pattern. To check if a string is a semi-palindrome:​

Choose a positive divisor d of the string's length. d can range from 1 up to, but not including, the string's length. For a string of length 1, it does not have a valid divisor as per this definition, since the only divisor is its length, which is not allowed.
For a given divisor d, divide the string into groups where each group contains characters from the string that follow a repeating pattern of length d. Specifically, the first group consists of characters at positions 1, 1 + d, 1 + 2d, and so on; the second group includes characters at positions 2, 2 + d, 2 + 2d, etc.
The string is considered a semi-palindrome if each of these groups forms a palindrome.
Consider the string "abcabc":

The length of "abcabc" is 6. Valid divisors are 1, 2, and 3.
For d = 1: The entire string "abcabc" forms one group. Not a palindrome.
For d = 2:
Group 1 (positions 1, 3, 5): "acb"
Group 2 (positions 2, 4, 6): "bac"
Neither group forms a palindrome.
For d = 3:
Group 1 (positions 1, 4): "aa"
Group 2 (positions 2, 5): "bb"
Group 3 (positions 3, 6): "cc"
All groups form palindromes. Therefore, "abcabc" is a semi-palindrome.
 

Example 1:

Input: s = "abcac", k = 2

Output: 1

Explanation: Divide s into "ab" and "cac". "cac" is already semi-palindrome. Change "ab" to "aa", it becomes semi-palindrome with d = 1.

Example 2:

Input: s = "abcdef", k = 2

Output: 2

Explanation: Divide s into substrings "abc" and "def". Each needs one change to become semi-palindrome.

Example 3:

Input: s = "aabbaa", k = 3

Output: 0

Explanation: Divide s into substrings "aa", "bb" and "aa". All are already semi-palindromes.

 

Constraints:

2 <= s.length <= 200
1 <= k <= s.length / 2
s contains only lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
5,814/16.4K
Acceptance Rate
35.4%
Topics
Principal
Two Pointers
String
Dynamic Programming
Weekly Contest 368
icon
Companies
Hint 1
Define dp[i][j] as the minimum count of letter changes needed to split the suffix of string s starting from s[i] into j valid parts.
Hint 2
We have dp[i][j] = min(dp[x + 1][j - 1] + v[i][x]). Here v[i][x] is the minimum number of letter changes to change substring s[i..x] into semi-palindrome.
Hint 3
v[i][j] can be calculated separately by brute-force. We can create a table of v[i][j] independently to improve the complexity. Also note that semi-palindrome’s length is at least 2.
Similar Questions
Palindrome Partitioning III
Hard
''')
