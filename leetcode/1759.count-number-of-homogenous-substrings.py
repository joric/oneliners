from lc import *

# https://leetcode.com/problems/count-number-of-homogenous-substrings/discuss/1064530/JavaC%2B%2BPython-Straight-Forward

class Solution:
    def countHomogenous(self, s: str) -> int:
        return sum(comb(len([*g])+1,2)for _,g in groupby(s))%(10**9+7)

test('''
1759. Count Number of Homogenous Substrings
Medium

739

46

Add to List

Share
Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
Example 2:

Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
Example 3:

Input: s = "zzzzz"
Output: 15
 

Constraints:

1 <= s.length <= 10^5
s consists of lowercase letters.
Accepted
35,647
Submissions
68,199
''')
