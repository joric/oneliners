from lc import *

# https://leetcode.com/problems/reverse-string

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:]=s[::-1]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

test('''
344. Reverse String
Easy

8325

1155

Add to List

Share
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
Accepted
2,521,633
Submissions
3,236,687
''')
