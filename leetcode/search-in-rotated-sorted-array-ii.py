from lc import *

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if(not nums):
            return False 
        l, r = 0, len(nums) - 1
        while(l < r):
            mid = (l + r) >> 1
            left, middle, right = nums[l], nums[mid], nums[r]
            if(middle == target):
                return True
            if(middle > right):
                if(left <= target < middle):
                    r = mid
                else:
                    l = mid + 1
            elif(middle < right):
                if(middle < target <= right):
                    l = mid + 1
                else:
                    r = mid
            else:
                r -= 1
        return nums[l] == target

class Solution:
    def search(self, n: List[int], t: int) -> int:
        return t in n

test('''
81. Search in Rotated Sorted Array II
Medium

6699

867

Add to List

Share
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

 

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
 

Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
''')

