from lc import *

# Q2. https://leetcode.com/contest/weekly-contest-394/
# https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution:
    def numberOfSpecialChars(self, w: str) -> int:
        d = Counter()
        for i,c in enumerate(w):
            if c not in d or c != c.upper():
                d[c] = i                
        return sum(c in d and c.upper()in d and d[c]<d[c.upper()] for c in ascii_lowercase)

class Solution:
    def numberOfSpecialChars(self, w: str) -> int:
        d=Counter();[setitem(d,c,i)for i,c in enumerate(w)if c not in d or c!=c.upper()];return sum(c in d and c.upper()in d and d[c]<d[c.upper()] for c in ascii_lowercase)

# https://leetcode.com/problems/count-the-number-of-special-characters-ii/solutions/5072810/1-logical-line-python-by-stefanpochmann-ol91/?envType=daily-question&envId=2026-05-27

# POTD 2026-05-26

class Solution:
    def numberOfSpecialChars(self, w: str) -> int:
        return sum(0<=w.rfind(c)<w.find(c.upper())for c in ascii_lowercase)

class Solution:
    def numberOfSpecialChars(self, w: str) -> int:
        return sum(0<=w.rfind(c)<w.find(c.upper())for c in{*w.lower()})

test('''
3121. Count the Number of Special Characters II
Medium

20

2

Add to List

Share
You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

 

Example 1:

Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters are 'a', 'b', and 'c'.

Example 2:

Input: word = "abc"

Output: 0

Explanation:

There are no special characters in word.

Example 3:

Input: word = "AbBCab"

Output: 0

Explanation:

There are no special characters in word.

 

Constraints:

1 <= word.length <= 2 * 105
word consists of only lowercase and uppercase English letters.
Accepted
14,784
Submissions
42,173
''')