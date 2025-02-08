from lc import *

# https://leetcode.com/problems/combination-sum-iv/discuss/2795192/3-Line-Python

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i:
                    break
                if num == i:
                    combs[i] += 1
                if num  < i:
                    combs[i] += combs[i - num]
        return combs[target]

class Solution:
    def combinationSum4(self, n: List[int], t: int) -> int:
        return(f:=cache(lambda x:1 if not x else sum(f(x-y)if x-y>=0 else 0 for y in n)))(t)

class Solution:
    def combinationSum4(self, n: List[int], t: int) -> int:
        return(f:=cache(lambda x:sum(f(x-y)for y in n if x>=y)if x else 1))(t)

class Solution:
    def combinationSum4(self, n: List[int], t: int) -> int:
        return+(f:=cache(lambda x:sum(f(x-y)for y in n)if x>0else x==0))(t)

class Solution:
    def combinationSum4(self, n: List[int], t: int) -> int:
        return+(f:=cache(lambda x:x>0and sum(f(x-y)for y in n)or x==0))(t)

test('''
377. Combination Sum IV
Medium

6064

593

Add to List

Share
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
 

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
''')
