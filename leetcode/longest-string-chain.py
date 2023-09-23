from lc import *

# https://leetcode.com/problems/longest-string-chain/discuss/294890/JavaC%2B%2BPython-DP-Solution

class Solution:
    def longestStrChain(self, s: List[str]) -> int:
        d={};[setitem(d,w,max(d.get(w[:i]+w[i+1:],0)+1for i in range(len(w))))for w in sorted(s,key=len)];return max(d.values())

# https://leetcode.com/problems/longest-string-chain/discuss/2153436/python-beginner-recursion-%2B-memoization

class Solution:
    def longestStrChain(self, s: List[str]) -> int:
        @cache
        def f(w):
            if not w or w not in s:
                return 0
            c = 0
            for i in range(len(w)):
                c = max(c,1+f(w[0:i]+w[i+1:len(w)]))
            return c
        s=set(s)
        return max(f(w)for w in s)

# 436 ms
class Solution:
    def longestStrChain(self, s: List[str]) -> int:
        s=set(s);return max((f:=cache(lambda w:w in s and max(1+f(w[0:i]+w[i+1:len(w)])for i in range(len(w)))))(w)for w in s)

# 3234 ms, 10 chars shorter
class Solution:
    def longestStrChain(self, s: List[str]) -> int:
        return max((f:=cache(lambda w:w in s and max(1+f(w[0:i]+w[i+1:len(w)])for i in range(len(w)))))(w)for w in s)

test('''
1048. Longest String Chain
Medium

6365

228

Add to List

Share
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
Example 3:

Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["abcd","dbqca"] is not a valid word chain because the ordering of the letters is changed.
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of lowercase English letters.
''')


