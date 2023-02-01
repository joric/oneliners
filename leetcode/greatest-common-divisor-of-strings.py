from lc import *

class Solution:
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        return s1[:gcd(len(s1),len(s2))] if s1+s2==s2+s1 else ''

test('''

1071. Greatest Common Divisor of Strings
Easy

1718

333

Add to List

Share
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

''')
