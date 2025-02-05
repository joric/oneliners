from lc import *

# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/solutions/1108295/python3-check-diff/?envType=daily-question&envId=2025-02-05

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]

# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/solutions/1598053/easy-python-solution/?envType=daily-question&envId=2025-02-05

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c=0
        for i,j in zip(s1,s2):
            if i!=j:
                c+=1
        return s1==s2 or sorted(s1)==sorted(s2) and c==2

class Solution:
    def areAlmostEqual(self, a: str, b: str) -> bool:
        return sorted(a)==sorted(b)and sum(x!=y for x,y in zip(a,b))<3

class Solution:
    def areAlmostEqual(self, a: str, b: str) -> bool:
        return eq(*map(sorted,(a,b)))and sum(map(ne,a,b))<3

class Solution:
    def areAlmostEqual(self, a: str, b: str) -> bool:
        return sorted(a)==sorted(b)and sum(map(ne,a,b))<3

class Solution:
    def areAlmostEqual(self, a: str, b: str) -> bool:
        s=sorted;return s(a)==s(b)and sum(map(ne,a,b))<3

class Solution:
    def areAlmostEqual(self, a: str, b: str) -> bool:
        return(s:=sorted)(a)==s(b)and sum(map(ne,a,b))<3

test('''
1790. Check if One String Swap Can Make Strings Equal
Easy
Topics
Companies
Hint
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Other examples:

Input: s1 = "abca", s2 = "abcc"
Output: false

Input: s1 = "bankb", s2 = "kannb"
Output: false


Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
122.6K
Submissions
266.1K
Acceptance Rate
46.1%
Topics
Hash Table
String
Counting
Companies
Hint 1
The answer is false if the number of nonequal positions in the strings is not equal to 0 or 2.
Hint 2
Check that these positions have the same set of characters.
Similar Questions
Buddy Strings
Easy
Make Number of Distinct Characters Equal
Medium
Count Almost Equal Pairs I
Medium
''')
