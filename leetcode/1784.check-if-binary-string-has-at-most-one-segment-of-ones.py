from lc import *

# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/solutions/7625704/one-line-solution-by-mikposp-ci6c/?envType=daily-question&envId=2026-03-06

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return s.find('01')<0

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return'01'not in s

test('''
1784. Check if Binary String Has at Most One Segment of Ones
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most one contiguous segment of ones. Otherwise, return false.

 

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true
 

Constraints:

1 <= s.length <= 100
s[i]​​​​ is either '0' or '1'.
s[0] is '1'.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
58,819/149.3K
Acceptance Rate
39.4%
Topics
Mid Level
String
Weekly Contest 231
icon
Companies
Hint 1
It's guaranteed to have at least one segment
Hint 2
The string size is small so you can count all segments of ones with no that have no adjacent ones.
Similar Questions
Longer Contiguous Segments of Ones than Zeros
Easy
''')
