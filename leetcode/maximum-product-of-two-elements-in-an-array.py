from lc import *

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = -inf
        for x in nums:
            a, b = max(a,x), max(b, min(a, x))
        return (a-1)*(b-1)

# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/discuss/665311/Python-3-one-line

class Solution:
    def maxProduct(self, a: List[int]) -> int:
        return reduce(mul,(x-1for x in nlargest(2,a)))

# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/discuss/4392701/Python-one-line

class Solution:
    def maxProduct(self, a: List[int]) -> int:
        return(a:=nlargest(2,a))and(a[0]-1)*(a[1]-1)

# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/discuss/4392881/2-line-solution-oror-simple-oror-python

class Solution:
    def maxProduct(self, a: List[int]) -> int:
        a.sort();return(a[-1]-1)*(a[-2]-1)

test('''
1464. Maximum Product of Two Elements in an Array
Easy

1960

201

Add to List

Share
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
 

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3
Accepted
245,629
Submissions
302,288
''')

