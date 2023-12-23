from lc import *

# Q1. biweekly-contest-120

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def increasing(v):
            return len(v)==0 or all(a<b for a,b in pairwise(v))
        n = len(nums)
        r = 0
        for i in range(n):
            for j in range(i,n):
                if increasing(nums[:i] + nums[j+1:]):
                    r += 1
        return r

# jwseph

class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        def inc(arr):
            return all(arr[i-1] < arr[i] for i in range(1, len(arr)))
        return sum(inc(nums[:i]+nums[j:]) for i in range(len(nums)+1) for j in range(i+1, len(nums)+1))

class Solution:
    def incremovableSubarrayCount(self, n: List[int]) -> int:
        return sum(all(a<b for a,b in pairwise(n[:i]+n[j+1:]))for i in range(len(n))for j in range(i,len(n)))

test('''
100171. Count the Number of Incremovable Subarrays I
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Easy
You are given a 0-indexed array of positive integers nums.

A subarray of nums is called incremovable if nums becomes strictly increasing on removing the subarray. For example, the subarray [3, 4] is an incremovable subarray of [5, 3, 4, 6, 7] because removing this subarray changes the array [5, 3, 4, 6, 7] to [5, 6, 7] which is strictly increasing.

Return the total number of incremovable subarrays of nums.

Note that an empty array is considered strictly increasing.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 10
Explanation: The 10 incremovable subarrays are: [1], [2], [3], [4], [1,2], [2,3], [3,4], [1,2,3], [2,3,4], and [1,2,3,4], because on removing any one of these subarrays nums becomes strictly increasing. Note that you cannot select an empty subarray.
Example 2:

Input: nums = [6,5,7,8]
Output: 7
Explanation: The 7 incremovable subarrays are: [5], [6], [5,7], [6,5], [5,7,8], [6,5,7] and [6,5,7,8].
It can be shown that there are only 7 incremovable subarrays in nums.
Example 3:

Input: nums = [8,7,6,6]
Output: 3
Explanation: The 3 incremovable subarrays are: [8,7,6], [7,6,6], and [8,7,6,6]. Note that [8,7] is not an incremovable subarray because after removing [8,7] nums becomes [6,6], which is sorted in ascending order but not strictly increasing.
 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
''')

