from lc import *

# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/solutions/3993607/python-3-1-line-counter-ts-100-65-by-spa-dnqw/

class Solution:
    def checkStrings(self, a: str, b: str) -> bool:
        c=Counter;return all(c(a[i::2])==c(b[i::2])for i in(0,1))

class Solution:
    def checkStrings(self, a: str, b: str) -> bool:
        c=sorted;return all(c(a[i::2])==c(b[i::2])for i in(0,1))

test('''
2840. Check if Strings Can be Made Equal With Operations II
Medium
Topics
premium lock icon
Companies
Hint
You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:

Choose any two indices i and j such that i < j and the difference j - i is even, then swap the two characters at those indices in the string.
Return true if you can make the strings s1 and s2 equal, and false otherwise.

 

Example 1:

Input: s1 = "abcdba", s2 = "cabdab"
Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = "cbadba".
- Choose the indices i = 2, j = 4. The resulting string is s1 = "cbbdaa".
- Choose the indices i = 1, j = 5. The resulting string is s1 = "cabdab" = s2.
Example 2:

Input: s1 = "abe", s2 = "bea"
Output: false
Explanation: It is not possible to make the two strings equal.
 

Constraints:

n == s1.length == s2.length
1 <= n <= 105
s1 and s2 consist only of lowercase English letters.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
31,447/55.9K
Acceptance Rate
56.2%
Topics
Senior
Hash Table
String
Sorting
Biweekly Contest 112
icon
Companies
Hint 1
Characters in two positions can be swapped if and only if the two positions have the same parity.
Hint 2
To be able to make the two strings equal, the characters at even and odd positions in the strings should be the same.
''')
