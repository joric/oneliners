from lc import *

# Q4. https://leetcode.com/contest/weekly-contest-393/
# https://leetcode.com/problems/minimum-sum-of-values-by-dividing-array/

class Solution:
    def minimumValueSum(self, a: List[int], v: List[int]) -> int:
        @cache
        def f(i,j,b=(1<<32)-1): 
            if i==len(a) and j==len(v):
                return 0
            if i==len(a) or j==len(v):
                return inf
            return inf if(b:=b&a[i])<v[j]else f(i+1,j,b)if b>v[j]else min(f(i+1,j,b),a[i]+f(i+1,j+1))
        return(-1,r:=f(0,0))[r<inf]

class Solution:
    def minimumValueSum(self, a: List[int], v: List[int]) -> int:
        return(-1,r:=(f:=cache(lambda i,j,b=(1<<32)-1:0 if i==len(a)and j==len(v)else inf if i==len(a)or j==len(v)or(b:=b&a[i])<v[j]else f(i+1,j,b)if b>v[j]else min(f(i+1,j,b),a[i]+f(i+1,j+1))))(0,0))[r<inf]

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

Other examples:


Input: nums = [4,4], andValues = [4]
Output: 4

 

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
