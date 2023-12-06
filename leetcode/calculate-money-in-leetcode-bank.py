from lc import *

class Solution:
    def totalMoney(self, n: int) -> int:
        m = 1
        res = 0
        prev = 0
        for i in range(n):
            if i%7==0:
                x = m
                m += 1
            else:
                x = prev+1
            res += x
            prev = x
        return res

class Solution:
    def totalMoney(self, n: int) -> int:
        f,l=n//7,n%7;return(7*f*(7+f)+l*(2*f+l+1))//2

test('''
1716. Calculate Money in Leetcode Bank
Easy

753

23

Add to List

Share
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
 

Constraints:

1 <= n <= 1000
Accepted
58,562
Submissions
82,928
''')
