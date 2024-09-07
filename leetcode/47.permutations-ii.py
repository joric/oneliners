from lc import *

# https://leetcode.com/problems/permutations-ii/

class Solution:
    def permuteUnique(self, n: List[int]) -> List[List[int]]:
        return{*permutations(n)}

test('''
47. Permutations II
Medium

8567

146

Add to List

Share
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
Accepted
979,357
Submissions
1,633,286
''', sort=True)
