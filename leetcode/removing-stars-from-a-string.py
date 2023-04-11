from lc import *

class Solution:
    def removeStars(self, s: str) -> str:
        i,r = 0,''
        for c in s[::-1]:
            if c=='*':
                i += 1
            elif i>0:
                i -= 1
            elif i==0:
                r += c
        return r[::-1]

class Solution:
    def removeStars(self, s: str) -> str:
        r = []
        for c in s:
            if c == '*':
                r.pop()
            else:
                r.append(c)
        return ''.join(r)

class Solution:
    def removeStars(self, s: str) -> str:
        return ''.join(next((r for c in s if (not r.pop() if c=='*' else r.append(c))),r:=[]))

class Solution:
    def removeStars(self, s: str) -> str:
        return ''.join(reduce(lambda r,c:(c=='*' and r.pop() or not r.append(c)) and r,s,[]))

class Solution:
    def removeStars(self, s: str) -> str:
        return (r:=[]) or [(c=='*' and r.pop() or r.append(c)) for c in s] and ''.join(r)

test('''
2390. Removing Stars From a String
Medium

1111

78

Add to List

Share
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
 

Example 1:

Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
Example 2:

Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase English letters and stars *.
The operation above can be performed on s.
Accepted
62,530
Submissions
89,101
Seen this question in a real interview before?

Yes

No
Backspace String Compare
Easy
Remove All Adjacent Duplicates In String
Easy
What data structure could we use to efficiently perform these removals?
Use a stack to store the characters. Pop one character off the stack at each star. Otherwise, we push the character onto the stack.
''')

