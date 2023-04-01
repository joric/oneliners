from lc import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r  = len(nums)-1
        while l<=r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return i if (i:=bisect_left(nums,target))<len(nums) and nums[i]==target else -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return i if nums[i:=bisect_right(nums,target)-1]==target else -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return (target in nums and nums.index(target)+1)-1

test('''
704. Binary Search
Easy

8514

183

Add to List

Share
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Example 3:

Input: nums = [-1,0,3,5,9,12], target = 13
Output: -1

Constraints:

1 <= nums.length <= 10^4
-10^4 < nums[i], target < 10^4
All the integers in nums are unique.
nums is sorted in ascending order.

Accepted
1,642,924
Submissions
2,958,532
''')

