from lc import *

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        jumps = 1
        step = reach = nums[0]
        for i in range(1, len(nums)):
            if i > step:
                jumps += 1
                step = reach
            reach = max(reach, i + nums[i])
        return jumps

# https://leetcode.com/problems/jump-game-ii/discuss/2332653/Simple-1-line-solution

class Solution:
    def jump(self, nums: List[int]) -> int:
        j=c=f=0
        for i in range(len(nums)-1):
            f = max(f,nums[i]+i)
            if i==c:
                c=f
                j+=1
        return j

class Solution:
    def jump(self, nums: List[int]) -> int:
        return (j:=0,c:=0,f:=0,[(f:=max(f,x+i),i==c and (c:=f,j:=j+1)) for i,x in enumerate(nums[:-1])]) and j

test('''
45. Jump Game II
Medium

10780

376

Add to List

Share
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
 

Constraints:

1 <= nums.length <= 10^4
0 <= nums[i] <= 1000
''')
