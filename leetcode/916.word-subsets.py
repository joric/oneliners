from lc import *

# https://leetcode.com/problems/word-subsets/solutions/176850/2-line-python/?envType=daily-question&envId=2025-01-10

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        return (lambda c:[a for a in words1 if not c-Counter(a)])(reduce(lambda a,b:a|Counter(b), words2, Counter()))

# POTD 2025-01-10

class Solution:
    def wordSubsets(self, a: List[str], b: List[str]) -> List[str]:
        c=reduce(ior,map(Counter,b));return[w for w in a if Counter(w)&c==c]

class Solution:
    def wordSubsets(self, a: List[str], b: List[str]) -> List[str]:
        c=Counter;t=reduce(ior,map(c,b));return[w for w in a if c(w)&t==t]

class Solution:
    def wordSubsets(self, a: List[str], b: List[str]) -> List[str]:
        return compress(a,map(reduce(ior,map(Counter,b)).__le__,map(Counter,a)))

class Solution:
    def wordSubsets(self, a: List[str], b: List[str]) -> List[str]:
        c=Counter;t=reduce(ior,map(c,b));return[w for w in a if t<=c(w)]

class Solution:
    def wordSubsets(self, a: List[str], b: List[str]) -> List[str]:
        t=reduce(ior,map(c:=Counter,b));return[w for w in a if t<=c(w)]

test('''
916. Word Subsets
Medium

2483

206

Add to List

Share
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
 

Constraints:

1 <= words1.length, words2.length <= 10^4
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
''')
