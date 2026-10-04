from lc import *

# https://leetcode.com/problems/score-of-parentheses/solutions/141778/1-line-python-by-lee215-xh29/?envType=daily-question&envId=2026-10-05

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        return eval(s.replace(')(',')+(').replace('()','1').replace(')',')*2'))

# https://leetcode.com/problems/score-of-parentheses/solutions/6553896/python-one-liner-by-ausesa-7nof/?envType=daily-question&envId=2026-10-05

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        return eval(s.replace('()','+1').replace('(','+2*('))

test('''
856. Score of Parentheses
Solved
Medium
Topics
premium lock icon
Companies
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
233,363/367.7K
Acceptance Rate
63.5%
Topics
Staff
String
Stack
Bracket Sequences
Weekly Contest 90
''')
