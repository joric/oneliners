from lc import *

# https://leetcode.com/problems/lexicographically-smallest-string-after-a-swap/discuss/5473464/one-line-solution

class Solution:
    def getSmallestString(self, s: str) -> str:
        return min(chain([s],(s[:i]+s[i+1]+s[i]+s[i+2:] for i in range(len(s)-1) if int(s[i])&1==int(s[i+1])&1)))

test('''
3216. Lexicographically Smallest String After a Swap
Easy

5

5

Add to List

Share
Given a string s containing only digits, return the lexicographically smallest string that can be obtained after swapping adjacent digits in s with the same parity at most once.

Digits have the same parity if both are odd or both are even. For example, 5 and 9, as well as 2 and 4, have the same parity, while 6 and 9 do not.

 

Example 1:

Input: s = "45320"

Output: "43520"

Explanation:

s[1] == '5' and s[2] == '3' both have the same parity, and swapping them results in the lexicographically smallest string.

Example 2:

Input: s = "001"

Output: "001"

Explanation:

There is no need to perform a swap because s is already the lexicographically smallest.

 

Constraints:

2 <= s.length <= 100
s consists only of digits.
Accepted
23,586
Submissions
48,258
''')
