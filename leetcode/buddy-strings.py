from lc import *

class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
            if len(a)!=len(b):
                return False
            if a==b and len(set(a))<len(a):
                return True
            d=[(x,y)for x,y in zip(a,b)if x!=y]
            return len(d)==2 and d[0]==d[1][::-1]

# https://leetcode.com/problems/buddy-strings/discuss/183639/python-1-liner

class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        return sum(x!=y for x,y in zip(a,b))<=2 and Counter(a)==Counter(b) if a!=b else len(set(a))<len(a)

class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        return sum(x!=y for x,y in zip(a,b))<=2 and sorted(a)==sorted(b)if a!=b else len(set(a))<len(a)

test('''
859. Buddy Strings
Easy

1862

1165

Add to List

Share
Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
 

Example 1:

Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
Example 2:

Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
Example 3:

Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.

Example 4:

Input: s = "abcaa", goal = "abcbb"
Output: false

Constraints:

1 <= s.length, goal.length <= 2 * 10^4
s and goal consist of lowercase letters.
''')

