from lc import *

# https://leetcode.com/problems/longest-ideal-subsequence/discuss/2390512/JavaC%2B%2BPython-DP-Solution

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        d = [0]*128
        for i in map(ord,s):
            d[i] = 1+max(d[i-k:i+k+1])
        return max(d)

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        d=[0]*128;return max(setitem(d,i,1+max(d[i-k:i+k+1]))or d[i]for i in map(ord,s))

test('''
2370. Longest Ideal Subsequence
Medium

965

37

Add to List

Share
You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:

t is a subsequence of the string s.
The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
Return the length of the longest ideal string.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.

 

Example 1:

Input: s = "acfgbd", k = 2
Output: 4
Explanation: The longest ideal string is "acbd". The length of this string is 4, so 4 is returned.
Note that "acfgbd" is not ideal because 'c' and 'f' have a difference of 3 in alphabet order.
Example 2:

Input: s = "abcd", k = 3
Output: 4
Explanation: The longest ideal string is "abcd". The length of this string is 4, so 4 is returned.
 

Constraints:

1 <= s.length <= 105
0 <= k <= 25
s consists of lowercase English letters.
Accepted
41,375
Submissions
98,260
''')