from Leetcode import *

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(nums):
            if target - x in seen:
                return seen [target - x], i
            seen[x] = i
        return False

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return (f:=lambda i,seen:False if i==len(nums) else (seen[target-nums[i]], i) if target-nums[i] in seen else seen.__setitem__(nums[i], i) or f(i+1, seen))(0,{})

test(Solution, '''
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 10**4
-10**9 <= nums[i] <= 10**9
-10**9 <= target <= 10**9
Only one valid answer exists.
''')

