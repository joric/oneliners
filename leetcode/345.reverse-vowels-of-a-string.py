from lc import *

# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:
        return (t:='aeiouAEIOU',v:=[c for c in s if c in t]) and ''.join([v.pop() if c in t else c for c in s])

class Solution:
    def reverseVowels(self, s: str) -> str:
        return re.sub(t:='(?i)[aeiou]',lambda m,v=re.findall(t,s):v.pop(),s)

test('''

345. Reverse Vowels of a String
Easy

2019

2034

Add to List

Share
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

Example 3:

Input: s = "aA"
Output: "Aa"

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

''')