from lc import *

# Doug Mcelroy, programming pearls, page 33

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse(a):
            i,j = 0, len(a)-1
            while i < j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
            return a
        k = k % len(nums)
        nums = reverse(nums)
        nums[:k] = reverse(nums[:k])
        nums[k:] = reverse(nums[k:])

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
        nums.reverse()
        nums[:k]=(a:=nums[:k]).reverse() or a
        nums[k:]=(b:=nums[k:]).reverse() or b

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums[:]= nums[len(nums)-k:]+nums[:len(nums)-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        [nums.insert(0,nums.pop()) for i in range(k)]

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


