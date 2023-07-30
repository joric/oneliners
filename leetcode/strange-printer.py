from lc import *

# https://leetcode.com/problems/strange-printer/discuss/233067/Python.-Recursive-approach-with-memorization

class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def f(s):
            if not s:
                return 0
            r = f(s[:-1])+1
            for i in range(len(s)-1):
                if s[i]==s[-1]:
                    r = min(r,f(s[:i+1])+f(s[i+1:-1]))
            return r
        return f(s)

class Solution:
    def strangePrinter(self, s: str) -> int:
        return(f:=cache(lambda s:s and reduce(lambda r,i:min(r,s[i]==s[-1]and f(s[:i+1])+f(s[i+1:-1])or r),range(len(s)-1),f(s[0:-1])+1)or 0))(s)

class Solution:
    def strangePrinter(self, s: str) -> int:
        return(f:=cache(lambda s:s and(r:=f(s[:-1])+1,[r:=min(r,f(s[:i+1])+f(s[i+1:-1]))for i in range(len(s)-1)if s[i]==s[-1]],r)[2]or 0))(s)

class Solution:
    def strangePrinter(self, s: str) -> int:
        return(f:=cache(lambda s:s and min([f(s[:-1])+1]+[f(s[:i+1])+f(s[i+1:-1])for i in range(len(s)-1)if s[i]==s[-1]])or 0))(s)

class Solution:
    def strangePrinter(self, s: str) -> int:
        def f(i,j):
            if i==j:
                return 0
            r = f(i,j-1)+1
            for k in range(i,j-1):
                if s[k] == s[j-1]:
                    r = min(r,f(i,k+1)+f(k+1,j-1))
            return r
        return f(0, len(s))

class Solution:
    def strangePrinter(self, s: str) -> int:
        return(f:=cache(lambda i,j:i<j and min([f(i,j-1)+1]+[f(i,k+1)+f(k+1,j-1)for k in range(i,j-1)if s[k]==s[j-1]])))(0,len(s))

test('''
664. Strange Printer
Hard

1111

100

Add to List

Share
There is a strange printer with the following two special properties:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any place and will cover the original existing characters.
Given a string s, return the minimum number of turns the printer needed to print it.

 

Example 1:

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
 

Constraints:

1 <= s.length <= 100
s consists of lowercase English letters.
''')
