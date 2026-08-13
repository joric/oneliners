from lc import *

# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/?envType=daily-question&envId=2026-08-14

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        return max(j-i for i,j in combinations(range(len(s)+1),2)if max(map(s[i:j].count,s))<3)

test('''
3090. Maximum Length Substring With Two Occurrences
Easy
Topics
premium lock icon
Companies
Hint
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
68,703/104.2K
Acceptance Rate
65.9%
Topics
Mid Level
Hash Table
String
Sliding Window
Weekly Contest 390
icon
Companies
Hint 1
We can try all substrings by brute-force since the constraints are very small.
''')
