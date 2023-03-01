from lc import *

def check(res, expected, s):
    p = []
    for i in range(len(s)+1):
        for j in range(i+1, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                p.append(s[i:j])
    w = len(max(p, key = len))
    return res in (s for s in p if len(s)==w)

class Solution:
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
    def longestPalindrome(self, s: str) -> str:
        t = '#'.join('^{}$'.format(s))
        n = len(t)
        p = [0]*n
        c = r = 0
        for i in range (1, n-1):
            p[i] = (r>i) and min(r-i,p[2*c - i])
            while t[i+1+p[i]]==t[i-1-p[i]]:
                p[i]+=1
            if i+p[i]>r:
                c = i
                r = i+p[i]
        m,d = max((n, i) for i, n in enumerate(p))
        return s[(d-m)//2:(d+m)//2]


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return (t:='#'.join('^{}$'.format(s)),n:=len(t),p:=[0]*n,c:=0,r:=0,[(setitem(p,i,(r>i) and min(r-i,p[2*c - i])),next(0 for _ in count() if not(t[i+1+p[i]]==t[i-1-p[i]] and (setitem(p,i,p[i]+1),i+p[i]>r and (c:=i,r:=i+p[i]))))) for i in range (1,n-1)],v:=max((n, i) for i, n in enumerate(p)),s[(v[1]-v[0])//2:sum(v)//2])[-1]

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
