from lc import *

# https://leetcode.com/problems/word-break/discuss/2700603/4-line-pythonic

class Solution:
    def wordBreak(self, s: str, d: List[str]) -> bool:
        return(f:=cache(lambda s:not s or any((f(s[len(w):])for w in d if s.find(w)==0))))(s)

# https://leetcode.com/problems/word-break/discuss/716911/One-line-memoization

class Solution:
    def wordBreak(self, s: str, d: List[str]) -> bool:
        return(f:=cache(lambda s:not s or any(s[:len(w)]==w and f(s[len(w):])for w in d)))(s)

test('''
139. Word Break
Medium

14847

628

Add to List

Share
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
''')

