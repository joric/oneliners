from lc import *

# https://leetcode.com/problems/maximum-number-of-balloons/description/?envType=daily-question&envId=2026-06-22

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = {"b":0, "a":0, "l":0, "o":0, "n":0}
        for c in text:
            if c in d:
                d[c] += 1
        d["l"] //= 2
        d["o"] //= 2
        return min(d.values())

class Solution:
    def maxNumberOfBalloons(self, t: str) -> int:
        return min(t.count(c)//((c in'lo')+1)for c in'balon')

test('''
1189. Maximum Number of Balloons
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
 

Note: This question is the same as 2287: Rearrange Characters to Make Target String.

 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
337,434/559.5K
Acceptance Rate
60.3%
Topics
Mid Level
Hash Table
String
Counting
Weekly Contest 154
icon
Companies
Hint 1
Count the frequency of letters in the given string.
Hint 2
Find the letter than can make the minimum number of instances of the word "balloon".
''')
