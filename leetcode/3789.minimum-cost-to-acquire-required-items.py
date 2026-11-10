from lc import *

# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/solutions/7449335/python-one-line-by-ante-j2x1/?envType=daily-question&envId=2026-11-11

class Solution:
    def minimumCost(self, c1, c2, b, n1, n2):
        return  (lambda n, n1, n2: min(n * b, c1 * n + c2 * n) + n1 * min(c1, b) + n2 * min(b, c2))(min(n1, n2), n1 - min(n1, n2), n2 - min(n1, n2))

class Solution:
    def minimumCost(self, a: int, b: int, c: int, d: int, e: int) -> int:
        return min(c,a+b)*min(d,e)+abs(d-e)*min([a,b][d<e],c)

test('''
3789. Minimum Cost to Acquire Required Items
Medium
Topics
premium lock icon
Companies
Hint
You are given five integers cost1, cost2, costBoth, need1, and need2.

There are three types of items available:

An item of type 1 costs cost1 and contributes 1 unit to the type 1 requirement only.
An item of type 2 costs cost2 and contributes 1 unit to the type 2 requirement only.
An item of type 3 costs costBoth and contributes 1 unit to both type 1 and type 2 requirements.
You must collect enough items so that the total contribution toward type 1 is at least need1 and the total contribution toward type 2 is at least need2.

Return an integer representing the minimum possible total cost to achieve these requirements.

 

Example 1:

Input: cost1 = 3, cost2 = 2, costBoth = 1, need1 = 3, need2 = 2

Output: 3

Explanation:

After buying three type 3 items, which cost 3 * 1 = 3, the total contribution to type 1 is 3 (>= need1 = 3) and to type 2 is 3 (>= need2 = 2).
Any other valid combination would cost more, so the minimum total cost is 3.

Example 2:

Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 2, need2 = 3

Output: 22

Explanation:

We buy need1 = 2 items of type 1 and need2 = 3 items of type 2: 2 * 5 + 3 * 4 = 10 + 12 = 22.
Any other valid combination would cost more, so the minimum total cost is 22.

Example 3:

Input: cost1 = 5, cost2 = 4, costBoth = 15, need1 = 0, need2 = 0

Output: 0

Explanation:

Since no items are required (need1 = need2 = 0), we buy nothing and pay 0.

 

Constraints:

1 <= cost1, cost2, costBoth <= 106
0 <= need1, need2 <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
25,660/73.2K
Acceptance Rate
35.1%
Topics
Staff
Math
Greedy
Weekly Contest 482
icon
Companies
Hint 1
First, use min(costBoth, cost1 + cost2) for min(need1, need2).
Hint 2
For the remaining type 1 requirement rem1, use cost min(costBoth, cost1) for the rest.
Hint 3
Do the same for type 2, using cost min(costBoth, cost2).
''')
