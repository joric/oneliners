from lc import *

# https://leetcode.com/problems/minimum-positive-sum-subarray/solutions/6078024/python-solution-most-optimised-one-1-lin-rx6h/?envType=daily-question&envId=2026-11-14

class Solution:
    def minimumSumSubarray(self, a: List[int], l: int, r: int) -> int:
        return min((sum(a[i:i+n])for n in range(l,r+1) for i in range(len(a)-n+1)if sum(a[i:i+n])>0), default=-1)

class Solution:
    def minimumSumSubarray(self, a: List[int], l: int, r: int) -> int:
        return min([s for n in range(l,r+1)for i in range(len(a)-n+1)if(s:=sum(a[i:i+n]))>0]or[-1])

class Solution:
    def minimumSumSubarray(self, a: List[int], l: int, r: int) -> int:
        return min([s for n in range(l,r+1)for i in range(len(a)+1)if(s:=sum(a[i-n:i]))>0]or[-1])

test('''
3364. Minimum Positive Sum Subarray 
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.

Return the minimum sum of such a subarray. If no such subarray exists, return -1.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [3, -2, 1, 4], l = 2, r = 3

Output: 1

Explanation:

The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:

[3, -2] with a sum of 1
[1, 4] with a sum of 5
[3, -2, 1] with a sum of 2
[-2, 1, 4] with a sum of 3
Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

Example 2:

Input: nums = [-2, 2, -3, 1], l = 2, r = 3

Output: -1

Explanation:

There is no subarray of length between l and r that has a sum greater than 0. So, the answer is -1.

Example 3:

Input: nums = [1, 2, 3, 4], l = 2, r = 4

Output: 3

Explanation:

The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

 

Constraints:

1 <= nums.length <= 100
1 <= l <= r <= nums.length
-1000 <= nums[i] <= 1000
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
54,049/118.3K
Acceptance Rate
45.7%
Topics
Mid Level
Array
Sliding Window
Prefix Sum
Weekly Contest 425
icon
Companies
Hint 1
Check every subarray, since constraints are small.
Similar Questions
Minimum Size Subarray Sum
Medium
''')
