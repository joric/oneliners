from lc import *

# https://leetcode.com/problems/distribute-candies-among-children-ii/solutions/4284301/python3-1-line/?envType=daily-question&envId=2025-06-01

class Solution:
    def distributeCandies(self, n: int, l: int) -> int:
        return sum(max(0,min(n-x,2*l-n+x)+1)for x in range(l+1))

test('''
2929. Distribute Candies Among Children II
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given two positive integers n and limit.

Return the total number of ways to distribute n candies among 3 children such that no child gets more than limit candies.

 

Example 1:

Input: n = 5, limit = 2
Output: 3
Explanation: There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
Example 2:

Input: n = 3, limit = 3
Output: 10
Explanation: There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
 

Constraints:

1 <= n <= 106
1 <= limit <= 106
Seen this question in a real interview before?
1/5
Yes
No
Accepted
28,093/62K
Acceptance Rate
45.3%
Topics
Math
Combinatorics
Enumeration
icon
Companies
Hint 1
We can enumerate the number of candies of one particular child, let it be i which means 0 <= i <= min(limit, n).
Hint 2
Suppose the 2nd child gets j candies. Then 0 <= j <= limit and i + j <= n.
Hint 3
The 3rd child will hence get n - i - j candies and we should have 0 <= n - i - j <= limit.
Hint 4
After some transformations, for each i, we have max(0, n - i - limit) <= j <= min(limit, n - i), each j corresponding to a solution. So the number of solutions for some i is max(min(limit, n - i) - max(0, n - i - limit) + 1, 0). Sum the expression for every i in [0, min(n, limit)].
Similar Questions
Count Ways to Distribute Candies
Hard
''')
