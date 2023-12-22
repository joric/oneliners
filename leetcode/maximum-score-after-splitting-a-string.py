from lc import *

# https://leetcode.com/problems/maximum-score-after-splitting-a-string/discuss/4438486/One-line-solution

class Solution:
    def maxScore(self, s: str) -> int:
        return max(islice(accumulate(s,lambda i,c:i-int(c)*2+1,initial=s.count('1')),1,None))

class Solution:
    def maxScore(self, s: str) -> int:
        c,t=s.count('1'),0;return max(c-i+(t:=t+2*(s[i-1]<'1'))for i in range(1,len(s)))

# https://leetcode.com/problems/maximum-score-after-splitting-a-string/discuss/3297911/Python-one-line

class Solution:
    def maxScore(self, s: str) -> int:
        return max(s[:i].count('0')+s[i:].count('1')for i in range(1,len(s)))

test('''
1422. Maximum Score After Splitting a String
Easy

651

37

Add to List

Share
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3
 

Constraints:

2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
Accepted
51,077
Submissions
88,027
''')

