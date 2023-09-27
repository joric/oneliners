from lc import *

# https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/discuss/2752706/Python-one-line-without-coun

class Solution:
    def digitCount(self, num: str) -> bool:
        return num in {'1210','21200','2020'} or num == str(len(num)-4) + '21' + '0' * (len(num)-7) + '1000'

class Solution:
    def digitCount(self, n: str) -> bool:
        return all(int(n[i])==n.count(str(i))for i in range(len(n)))

test('''
2283. Check if Number Has Equal Digit Count and Digit Value
Easy

525

62

Add to List

Share
You are given a 0-indexed string num of length n consisting of digits.

Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

 

Example 1:

Input: num = "1210"
Output: true
Explanation:
num[0] = '1'. The digit 0 occurs once in num.
num[1] = '2'. The digit 1 occurs twice in num.
num[2] = '1'. The digit 2 occurs once in num.
num[3] = '0'. The digit 3 occurs zero times in num.
The condition holds true for every index in "1210", so return true.
Example 2:

Input: num = "030"
Output: false
Explanation:
num[0] = '0'. The digit 0 should occur zero times, but actually occurs twice in num.
num[1] = '3'. The digit 1 should occur three times, but actually occurs zero times in num.
num[2] = '0'. The digit 2 occurs zero times in num.
The indices 0 and 1 both violate the condition, so return false.
 

Constraints:

n == num.length
1 <= n <= 10
num consists of digits.
Accepted
46,158
Submissions
63,537
''')

