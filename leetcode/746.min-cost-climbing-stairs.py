from lc import *

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0
        for c in cost:
            a, b = b, a
            b = c + min(a, b)
        return min(a, b)

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(reduce(lambda ab,c:(ab[1],c+min(ab)),cost,(0,0)))

class Solution:
    def minCostClimbingStairs(self, c: List[int]) -> int:
        return min(reduce(lambda a,c:(a[1],c+min(a)),c,(0,0)))

test('''
746. Min Cost Climbing Stairs
Easy

8207

1296

Add to List

Share
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
''')