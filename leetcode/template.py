from Leetcode import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(nums):
            if target - x in seen:
                return seen [target - x], i
            seen[x] = i
        return False

test(Solution, '''

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

''')
