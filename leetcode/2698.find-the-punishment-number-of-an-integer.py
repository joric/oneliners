from lc import *

# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/solutions/6423721/one-line-o-1-0ms-for-fun/?envType=daily-question&envId=2025-02-15

class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum(i*i for i in[0,1,9,10,36,45,55,82,91,99,100,235,297,369,370,379,414,657,675,703,756,792,909,918,945,964,990,991,999,1000]if i<=n)

# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/?envType=daily-question&envId=2025-02-15

class Solution:
    def punishmentNumber(self, n: int) -> int:
        f=lambda x,t:0<=t<=x and(x==t or any(f(x//10**p,t-x%10**p)for p in(1,2,3)));return sum(x*x for x in range(1,n+1)if f(x*x,x))

test('''
2698. Find the Punishment Number of an Integer
Medium
Topics
Companies
Hint
Given a positive integer n, return the punishment number of n.

The punishment number of n is defined as the sum of the squares of all integers i such that:

1 <= i <= n
The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
 

Example 1:

Input: n = 10
Output: 182
Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
Hence, the punishment number of 10 is 1 + 81 + 100 = 182
Example 2:

Input: n = 37
Output: 1478
Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
- 1 since 1 * 1 = 1. 
- 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
- 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
- 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478
 

Constraints:

1 <= n <= 1000
Seen this question in a real interview before?
1/5
Yes
No
Accepted
48.2K
Submissions
64.6K
Acceptance Rate
74.7%
Topics
Math
Backtracking
Companies
Hint 1
Can we generate all possible partitions of a number?
Hint 2
Use a recursive algorithm that splits the number into two parts, generates all possible partitions of each part recursively, and then combines them in all possible ways.
Similar Questions
Number of Great Partitions
Hard
''')
