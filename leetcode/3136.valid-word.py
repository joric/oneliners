from lc import *

# Q1. https://leetcode.com/contest/weekly-contest-396/
# https://leetcode.com/problems/valid-word/

class Solution:
    def isValid(self, w: str) -> bool:
        a,v=ascii_letters,{*'aeiou'};return w[2:]and not{*w}-{*a,*digits}and all(x&{*w.lower()}for x in(v,{*a.lower()}-v))

class Solution:
    def isValid(self, w: str) -> bool:
        v={*'aeiou'};return w[2:]and w.isalnum()and all(x&{*w.lower()}for x in(v,{*ascii_lowercase}-v))

# https://leetcode.com/problems/valid-word/discuss/5114540/Python-Solution-oror-Regexp.

class Solution:
    def isValid(self, word: str) -> bool:
        import re
        rule1 = len(word) >= 3
        rule2 = len(word) == len(re.findall(r'[a-zA-Z0-9]', word))
        rule3 = len(re.findall(r'[aeiouAEIOU]', word))
        rule4 = len(re.findall(r'[A-Za-z]', word)) - rule3
        return rule1 and rule2 and rule3 and rule4

class Solution:
    def isValid(self, w: str) -> bool:
        return re.match('^(?=.*[aeiou])(?=.*[bcdfghjklmnpqrstvwxyz])[a-z0-9]{3,}$',w,re.I)

class Solution:
    def isValid(self, w: str) -> bool:
        return re.match('^(?=.*[aeiou])(?=.*[b-df-hj-np-tv-z])[a-z0-9]{3,}$',w,re.I)

class Solution:
    def isValid(self, w: str) -> bool:
        return match('^(?=.*[aeiou])(?=.*[^0-9aeiou])[a-z0-9]{3,}$',w,I)

# POTD 2025-07-15

class Solution:
    def isValid(self, s: str) -> bool:
        return bool(match('(?=.*[aeiou])(?=.*[^\daeiou])\w{3,}$',s,I))

test('''
3136. Valid Word
Easy

19

33

Add to List

Share
A word is considered valid if:

It contains a minimum of 3 characters.
It consists of the digits 0-9, and the uppercase and lowercase English letters. (Not necessary to have all of them.)
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
 

Example 1:

Input: word = "234Adas"

Output: true

Explanation:

This word satisfies the conditions.

Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.

Example 3:

Input: word = "a3$e"

Output: false

Explanation:

This word contains a '$' character and does not have a consonant.

Other examples:

Input: word = "AhI" 
Output: true

Constraints:

1 <= word.length <= 20
word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.
Accepted
19,691
Submissions
60,973
''')