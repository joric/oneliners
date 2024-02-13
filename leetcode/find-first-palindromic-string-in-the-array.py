from lc import *

# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/discuss/1737267/Python-One-Line-90-faster

class Solution:
    def firstPalindrome(self, w: List[str]) -> str:
        return next(filter(lambda s:s==s[::-1],w),'')

class Solution:
    def firstPalindrome(self, w: List[str]) -> str:
        return next((s for s in w if s==s[::-1]),'')

test('''
2108. Find First Palindromic String in the Array
Easy

993

33

Add to List

Share
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

 

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists only of lowercase English letters.
Accepted
115,891
Submissions
146,373
''')

