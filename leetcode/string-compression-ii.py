#!/usr/bin/env python3

from Leetcode import *

class Solution1:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache 
        def dp(i, k, prev, cnt):
            if k < 0:
                return inf 
            if i == len(s):
                return 0
            ans = dp(i+1, k-1, prev, cnt)
            if prev == s[i]: 
                delta = (0 if cnt not in [9, 99] else 1)
                delta += 1 if cnt==1 else 0
                ans = min(ans, dp(i+1, k, s[i], cnt+1) + delta)
            else: 
                ans = min(ans, dp(i+1, k, s[i], 1) + 1)
            return ans 
        return dp(0, k, "", 0)


class Solution2:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache 
        def dp(i, k, p, c):
            if k < 0:
                return inf 
            if i == len(s):
                return 0
            r = dp(i+1,k-1,p,c)
            if p==s[i]: 
                d = (0 if c not in [9, 99] else 1)
                d += 1 if c==1 else 0
                r = min(r, dp(i+1,k,s[i],c+1)+d)
            else: 
                r = min(r, dp(i+1,k,s[i],1)+1)
            return r

        return dp(0, k, "", 0)

# https://leetcode.com/problems/string-compression-ii/discuss/1562489/Python-DP-solution

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        return (f:=cache(lambda i,k,p,c:inf if k<0 else 0 if i==len(s) else min(f(i+1,k-1,p,c),f(i+1,k,s[i],c+1)+int(c in [1,9,99])) if p==s[i] else min(f(i+1,k-1,p,c), f(i+1,k,s[i],1)+1)))(0,k,'',0)

test(Solution,'''
Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.

 

Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.
Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
 

Constraints:

1 <= s.length <= 100
0 <= k <= s.length
s contains only lowercase English letters.
''')
