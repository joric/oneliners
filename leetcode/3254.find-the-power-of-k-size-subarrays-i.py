from lc import *

# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/discuss/6049277/Recursion-One-Line-Method
# const resultsArray = f = (nums, k) => k === 1 ? nums : f(nums.map((v, i, a) => v === a[i-1] + 1 ? v : -1).slice(1), k - 1);

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        return k>1 and self.resultsArray([v if v == nums[i - 1] + 1 else -1 for i, v in enumerate(nums)][1:],k-1)or nums

class Solution:
    def resultsArray(self, a: List[int], k: int) -> List[int]:
        return(f:=lambda a,k:k>1 and f([(-1,x)[x==a[i-1]+1]for i,x in enumerate(a)][1:],k-1)or a)(a,k)

class Solution:
    def resultsArray(self, a: List[int], k: int) -> List[int]:
        return k>1 and self.resultsArray([(-1,x)[x==a[i-1]+1]for i,x in enumerate(a)][1:],k-1)or a

test('''
3254. Find the Power of K-Size Subarrays I
Medium

88

11

Add to List

Share
You are given an array of integers nums of length n and a positive integer k.

The power of an array is defined as:

Its maximum element if all of its elements are consecutive and sorted in ascending order.
-1 otherwise.
You need to find the power of all subarrays of nums of size k.

Return an integer array results of size n - k + 1, where results[i] is the power of nums[i..(i + k - 1)].

 

Example 1:

Input: nums = [1,2,3,4,3,2,5], k = 3

Output: [3,4,-1,-1,-1]

Explanation:

There are 5 subarrays of nums of size 3:

[1, 2, 3] with the maximum element 3.
[2, 3, 4] with the maximum element 4.
[3, 4, 3] whose elements are not consecutive.
[4, 3, 2] whose elements are not sorted.
[3, 2, 5] whose elements are not consecutive.
Example 2:

Input: nums = [2,2,2,2,2], k = 4

Output: [-1,-1]

Example 3:

Input: nums = [3,2,3,2,3,2], k = 2

Output: [-1,3,-1,3,-1]

 

Constraints:

1 <= n == nums.length <= 500
1 <= nums[i] <= 105
1 <= k <= n
Accepted
41,595
Submissions
76,446
''')
