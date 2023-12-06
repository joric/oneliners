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

# https://leetcode.com/problems/calculate-money-in-leetcode-bank/discuss/4368090/One-Liner-Python-Math

class Solution:
    def totalMoney(self, n: int) -> int:
        return sum(range(1,8)) * (n//7) + 7*sum(range(0,n//7)) + sum(range(1,n%7+1)) + (n%7) * (n//7)

# https://leetcode.com/problems/calculate-money-in-leetcode-bank/discuss/1009192/C%2B%2B-O(1)-Math

class Solution:
    def totalMoney(self, n: int) -> int:
        f,l=n//7,n%7;return(7*f*(7+f)+l*(2*f+l+1))//2

# https://leetcode.com/problems/calculate-money-in-leetcode-bank/discuss/1010596/Python-One-Line-Simple

class Solution:
    def totalMoney(self, n: int) -> int:
        return n+sum(sum(divmod(i,7))for i in range(n))

class Solution:
    def totalMoney(self, n: int) -> int:
        return sum(i//7+i%7+1for i in range(n))

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
