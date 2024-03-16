from lc import *

class Solution:
    def maxProduct(self, n: List[int]) -> int:
        a,b = n,n[::-1]
        for i in range(1,len(n)):
            a[i] *= a[i-1] or 1
            b[i] *= b[i-1] or 1
        return max(a+b)

# https://leetcode.com/problems/maximum-product-subarray/discuss/4883280/one-line-solution

class Solution:
    def maxProduct(self, n: List[int]) -> int:
        a=b=1;return max((a:=min(q:=(x,a*x,b*x)),b:=max(q))[1]for x in n)

test('''
152. Maximum Product Subarray
Medium

18096

589

Add to List

Share
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
Accepted
1,221,384
Submissions
3,491,490
''')
