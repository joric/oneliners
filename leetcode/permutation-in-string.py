from lc import *

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        need, have = Counter(s1), Counter(s2[:n])
        for i in range(m-n):
            if need == have:
                return True
            have[s2[i]] -= have[s2[i]] > 0
            have[s2[i+n]] += 1
        return need == have

class Solution2:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return any(Counter(s1)==Counter(s2[i:i+len(s1)]) for i in range(len(s2)-len(s1)+1))


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
