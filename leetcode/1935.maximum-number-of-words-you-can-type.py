from lc import *

# https://leetcode.com/problems/maximum-number-of-words-you-can-type/solutions/1353222/python-3-easy-1-line-using-set/?envType=daily-question&envId=2025-09-15

class Solution:
    def canBeTypedWords(self, t: str, b: str) -> int:
        return sum(not{*s}&{*b}for s in t.split())

test('''
1935. Maximum Number of Words You Can Type
Easy
Topics
premium lock icon
Companies
Hint
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

 

Example 1:

Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.
Example 2:

Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
Example 3:

Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.
 

Constraints:

1 <= text.length <= 104
0 <= brokenLetters.length <= 26
text consists of words separated by a single space without any leading or trailing spaces.
Each word only consists of lowercase English letters.
brokenLetters consists of distinct lowercase English letters.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
99,598/127.1K
Acceptance Rate
78.3%
Topics
Hash Table
String
Weekly Contest 250
icon
Companies
Hint 1
Check each word separately if it can be typed.
Hint 2
A word can be typed if all its letters are not broken.
''')
