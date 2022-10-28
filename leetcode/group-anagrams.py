from Leetcode import *

def check(res, expected, strs):
    u = lambda v: sorted(list(map(sorted,v)))
    return u(res)==u(expected)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return [list(v) for k,v in groupby(sorted(strs,key=sorted),sorted)]

test(Solution,'''
49. Group Anagrams
Medium

12232

377

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 10^4
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
''',check=check)
