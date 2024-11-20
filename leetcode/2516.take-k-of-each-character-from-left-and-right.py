from lc import *

# https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/discuss/2948183/Python-clean-12-line-sliding-window-solution-with-explanation
# TODO

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        t=j=0
        d = {c:s.count(c)-k for c in 'abc'}
        p = {c:0 for c in 'abc'}
        if any(x<0 for x in d.values()):
            return -1
        for i,c in enumerate(s):
            p[c] += 1
            while p[c]>d[c]:
                p[s[j]] -= 1
                j += 1
            t = max(t, i-j+1)
        return len(s) - t

test('''
2516. Take K of Each Character From Left and Right
Medium

732

65

Add to List

Share
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
Accepted
18,338
Submissions
52,823
''')
