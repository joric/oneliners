from lc import *

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, target, path, ret):
            if target < 0: return 
            if target == 0:
                ret.append(path)
                return 
            for i in range(len(nums)):
                dfs(nums[i:], target-nums[i], path+[nums[i]], ret)
        ret = []
        dfs(candidates, target, [], ret)
        return ret

# https://leetcode.com/problems/combination-sum/discuss/458821/One-line-in-Python

class Solution:
    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:
        return[[x]+s for x in c for s in self.combinationSum(c,t-x)if x<=(s[0]if s else t)]if t>0else[[]]

test('''
39. Combination Sum
Medium

17736

362

Add to List

Share
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
 

Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
''')

