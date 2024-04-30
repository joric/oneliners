from lc import *

# https://leetcode.com/problems/number-of-wonderful-substrings/discuss/1299552/JavaC%2B%2BPython-Bit-Mask-%2B-Prefix

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [1] + [0] * 1024
        res = cur = 0
        for c in word:
            cur ^= 1 << (ord(c) - ord('a'))
            res += count[cur]
            res += sum(count[cur ^ (1 << i)] for i in range(10))
            count[cur] += 1
        return res

class Solution:
    def wonderfulSubstrings(self, w: str) -> int:
        r=c=0;d=[1]+[0]*1024;[(c:=c^1<<(ord(i)-97),r:=r+d[c]+sum(d[c^(1<<i)]for i in range(10)),setitem(d,c,d[c]+1))for i in w];return r

class Solution:
    def wonderfulSubstrings(self, w: str) -> int:
        c,d=0,[1]+[0]*1024;return sum((c:=c^1<<(ord(i)-97),d[c]+sum(d[c^(1<<i)]for i in range(10)),setitem(d,c,d[c]+1))[1]for i in w)

class Solution:
    def wonderfulSubstrings(self, w: str) -> int:
        c,d=0,[1]+[0]*1024;return sum((d[c:=c^1<<(ord(i)-97)]+sum(d[c^(1<<i)]for i in range(10)),setitem(d,c,d[c]+1))[0]for i in w)

test('''
1915. Number of Wonderful Substrings
Medium

988

67

Add to List

Share
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"
Example 2:

Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"
Example 3:

Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "he" -> "h"
- "he" -> "e"
 

Constraints:

1 <= word.length <= 105
word consists of lowercase English letters from 'a' to 'j'.
Accepted
14,478
Submissions
30,930
''')
