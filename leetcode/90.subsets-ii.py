from lc import *

# https://leetcode.com/problems/subsets-ii/discuss/30137/Simple-iterative-solution

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[[]]
        for i in range(len(nums)):
            if(i==0 or nums[i]!=nums[i-1]):
                l=len(res)
                for t in range(len(res)):
                    res.append(res[t]+[nums[i]])
            else:
                p=len(res)
                for t in range(l,len(res)):
                    res.append(res[t]+[nums[i]])
                l=p
        return res

test()

# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, a: List[int]) -> List[List[int]]:
        a.sort();
        return[*{*chain.from_iterable(combinations(a,r)for r in range(len(a)+1))}]

test('''
90. Subsets II
Medium

9855

327

Add to List

Share
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
Accepted
1,011,797
Submissions
1,743,821
''', sort=True)
