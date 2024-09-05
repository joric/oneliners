from lc import *

# https://leetcode.com/problems/house-robber/solutions/2910723/c-python-one-liner-dp

class Solution:
    def rob(self, nums: List[int], a = 0, b = 0, i=0) -> int:  
        return b if i==len(nums)else self.rob(nums,b,max(a+nums[i],b),i+1)

class Solution:
    def rob(self, n: List[int]) -> int:
        return(f:=lambda a,b,i:i<len(n)and f(b,max(a+n[i],b),i+1)or b)(0,0,0)

class Solution:
    def rob(self, nums: List[int], a = 0, b = 0, i=0) -> int:  
        return nums[i:]and self.rob(nums,b,max(a+nums[i],b),i+1)or b

# https://leetcode.com/problems/house-robber/solutions/3229996/simplest-one-liner-python-dp

class Solution:
    def rob(self, n: List[int]) -> int:
        return(f:=cache(lambda i:i<len(n)and max(f(i+2)+n[i],f(i+1))))(0)

# https://leetcode.com/problems/house-robber/solutions/4510083/easy-dp-solution

class Solution:
    def rob(self, n: List[int]) -> int:
        a,b = 0,0
        for i in n:
            a,b = b,max(i+a,b)
        return b

class Solution:
    def rob(self, n: List[int]) -> int:
        return reduce(lambda x,y:(x[1],max(x[0]+y,x[1])),n,(0,0))[1]

class Solution:
    def rob(self, n: List[int]) -> int:
        a=b=0;[b:=max(x+a,a:=b)for x in n];return b

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
