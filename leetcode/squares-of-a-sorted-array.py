from lc import *

# https://leetcode.com/problems/squares-of-a-sorted-array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = deque([])
        l, r = 0, len(nums)-1
        while r >= l:
            if abs(nums[l]) > abs(nums[r]):
                res.appendleft(nums[l]**2)
                l += 1
            else:
                res.appendleft(nums[r]**2)
                r -= 1
        return res

class Solution:
    def sortedSquares(self, n: List[int]) -> List[int]:
        return sorted(map(pow,n,[2]*len(n)))

class Solution:
    def sortedSquares(self, n: List[int]) -> List[int]:
        return sorted(x*x for x in n)

test('''
977. Squares of a Sorted Array
Easy

8848

221

Add to List

Share
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
Accepted
1,665,254
Submissions
2,309,859
''')
