from lc import *

# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/solutions/7300759/python-one-line-by-ante-9mnw/?envType=daily-question&envId=2026-10-14

class Solution:
    def maxSumOfSquares(self, n, s):
        return (lambda A: '' if len(A) > n else A)((lambda a: a + '0' * (n - len(a)))((lambda n9, r: '9' * n9 + (str(r)  if r else ''))(*divmod(s, 9))))

# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/solutions/7427885/beautiful-one-liner-not-really-by-gmjama-us4l/?envType=daily-question&envId=2026-10-14

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        return "9"*(sum // 9) + (str(sum%9) if sum%9!=0 else "") + ("0"*(num - len("9"*(sum // 9) + (str(sum%9) if sum%9!=0 else "")))) if num * 9 >= sum else ""

class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        return('9'*(s//9)+str(s%9)+'0'*n)[:n*(s<=9*n)]

class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        return(s//9*'9'+str(s%9)+'0'*n)[:n*(s<=9*n)]

test('''
3723. Maximize Sum of Squares of Digits
Medium
Topics
premium lock icon
Companies
Hint
You are given two positive integers num and sum.

A positive integer n is good if it satisfies both of the following:

The number of digits in n is exactly num.
The sum of digits in n is exactly sum.
The score of a good integer n is the sum of the squares of digits in n.

Return a string denoting the good integer n that achieves the maximum score. If there are multiple possible integers, return the maximum ​​​​​​​one. If no such integer exists, return an empty string.

 

Example 1:

Input: num = 2, sum = 3

Output: "30"

Explanation:

There are 3 good integers: 12, 21, and 30.

The score of 12 is 12 + 22 = 5.
The score of 21 is 22 + 12 = 5.
The score of 30 is 32 + 02 = 9.
The maximum score is 9, which is achieved by the good integer 30. Therefore, the answer is "30".

Example 2:

Input: num = 2, sum = 17

Output: "98"

Explanation:

There are 2 good integers: 89 and 98.

The score of 89 is 82 + 92 = 145.
The score of 98 is 92 + 82 = 145.
The maximum score is 145. The maximum good integer that achieves this score is 98. Therefore, the answer is "98".

Example 3:

Input: num = 1, sum = 10

Output: ""

Explanation:

There are no integers that have exactly 1 digit and whose digits sum to 10. Therefore, the answer is "".

 

Constraints:

1 <= num <= 2 * 105
1 <= sum <= 2 * 106
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
24,731/42.6K
Acceptance Rate
58.0%
Topics
Staff
Math
Greedy
Biweekly Contest 168
icon
Companies
Hint 1
Use a greedy approach.
Hint 2
Fill the leftmost digits with 9s first (as much as possible).
''')
