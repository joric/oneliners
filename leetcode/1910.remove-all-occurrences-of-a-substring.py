from lc import *

# https://leetcode.com/problems/remove-all-occurrences-of-a-substring

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_length = len(part)
        for char in s:
            stack.append(char)
            if len(stack) >= part_length and self._check_match(stack, part, part_length):
                for _ in range(part_length):
                    stack.pop()
        return ''.join(stack)
    def _check_match(self, stack: list, part: str, part_length: int) -> bool:
        return ''.join(stack[-part_length:]) == part

class Solution:
    def removeOccurrences(self, s: str, p: str) -> str:
        [s:=re.sub(p,'',s,1)for _ in s];return s

test('''
1910. Remove All Occurrences of a Substring
Medium
Topics
Companies
Hint
Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "daabcbaabcbc", part = "abc"
Output: "dab"
Explanation: The following operations are done:
- s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc".
- s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc".
- s = "dababc", remove "abc" starting at index 3, so s = "dab".
Now s has no occurrences of "abc".
Example 2:

Input: s = "axxxxyyyyb", part = "xy"
Output: "ab"
Explanation: The following operations are done:
- s = "axxxxyyyyb", remove "xy" starting at index 4 so s = "axxxyyyb".
- s = "axxxyyyb", remove "xy" starting at index 3 so s = "axxyyb".
- s = "axxyyb", remove "xy" starting at index 2 so s = "axyb".
- s = "axyb", remove "xy" starting at index 1 so s = "ab".
Now s has no occurrences of "xy".
 

Other examples:

Input: s = "aabababa", part = "aba"
Output: "ba"

Constraints:

1 <= s.length <= 1000
1 <= part.length <= 1000
s​​​​​​ and part consists of lowercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
183.6K
Submissions
234.6K
Acceptance Rate
78.2%
Topics
String
Stack
Simulation
Companies
Hint 1
Note that a new occurrence of pattern can appear if you remove an old one, For example, s = "ababcc" and pattern = "abc".
Hint 2
You can maintain a stack of characters and if the last character of the pattern size in the stack match the pattern remove them
''')
