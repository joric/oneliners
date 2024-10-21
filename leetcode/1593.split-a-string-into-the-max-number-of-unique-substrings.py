from lc import *

# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/discuss/1018747/Python3-4-Lines-Easy-Backtracking

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(s, path=set()):
            if not s: return len(path)
            return max([dfs(s[i:], path|{s[:i]}) for i in range(1, len(s)+1) if s[:i] not in path] + [-inf])
        return dfs(s)

# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/discuss/855359/Python-One-Liner

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return(f:=lambda j,v=set():max([1+f(j+i,v|{s[j:j+i]})for i in range(1,len(s)-j+1)if s[j:j+i]not in v]+[0]))(0)

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return(f:=lambda s,v:max([1+f(s[i+1:],{c,*v})for i in range(len(s))if(c:=s[:i+1])not in v]+[0]))(s,())

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return(f:=lambda s,v:max([1+f(s[i:],{c,*v})for i in range(1,len(s)+1)if(c:=s[:i])not in v]+[0]))(s,())

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return(f:=lambda s,v:max([1+f(s[i:],{s[:i],*v})for i in range(1,len(s)+1)if s[:i]not in v]+[0]))(s,())

# updated 2024-10-21 (POTD)

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return(f:=lambda s,v:1+max(s[:i]in v or f(s[i:],{s[:i],*v})for i in range(1,len(s)+2)))(s,())-3

test('''
1593. Split a String Into the Max Number of Unique Substrings
Medium

863

38

Add to List

Share
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.

Accepted
34,673
Submissions
60,190
''')
