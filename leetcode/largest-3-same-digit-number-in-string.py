from lc import *

# https://leetcode.com/problems/largest-3-same-digit-number-in-string/discuss/2760074/Easy-solution-using-groupby-(Python)

class Solution:
    def largestGoodInteger(self, n: str) -> str:
        return (s:=[int(k) for k,g in groupby(n)if len([*g])>2])and str(max(s))*3 or''

# https://leetcode.com/problems/largest-3-same-digit-number-in-string/discuss/2156885/1-line-simple-Python

class Solution:
    def largestGoodInteger(self, n: str) -> str:
        return next((s for s in ['999','888','777','666','555','444','333','222','111','000']if s in n),'')

class Solution:
    def largestGoodInteger(self, n: str) -> str:
        return next((s for s in[str(i)*3 for i in range(9,-1,-1)]if s in n),'')

class Solution:
    def largestGoodInteger(self, n: str) -> str:
        return next(filter(n.count,(str(i)*3 for i in range(9,-1,-1))),'')

test('''
2264. Largest 3-Same-Digit Number in String
Easy

362

19

Add to List

Share
You are given a string num representing a large integer. An integer is good if it meets the following conditions:

It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.

Note:

A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
 

Example 1:

Input: num = "6777133339"
Output: "777"
Explanation: There are two distinct good integers: "777" and "333".
"777" is the largest, so we return "777".
Example 2:

Input: num = "2300019"
Output: "000"
Explanation: "000" is the only good integer.
Example 3:

Input: num = "42352338"
Output: ""
Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

Example 4:
Input: num = "101010"
Output: ""
 

Constraints:

3 <= num.length <= 1000
num only consists of digits.
Accepted
38,232
Submissions
63,405
''')

