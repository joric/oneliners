from lc import *

# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/discuss/1676121/Python-simple-solution-andand-one-line

# ruby version is shorter: words.find{|i|i==i.reverse}||''

class Solution:
    def firstPalindrome(self, d: List[str]) -> str:
        return next(filter(lambda w:w==w[::-1],d),'')

class Solution:
    def firstPalindrome(self, d: List[str]) -> str:
        return next((w for w in d if w==w[::-1]),'')

class Solution:
    def firstPalindrome(self, d: List[str]) -> str:
        return[w for w in d+['']if w==w[::-1]][0]

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
