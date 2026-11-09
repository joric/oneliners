from lc import *

# https://leetcode.com/problems/climbing-stairs-ii/solutions/7348384/one-line-rust-by-sometimesnever-yf0v/?envType=daily-question&envId=2026-11-10

class Solution:
    def climbStairs(self, n: int, c: List[int]) -> int:
        return reduce(lambda s,x:(s[1]+5,s[2]+3,min(s)+x+1),c,(8,3,0))[2]

class Solution:
    def climbStairs(self, n: int, c: List[int]) -> int:
        s=8,3,0;[s:=(s[1]+5,s[2]+3,min(s)+x+1)for x in c];return s[2]

test('''
3693. Climbing Stairs II
Medium
Topics
premium lock icon
Companies
Hint
You are climbing a staircase with n + 1 steps, numbered from 0 to n.

You are also given a 1-indexed integer array costs of length n, where costs[i] is the cost of step i.

From step i, you can jump only to step i + 1, i + 2, or i + 3. The cost of jumping from step i to step j is defined as: costs[j] + (j - i)2

You start from step 0 with cost = 0.

Return the minimum total cost to reach step n.

 

Example 1:

Input: n = 4, costs = [1,2,3,4]

Output: 13

Explanation:

One optimal path is 0 → 1 → 2 → 4

Jump    Cost Calculation    Cost
0 → 1   costs[1] + (1 - 0)2 = 1 + 1 2
1 → 2   costs[2] + (2 - 1)2 = 2 + 1 3
2 → 4   costs[4] + (4 - 2)2 = 4 + 4 8
Thus, the minimum total cost is 2 + 3 + 8 = 13

Example 2:

Input: n = 4, costs = [5,1,6,2]

Output: 11

Explanation:

One optimal path is 0 → 2 → 4

Jump    Cost Calculation    Cost
0 → 2   costs[2] + (2 - 0)2 = 1 + 4 5
2 → 4   costs[4] + (4 - 2)2 = 2 + 4 6
Thus, the minimum total cost is 5 + 6 = 11

Example 3:

Input: n = 3, costs = [9,8,3]

Output: 12

Explanation:

The optimal path is 0 → 3 with total cost = costs[3] + (3 - 0)2 = 3 + 9 = 12

 

Constraints:

1 <= n == costs.length <= 105​​​​​​​
1 <= costs[i] <= 104
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
40,303/62.9K
Acceptance Rate
64.1%
Topics
Senior
Array
Dynamic Programming
Biweekly Contest 166
icon
Companies
Hint 1
Use dynamic programming where dp[j] represents the minimum cost to reach step j.
Hint 2
From step i, you can jump to i+1, i+2, or i+3. Transition depends only on the previous three states.
Hint 3
dp[j] = min(dp[i] + costs[j] + (j - i)2) for all i in {j-1, j-2, j-3}.
Hint 4
Initialize dp[0] = 0 and compute up to dp[n]; the answer is dp[n].
''')
