from lc import *

# https://leetcode.com/problems/first-unique-character-in-a-string

# 70 ms
class Solution:
    def firstUniqChar(self, s: str) -> int:
        t=Counter(s);return next((i for i,c in enumerate(s)if t[c]<2),-1)

# 63 ms
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return s.find(next((k for k,v in Counter(s).items()if v<2),'$'))

# 54 ms
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return min([s.find(c)for c in{*s}if s.count(c)<2]or[-1])

# 9836 ms
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return s.find((*(c for c in s if s.count(c)<2),'$')[0])

# 4383 ms
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return next((s.find(с)for с in s if s.count(с)<2),-1)

# 9869 ms
class Solution:
    def firstUniqChar(self, s: str) -> int:
        return(*(s.find(с)for с in s if s.count(с)<2),-1)[0]

test('''
387. First Unique Character in a String
Easy

8554

278

Add to List

Share
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 10^5
s consists of only lowercase English letters.
Accepted
1,561,193
Submissions
2,560,073
''')
