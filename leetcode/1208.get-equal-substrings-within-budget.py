from lc import *

# https://leetcode.com/problems/get-equal-substrings-within-budget/discuss/392837/JavaC%2B%2BPython-Sliding-Window

class Solution:
    def equalSubstring(self, s: str, t: str, m: int) -> int:
        i = 0
        for j in range(len(s)):
            m -= abs(ord(s[j])-ord(t[j]))
            if m < 0:
                m += abs(ord(s[i])-ord(t[i]))
                i += 1
        return j-i+1

class Solution:
    def equalSubstring(self, s: str, t: str, m: int) -> int:
        i=0;s,t=[[*map(ord,x)]for x in(s,t)];[0>(m:=m-abs(s[j]-t[j]))and(m:=m+abs(s[i]-t[i]),i:=i+1)for j in range(len(s))];return len(s)-i

class Solution:
    def equalSubstring(self, s: str, t: str, m: int) -> int:
        i,d=0,[abs(ord(a)-ord(b))for a,b in zip(s,t)];[0>(m:=m-d[j])and(m:=m+d[i],i:=i+1)for j in range(len(s))];return len(s)-i

class Solution:
    def equalSubstring(self, s: str, t: str, m: int) -> int:
        i,n,f=0,len(s),lambda i:abs(ord(s[i])-ord(t[i]));[0>(m:=m-f(j))and(m:=m+f(i),i:=i+1)for j in range(n)];return n-i


class Solution:
    def equalSubstring(self, s: str, t: str, m: int) -> int:
        i,f=len(s)-1,lambda i:abs(ord(s[i])-ord(t[i]));[0>(m:=m-f(j))and(m:=m+f(i),i:=i+1)for j in range(n)];return n-i


test('''
1208. Get Equal Substrings Within Budget
Medium

1184

74

Add to List

Share
You are given two strings s and t of the same length and an integer maxCost.

You want to change s to t. Changing the ith character of s to ith character of t costs |s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

Return the maximum length of a substring of s that can be changed to be the same as the corresponding substring of t with a cost less than or equal to maxCost. If there is no substring from s that can be changed to its corresponding substring from t, return 0.

 

Example 1:

Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" of s can change to "bcd".
That costs 3, so the maximum length is 3.
Example 2:

Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in s costs 2 to change to character in t,  so the maximum length is 1.
Example 3:

Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any change, so the maximum length is 1.
 

Other examples:

Input: s = "pxezla", t = "loewbi", maxCost = 25
Output: 4

Constraints:

1 <= s.length <= 105
t.length == s.length
0 <= maxCost <= 106
s and t consist of only lowercase English letters.
Accepted
56,063
Submissions
109,275
''')