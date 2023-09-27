from lc import *

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        i = 0
        for c in s:
            i = i * int(c) if c.isdigit() else i + 1
        for c in s[::-1]:
            k %= i
            if k == 0 and c.isalpha():
                return c
            i = i // int(c) if c.isdigit() else i - 1

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        i=0;[i:=i*int(c)if c.isdigit()else i+1 for c in s];return next(c for c in s[::-1]if(k:=k%i)==0 and c.isalpha()or(i:=i//int(c)if c.isdigit()else i-1)<0)

# https://leetcode.com/problems/decoded-string-at-index/discuss/4094809/JavaScript-5-Lines-Recursive-Time%3A-O(n)-Space%3A-O(n)

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        i = 0
        for c in s:
            if c.isdigit():
                x = int(c)
                if k>x*i:
                    i *= x
                else:
                    return self.decodeAtIndex(s, k%i or i)
            else:
                i += 1
                if i == k:
                    return c

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        return(f:=lambda k,i=0:next(t and f(k%i or i)or c for c in s if(t:=c.isdigit())and k<=i*int(c)or i==k-1or(i:=t and i*int(c)or i+1)<0))(k)

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        return(f:=lambda k,i=0:next(t and f(k%i or i)or c for c in s if(t:=(v:=ord(c)-48)<10)and k<=i*v or i==k-1or(i:=t and i*v or i+1)<0))(k)

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        return(f:=lambda k,i=0:next(v<10and f(k%i or i)or c for c in s if(v:=ord(c)-48)<10and k<=i*v or i==k-1or(i:=v<10and i*v or i+1)<0))(k)

test('''
880. Decoded String at Index
Medium

1650

246

Add to List

Share
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.

 

Example 1:

Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".
Example 3:

Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".
 

Constraints:

2 <= s.length <= 100
s consists of lowercase English letters and digits 2 through 9.
s starts with a letter.
1 <= k <= 10^9
It is guaranteed that k is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 263 letters.
Accepted
48,497
Submissions
157,077
''')

