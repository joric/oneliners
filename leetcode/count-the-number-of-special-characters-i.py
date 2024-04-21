from lc import *

# Q1. https://leetcode.com/contest/weekly-contest-394/
# https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, w: str) -> int:
        d=Counter(w);return sum(c in d and c.upper() in d for c in ascii_lowercase)

class Solution:
    def numberOfSpecialChars(self, w: str) -> int:
        return sum(c in w and c.upper()in w for c in ascii_lowercase)

test('''
3120. Count the Number of Special Characters I
Easy

16

0

Add to List

Share
You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.

Example 3:

Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.

 

Constraints:

1 <= word.length <= 50
word consists of only lowercase and uppercase English letters.
Accepted
19,860
Submissions
33,726
''')

