from lc import *

# https://leetcode.com/problems/find-all-duplicates-in-an-array

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for n in nums:
            i = abs(n) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]
            else:
                ans.append(i+1)
        return ans

class Solution:
    def findDuplicates(self, n: List[int]) -> List[int]:
        c=Counter;return c(n)-c({*n})

class Solution:
    def findDuplicates(self, n: List[int]) -> List[int]:
        return(c:=Counter)(n)-c({*n})

class Solution:
    def findDuplicates(self, n: List[int]) -> List[int]:
        return multimode([0,0]+n)[1:]

test('''
442. Find All Duplicates in an Array
Medium

9703

355

Add to List

Share
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]
Example 2:

Input: nums = [1,1,2]
Output: [1]
Example 3:

Input: nums = [1]
Output: []
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
Accepted
632,408
Submissions
853,638
''', check=lambda r,e,n:set(r)==set(e))
