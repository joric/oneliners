from lc import *

# https://leetcode.com/problems/maximum-69-number

# did not need result cast before 11/07/2022

class Solution:
    def maximum69Number (self, n: int) -> int:
        return int(str(n).replace('6','9',1))

class Solution:
    def maximum69Number (self, n: int) -> int:
        return int(re.sub('6','9',str(n),1))

# POTD 2025-08-16

class Solution:
    def maximum69Number (self, n: int) -> int:
        return int(re.sub(*'69',str(n),1))

test('''
1323. Maximum 69 Number
Easy

1232

132

Add to List

Share
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
 

Constraints:

1 <= num <= 104
num consists of only 6 and 9 digits.
''')
