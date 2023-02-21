from lc import *

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r:
            m = (l + r)//2
            if nums[m]==nums[m^1]:
                l = m + 1
            else:
                r = m
        return nums[l]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return next((nums[l] for _ in count() if not (l<r and (m:=(l+r)//2,nums[m]==nums[m^1] and (l:=m+1) or (r:=m)))),(l:=0,r:=len(nums)-1))

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        class Wrap():
            def __getitem__(self, i):
                return nums[i*2] != nums[i*2+1]
        return nums[bisect_left(Wrap(), True, 0, len(nums) // 2) * 2]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return nums[bisect_left(type('',(),{'__getitem__':lambda _,i:nums[i*2]!=nums[i*2+1]})(),1,0,len(nums)//2)*2]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return nums[bisect_left(range(len(nums)//2),0,key=lambda i:(1,-1)[nums[i*2]==nums[i*2+1]])*2]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return nums[bisect_left(range(len(nums)-1),0,key=lambda i:(1,-1)[nums[i]==nums[i^1]])]

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return sum(set(nums))*2-sum(nums)

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(xor, nums)

test('''

540. Single Element in a Sorted Array
Medium

7060

116

Add to List

Share
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Example 3:

Input: nums = [1]
Output: 1

Example 4:
Input: nums = [1,1,2]
Output: 2

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5

''')