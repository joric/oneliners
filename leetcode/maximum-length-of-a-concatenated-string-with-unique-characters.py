from lc import *

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for a in arr:
            if len(set(a)) < len(a):
                continue
            a = set(a)
            for c in dp[:]:
                if a & c: continue
                dp.append(a | c)
        return max(len(a) for a in dp)

# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/discuss/1479802/Python-3-one-line

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        p = {''}
        for s in arr:
            if len(set(s)) == len(s):
                p |= {s + x for x in p if not (set(s) & set(y))}
        return max(map(len, p))

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return max(map(len,reduce(lambda p,s:p|{s+x for x in p if not (set(s)&set(x))},filter(lambda s:len(set(s))==len(s),arr),{''})))

test('''
1239. Maximum Length of a Concatenated String with Unique Characters
Medium

You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
''')
