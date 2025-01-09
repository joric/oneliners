from lc import *

# https://leetcode.com/problems/counting-words-with-a-given-prefix/solutions/1809593/python-one-line-simple-solution/?envType=daily-question&envId=2025-01-09


class Solution:
    def prefixCount(self, d: List[str], p: str) -> int:
        return sum(map(lambda w:w.startswith(p),d))

class Solution:
    def prefixCount(self, d: List[str], p: str) -> int:
        return sum(w.startswith(p)for w in d)

class Solution:
    def prefixCount(self, d: List[str], p: str) -> int:
        return sum(p==w[:len(p)]for w in d)

class Solution:
    def prefixCount(self, d: List[str], p: str) -> int:
        return sum(0==w.find(p)for w in d)

test('''
2185. Counting Words With a Given Prefix
Easy
Topics
Companies
Hint
You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
Example 2:

Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length, pref.length <= 100
words[i] and pref consist of lowercase English letters.
''')
