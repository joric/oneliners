from Leetcode import *

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start, res, h = 0, 0, {}
        for i, c in enumerate(s):
            start = max(start, h.get(c,0))
            res = max(res, i - start + 1)
            h[c] = i + 1
        return res

def fn(a,b):
    start, res, h = a
    i, c = b
    start = max(start, h.get(c,0))
    res = max(res, i - start + 1)
    h[c] = i + 1
    return start,res,h

class Solution1:
    def lengthOfLongestSubstring(self, s):
        return reduce(fn,enumerate(s),[0,0,{}])[1]

class Solution0:
    def lengthOfLongestSubstring(self, s):
        return reduce(lambda a,b:(s:=max(a[0],a[2].get(b[1],0)),max(a[1],b[0]-s+1),\
            {**a[2],b[1]:b[0]+1}),enumerate(s),(0,0,{}))[1]


test(Solution,'''
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
''')
