from lc import *

# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/solutions/4487292/rustpython-can-be-one-line-but-why-overc-ycej/?envType=daily-question&envId=2026-03-29

class Solution:
  def canBeEqual(self, s1: str, s2: str) -> bool:
    f = lambda i, j : (s1[i] == s2[i] and s1[j] == s2[j]) or (s1[i] == s2[j] and s1[j] == s2[i])
    return f(0, 2) and f(1, 3)

# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/solutions/3994710/1-line-python-by-true-detective-4s1z/?envType=daily-question&envId=2026-03-29

class Solution:
    def canBeEqual(self, s: str, t: str) -> bool:
        return sorted(s[::2]) == sorted(t[::2]) and sorted(s[1::2]) == sorted(t[1::2])

class Solution:
    def canBeEqual(self, s: str, t: str) -> bool:
        return all(map(eq,*([{*x[i::2]}for i in(0,1)]for x in(s,t))))

class Solution:
    def canBeEqual(self, s: str, t: str) -> bool:
        return{*s[::2]}=={*t[::2]}and{*s[1::2]}=={*t[1::2]}

class Solution:
    def canBeEqual(self, a: str, b: str) -> bool:
        return all({*a[i::2]}=={*b[i::2]}for i in(0,1))

test('''
2839. Check if Strings Can be Made Equal With Operations I
Easy
Topics
premium lock icon
Companies
Hint
You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

 

Example 1:

Input: s1 = "abcd", s2 = "cdab"
Output: true
Explanation: We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
- Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.
Example 2:

Input: s1 = "abcd", s2 = "dacb"
Output: false
Explanation: It is not possible to make the two strings equal.
 

Constraints:

s1.length == s2.length == 4
s1 and s2 consist only of lowercase English letters.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
45,084/94.2K
Acceptance Rate
47.8%
Topics
Mid Level
String
Biweekly Contest 112
icon
Companies
Hint 1
Since the strings are very small you can try a brute-force approach.
Hint 2
There are only 2 different swaps that are possible in a string.
''')
