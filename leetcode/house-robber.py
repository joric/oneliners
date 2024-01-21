from lc import *

# https://leetcode.com/problems/house-robber/solutions/4510083/easy-dp-solution

class Solution:
    def rob(self, n: List[int]) -> int:
        a,b = 0,0
        for i in n:
            t = max(i+a,b)
            a = b
            b = t
        return b

class Solution:
    def rob(self, n: List[int]) -> int:
        return reduce(lambda x,y:[x[1],max(x[0]+y,x[1])],n,[0, 0])[1]

class Solution:
    def rob(self, n: List[int]) -> int:
        a,b=0,0;[b:=max(x+a,(a:=b))for x in n];return b

test('''

198. House Robber
Medium
15.5K
305
Companies
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

''')

