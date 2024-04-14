from lc import *

# Q4. https://leetcode.com/contest/weekly-contest-393/
# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n = len(nums)
        m = len(andValues)
        @cache
        def calculate_min_sum(mask, j, k): 
            if k == m and j == n:
                return 0
            if k == m or j == n:
                return float('inf')
            mask &= nums[j]
            if mask < andValues[k]:
                return float('inf')
            if mask == andValues[k]:
                return min(calculate_min_sum(mask, j+1, k), nums[j] + calculate_min_sum((1<<32)-1, j+1, k+1))
            if mask > andValues[k]:
                return calculate_min_sum(mask, j+1, k)
        ans = calculate_min_sum((1<<32)-1, 0, 0)
        return ans if ans < float('inf') else -1

class Solution:
    def minimumValueSum(self, a: List[int], v: List[int]) -> int:
        n,m=len(a),len(v)
        @cache
        def f(b,j,k): 
            if k==m and j==n:
                return 0
            if k==m or j==n:
                return inf
            b &= a[j]
            if b < v[k]:
                return inf
            if b == v[k]:
                return min(f(b,j+1,k),a[j]+f((1<<32)-1,j+1,k+1))
            if b > v[k]:
                return f(b,j+1,k)
        return(-1,r:=f((1<<32)-1,0,0))[r<inf]

class Solution:
    def minimumValueSum(self, a: List[int], v: List[int]) -> int:
        return(-1,r:=(f:=cache(lambda b,j,k:0 if k==len(v)and j==len(a)else inf if k==len(v)or j==len(a)or(b:=b&a[j])<v[k]else min(f(b,j+1,k),a[j]+f((1<<32)-1,j+1,k+1))if b==v[k]else f(b,j+1,k)))((1<<32)-1,0,0))[r<inf]


class Solution:
    def minimumValueSum(self, a: List[int], v: List[int]) -> int:
        @cache
        def f(b,j,k): 
            if k==len(v) and j==len(a):
                return 0
            if k==len(v) or j==len(a):
                return inf
            b &= a[j]
            if b < v[k]:
                return inf
            if b == v[k]:
                return min(f(b,j+1,k),a[j]+f((1<<32)-1,j+1,k+1))
            if b > v[k]:
                return f(b,j+1,k)
        return(-1,r:=f((1<<32)-1,0,0))[r<inf]

test('''
3117. Minimum Sum of Values by Dividing Array
Hard

12

1

Add to List

Share
You are given two arrays nums and andValues of length n and m respectively.

The value of an array is equal to the last element of that array.

You have to divide nums into m disjoint contiguous subarrays such that for the ith subarray [li, ri], the bitwise AND of the subarray elements is equal to andValues[i], in other words, nums[li] & nums[li + 1] & ... & nums[ri] == andValues[i] for all 1 <= i <= m, where & represents the bitwise AND operator.

Return the minimum possible sum of the values of the m subarrays nums is divided into. If it is not possible to divide nums into m subarrays satisfying these conditions, return -1.

 

Example 1:

Input: nums = [1,4,3,3,2], andValues = [0,3,3,2]

Output: 12

Explanation:

The only possible way to divide nums is:

[1,4] as 1 & 4 == 0.
[3] as the bitwise AND of a single element subarray is that element itself.
[3] as the bitwise AND of a single element subarray is that element itself.
[2] as the bitwise AND of a single element subarray is that element itself.
The sum of the values for these subarrays is 4 + 3 + 3 + 2 = 12.

Example 2:

Input: nums = [2,3,5,7,7,7,5], andValues = [0,7,5]

Output: 17

Explanation:

There are three ways to divide nums:

[[2,3,5],[7,7,7],[5]] with the sum of the values 5 + 7 + 5 == 17.
[[2,3,5,7],[7,7],[5]] with the sum of the values 7 + 7 + 5 == 19.
[[2,3,5,7,7],[7],[5]] with the sum of the values 7 + 7 + 5 == 19.
The minimum possible sum of the values is 17.

Example 3:

Input: nums = [1,2,3,4], andValues = [2]

Output: -1

Explanation:

The bitwise AND of the entire array nums is 0. As there is no possible way to divide nums into a single subarray to have the bitwise AND of elements 2, return -1.

 

Constraints:

1 <= n == nums.length <= 104
1 <= m == andValues.length <= min(n, 10)
1 <= nums[i] < 105
0 <= andValues[j] < 105
Accepted
420
Submissions
4,617
''')

