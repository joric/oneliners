from lc import *

class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J] 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f, a, b, q, r = lambda x, y: all(x[c]>=y[c] for c in y), Counter(), Counter(t), deque(), ''
        for i, c in enumerate(s):
            a[c] += 1
            q.append(i)
            while f(a, b):
                r = s[q[0]:q[-1]+1] if not r or len(r) > q[-1]-q[0]+1 else r
                a[s[q.popleft()]] -= 1
        return r

test('''
76. Minimum Window Substring

Hard

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 10**5
s and t consist of uppercase and lowercase English letters.
''')
