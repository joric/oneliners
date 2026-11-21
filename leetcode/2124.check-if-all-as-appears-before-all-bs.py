from lc import *

# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/description/?envType=daily-question&envId=2026-11-22

class Solution:
    def checkString(self, s: str) -> bool:
        return s.find('ba')<0

class Solution:
    def checkString(self, s: str) -> bool:
        return'ba'not in s

test('''
2124. Check if All A's Appears Before All B's
Easy
Topics
premium lock icon
Companies
Hint
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

 

Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.
Example 2:

Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.
Example 3:

Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.
 

Constraints:

1 <= s.length <= 100
s[i] is either 'a' or 'b'.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
137,515/187.2K
Acceptance Rate
73.5%
Topics
Mid Level
String
Weekly Contest 274
icon
Companies
Hint 1
You can check the opposite: check if there is a ‘b’ before an ‘a’. Then, negate and return that answer.
Hint 2
s should not have any occurrences of “ba” as a substring.
Similar Questions
Minimum Deletions to Make String Balanced
Medium
Check if Array Is Sorted and Rotated
Easy
Check if Numbers Are Ascending in a Sentence
Easy
''')
