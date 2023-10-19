from lc import *

# https://leetcode.com/problems/backspace-string-compare/discuss/135603/JavaC%2B%2BPython-O(N)-time-and-O(1)-space

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return reduce(f:=lambda r,c:r[:-1] if c=='#' else r+c,s,'')==reduce(f,t,'')

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return reduce(f:=lambda r,c:(r+c,r[:-1])[c=='#'],s,'')==reduce(f,t,'')

test('''

844. Backspace String Compare
Easy

5748

264

Add to List

Share
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

Example 4:

Input: s = "a##c", t = "#a#c"
Output: true

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?

''')
