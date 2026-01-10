from lc import *

# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/discuss/3840746/Python-Simple-6-lines

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        a,b = [*map(ord,a)],[*map(ord,b)]
        m,n = len(a),len(b)
        d = [[0 for _ in range(m)]for _ in range(n)]
        for j,i in product(range(m),range(n)):
            d[i][j] = max((j>0)*d[i][j-1],(i>0)*d[i-1][j],(a[j]==b[i])*((i>0 and j>0)*d[i-1][j-1]+a[j]))
        return sum(a)+sum(b)-2*d[-1][-1]

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        a,b=[*map(ord,a)],[*map(ord,b)];m,n=len(a),len(b);d=[[0 for _ in range(m)]for _ in range(n)];[setitem(d[i],j,max((j>0)*d[i][j-1],(i>0)*d[i-1][j],(a[j]==b[i])*((i>0<j)*d[i-1][j-1]+a[j])))for j,i in product(range(m),range(n))];return sum(a)+sum(b)-2*d[-1][-1]

# another solution

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        @cache
        def f(i,j):
            if i<len(a) and j<len(b) and a[i]==b[j]:
                return f(i+1,j+1)
            p = i<len(a) and f(i+1,j)+ord(a[i])
            q = j<len(b) and f(i,j+1)+ord(b[j])
            return min(p,q) if i<len(a) and j<len(b) else max(p,q)
        return f(0,0)

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        return(f:=cache(lambda i,j:f(i+1,j+1)if(t:=i<len(a)and j<len(b))and a[i]==b[j]else([max,min][t])(i<len(a)and f(i+1,j)+ord(a[i]),j<len(b)and f(i,j+1)+ord(b[j]))))(0,0)

# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/discuss/2312674/Python-recursive-solution

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        @cache
        def f(i,j):
            if i<len(a) and j<len(b):
                return f(i+1,j+1) if a[i]==b[j] else min(f(i+1,j)+ord(a[i]),f(i,j+1)+ord(b[j]))
            return sum(map(ord,(b[j:],a[i:])[i<len(a)]))
        return f(0,0)

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        return(f:=cache(lambda i,j:(f(i+1,j+1)if a[i]==b[j]else min(f(i+1,j)+ord(a[i]),f(i,j+1)+ord(b[j])))if i<len(a)and j<len(b)else sum(map(ord,(b[j:],a[i:])[i<len(a)]))))(0,0)

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        t=ord;return(f:=cache(lambda i,j:min(f(i+1,j)+t(a[i]),f(i,j+1)+t(b[j]),f(i+1,j+1)+999*(a[i]!=b[j]))if(a[i:]and b[j:])else sum(map(t,b[j:]+a[i:]))))(0,0)

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        return(f:=cache(lambda i,j:min(f(i+1,j)+ord(a[i]),f(i,j+1)+ord(b[j]),f(i+1,j+1)+999*(a[i]!=b[j]))if(a[i:]and b[j:])else sum(map(ord,b[j:]+a[i:]))))(0,0)

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        return(f:=cache(lambda i,j:min(f(i+1,j+1)+999*(a[i]!=b[j]),f(i+1,j)+ord(a[i]),f(i,j+1)+ord(b[j]))if a[i:]and b[j:]else sum(map(ord,b[j:]+a[i:]))))(0,0)

# another solution

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        @cache
        def f(a,b):
            if a and b:
                return f(a[1:],b[1:]) if a[0]==b[0] else min(ord(a[0])+f(a[1:],b),ord(b[0])+f(a,b[1:]))
            return sum(map(ord,a+b))
        return f(a,b)

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        return(f:=cache(lambda a,b:(f(a[1:],b[1:])if a[0]==b[0]else min(ord(a[0])+f(a[1:],b),ord(b[0])+f(a,b[1:])))if a and b else sum(map(ord,a+b))))(a,b)

# 2026-01-10 POTD

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        return sum(map(ord,a+b))-2*(f:=cache(lambda a,b:a and b and(a[0]==b[0]and ord(a[0])+f(a[1:],b[1:])or max(f(a[1:],b),f(a,b[1:])))or 0))(a,b)

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        return(f:=cache(lambda i,j:(f(i+1,j+1)if a[i]==b[j]else min(ord(a[i])+f(i+1,j),ord(b[j])+f(i,j+1)))if a[i:]and b[j:]else sum(map(ord,a[i:]+b[j:]))))(0,0)

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        return sum(map(ord,a+b))-2*(f:=cache(lambda i,j:a[i:]and b[j:]and(a[i]==b[j]and ord(a[i])+f(i+1,j+1)or max(f(i+1,j),f(i,j+1)))or 0))(0,0)

class Solution:
    def minimumDeleteSum(self, a: str, b: str) -> int:
        return sum(map(ord,a+b))-2*(f:=cache(lambda i,j:a[i:]and b[j:]and(a[i]==b[j]and ord(a[i])+f(i+1,j+1)or max(f(i+1,j),f(i,j+1)))or 0))(0,0)

test('''
712. Minimum ASCII Delete Sum for Two Strings
Medium

3102

81

Add to List

Share
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 

Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
''')
