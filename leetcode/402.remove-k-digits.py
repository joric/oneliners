from lc import *

# https://leetcode.com/problems/remove-k-digits/discuss/88668/Short-Python-one-O(n)-and-one-RegEx

# TLE
class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        g = re.compile('1[0]|2[01]|3[0-2]|4[0-3]|5[0-4]|6[0-5]|7[0-6]|8[0-7]|9[0-8]|.$').sub
        for _ in range(k):
            s = g(lambda m: m.group()[1:], s, 1)
        return s.lstrip('0') or '0'

class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        q = []
        for c in s:
            while k and q and q[-1]>c:
                q.pop()
                k -= 1
            q.append(c)
        return ''.join(q[:-k or None]).lstrip('0')or'0'

class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        q=[];[all(k and q and q[-1]>c and(q.pop(),k:=k-1)for _ in s)or q.append(c)for c in s];return''.join(q[:-k or None]).lstrip('0')or'0'

class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        q=[];[all(k and[c]<q[-1:]and(q.pop(),k:=k-1)for _ in s)or q.append(c)for c in s];return''.join(q[:-k or None]).lstrip('0')or'0'

test('''
402. Remove K Digits
Medium

8560

390

Add to List

Share
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
 

Constraints:

1 <= k <= num.length <= 105
num consists of only digits.
num does not have any leading zeros except for the zero itself.
Accepted
365,171
Submissions
1,174,038
''')
