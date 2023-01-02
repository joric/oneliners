from lc import *

def check(res, expected, s):
    p = []
    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                p.append(s[i:j])
    w = len(max(p, key = len))
    return res in (s for s in p if len(s)==w)

class Solution1:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n): dp[i][i] = True
        ans = s[0:1]
        for i in range(n):
            for j in range(i-1, -1, -1):
                if s[i] == s[j] and (i-j<2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    if i - j + 1 > len(ans):
                        ans = s[j:i+1]
        return ans

# Manacher algorithm http://en.wikipedia.org/wiki/Longest_palindromic_substring
class Solution:
    def longestPalindrome(self, s):
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C, R = i, i + P[i]
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

# TODO

test('''
5. Longest Palindromic Substring

Medium

Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

''', check=check)
