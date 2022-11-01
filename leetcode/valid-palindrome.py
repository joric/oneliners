from lc import *

class Solution1:
    def isPalindrome(self, s: str) -> bool:
        return (s:=''.join(filter(str.isalnum,s)).lower())==s[::-1]

# OOM
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        return (f:=lambda s:not s or (s[0]==s[-1] and f(s[1:-1])))(''.join(filter(str.isalnum,s)).lower())

class Solution3:
    def isPalindrome(self, s: str) -> bool:
        return (f:=lambda s,i,j:i>=j or (s[i]==s[j] and f(s,i+1,j-1)))(s:=''.join(filter(str.isalnum,s)).lower(),0,len(s)-1)

# TLE
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return (f:=lambda s,i,j:i>=j or (not s[i].isalnum() and f(s,i+1,j)) or (not s[j].isalnum() and f(s,i,j-1)) or (s[i].lower()==s[j].lower() and f(s,i+1,j-1)))(s,0,len(s)-1)

test('''

125. Valid Palindrome
Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Custom examples:

Input: s="aa"
Output: true

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

''')
