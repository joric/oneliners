from lc import *

# https://leetcode.com/problems/rotate-array/discuss/895412/Python-O(n)-inplace-solution-explained
# AKA Doug Mcelroy, programming pearls, page 33

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i+1, j-1
        n = len(nums)
        k = k % n
        reverse(0, n-1)
        reverse(0, k-1)
        reverse(k, n-1)
        return nums

# GCD solution, https://stackoverflow.com/questions/876293/fastest-algorithm-for-circle-shift-n-sized-array-for-m-position

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        shift = n - (k % n)
        for i in range(gcd(n, shift)):
            j = i
            while (k := (j + shift) % n) != i:
                nums[j],nums[k] = nums[k],nums[j]
                j = k

# misc

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:r] = nums[:k][::-1] 
        nums[r:] = nums[k:][::-1]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums.reverse()
        nums[:k]=(a:=nums[:k]).reverse() or a
        nums[k:]=(b:=nums[k:]).reverse() or b

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:] = nums[-(k-len(nums)):]+nums[:-(k-len(nums))]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:]=nums[-k%len(nums):]+nums[:-k%len(nums)]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        [nums.insert(0,nums.pop()) for _ in range(k)]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:]=(q:=deque(nums)).rotate(k) or q

test('''

189. Rotate Array
Medium

13448

1564

Add to List

Share
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Example 3:

Input: nums = [1,2], k = 5
Output: [2,1]

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?

Accepted
1,438,152
Submissions
3,653,081

''',check=lambda res, expected, arr,_: arr==expected
)


