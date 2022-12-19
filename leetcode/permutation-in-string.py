from lc import *

class Solution:
    def checkInclusion(self, a: str, b: str) -> bool:
        n, m = len(a), len(b)
        p, q = Counter(a), Counter(b[:n])
        for i in range(m-n):
            if p==q:
                return True
            q[b[i]] -= q[b[i]] > 0
            q[b[i+n]] += 1
        return p==q

class Solution:
    def checkInclusion(self, a: str, b: str) -> bool:
        return any(Counter(a)==Counter(b[i:i+len(a)]) for i in range(len(b)-len(a)+1))


test('''

567. Permutation in String
Medium

7748

258

Add to List

Share
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
Accepted
522,152
Submissions
1,197,635

''')
