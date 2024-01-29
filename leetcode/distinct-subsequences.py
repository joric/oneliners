from lc import *

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        p=[0]*len(t)
        for c in s:
            d = 1
            p = [((c==j)*d)+(d:=i) for i,j in zip(p,t)]
        return p[-1]

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        p=[0]*len(t);all((d:=1,p:=[((c==j)*d)+(d:=i)for i,j in zip(p,t)])for c in s);return p[-1]

test('''
115. Distinct Subsequences
Hard

6423

282

Add to List

Share
Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
Accepted
366,915
Submissions
794,122
''')
