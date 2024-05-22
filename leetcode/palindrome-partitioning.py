from lc import *

# https://leetcode.com/problems/palindrome-partitioning/discuss/42025/1-liner-Python-Ruby

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return[[s[:i]]+p for i in range(1,len(s)+1) if s[:i]==s[i-1::-1] for p in self.partition(s[i:])]or[[]]

# updated 2024-05-22

class Solution:
    def partition(t, s: str) -> List[List[str]]:
        return[[s[:i],*p]for i in range(1,len(s)+1)if s[:i]==s[i-1::-1]for p in t.partition(s[i:])]or[[]]


test('''

131. Palindrome Partitioning
Medium

9127

297

Add to List

Share
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

''')

