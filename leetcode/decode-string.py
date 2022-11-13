from lc import *

class Solution:
    def decodeString(self, s: str) -> str:
        res, x, st = '',0,[]
        for c in s:
            if c.isdigit():
                x = x*10 + int(c)
            elif c=='[':
                st += x,
                st += res,
                x, res = 0, ''
            elif c==']':
                p = st.pop()
                y = st.pop()
                res = p + y * res
            else:
                res += c
        return res

# https://leetcode.com/problems/decode-string/discuss/87536/3-lines-Python-2-lines-Ruby-regular-expression

class Solution:
    def decodeString(self, s: str) -> str:
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
        return s

class Solution:
    def decodeString(self, s: str) -> str:
        return all(takewhile(lambda s:'[' in s, (s:=re.sub(r'(\d+)\[([a-z]*)\]',lambda m:int(m.group(1))*m.group(2), s) for _ in count()))) and s

test('''

394. Decode String
Medium

9760

427

Add to List

Share
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].

''')
