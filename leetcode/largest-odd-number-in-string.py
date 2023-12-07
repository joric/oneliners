from lc import *

# https://leetcode.com/problems/largest-odd-number-in-string/discuss/1288404/Python-3-one-line

class Solution:
    def largestOddNumber(self, n: str) -> str:
        return re.sub('(^|[13579])[24680]*$',r'\1',n)

# https://leetcode.com/problems/largest-odd-number-in-string/discuss/2669269/Python-one-line-code-largest-odd-number-in-string

class Solution:
    def largestOddNumber(self, n: str) -> str:
        return n.rstrip('02468')

test('''
1903. Largest Odd Number in String
Easy

1262

78

Add to List

Share
You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
 

Constraints:

1 <= num.length <= 10^5
num only consists of digits and does not contain any leading zeros.
Accepted
99,281
Submissions
170,904
''')

