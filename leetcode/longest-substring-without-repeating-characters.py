from lc import *

class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        start, res, h = 0, 0, {}
        for i, c in enumerate(s):
            start = max(start, h.get(c,0))
            res = max(res, i - start + 1)
            h[c] = i + 1
        return res

# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1006208/Python-oneliner

class Solution2:
    def lengthOfLongestSubstring(self, s):
        def fn(a,b):
            start, res, h = a
            i, c = b
            start = max(start, h.get(c,0))
            res = max(res, i - start + 1)
            h[c] = i + 1
            return start,res,h
        return reduce(fn,enumerate(s),[0,0,{}])[1]

class Solution3:
    def lengthOfLongestSubstring(self, s):
        return reduce(lambda a,b:(s:=max(a[0],a[2].get(b[1],0)),max(a[1],b[0]-s+1),{**a[2],b[1]:b[0]+1}),enumerate(s),(0,0,{}))[1]

class Solution31:
    def lengthOfLongestSubstring(self, s):
        return reduce(lambda a,b:(lambda t,r,h,i,c:(s:=max(t,h.get(c,0)),max(r,i-s+1),{**h,c:i+1}))(*a,*b),enumerate(s),(0,0,{}))[1]

# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/2021476/Python3-1-Line-Sliding-Window

class Solution4:
    def lengthOfLongestSubstring(self, s):
        d = {}
        i = -1
        res = 0
        for j,c in enumerate(s):
            k = d.pop(c,-1)
            d.setdefault(c,j)
            i = max(i, k)
            res = max(res, j-i)
        return res

class Solution5:
    def lengthOfLongestSubstring(self, s):
        return ((d:={}),(i:=-1)) and max(j-(i:=max(i,(d.pop(c,-1),d.setdefault(c,j))[0])) for j,c in enumerate(s)) if s else 0


# https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/372028/One-line-Scala-Solution%3A-faster-than-64-memory-less-than-100

class Solution:
    def lengthOfLongestSubstring(self, s):
        return max(map(len,accumulate(s,lambda x,y:x[y in x and 1+x.index(y):]+y,initial='')))


test('''
3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

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

Custom tests:

Input: s = "aab"
Output: 2

Input: s = " "
Output: 1

Input: s = ""
Output: 0

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.


''')
