from lc import *

# https://leetcode.com/problems/reorganize-string/discuss/113435/4-lines-Python

class Solution:
    def reorganizeString(self, s: str) -> str:
        a=sorted(sorted(s),key=s.count);h=len(a)//2;a[1::2],a[::2]=a[:h],a[h:];return''.join(a)*(a[-1:]!=a[-2:-1])

test('''
767. Reorganize String
Medium

6698

215

Add to List

Share
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"
Example 2:

Input: s = "aaab"
Output: ""
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
Accepted
284,263
Submissions
533,166
Seen this question in a real interview before?

Yes

No
Rearrange String k Distance Apart
Hard
Task Scheduler
Medium
Longest Happy String
Medium
Alternate placing the most common letters.
''')

