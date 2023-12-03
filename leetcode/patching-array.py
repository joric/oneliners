from lc import *

# same as https://leetcode.com/problems/minimum-number-of-coins-to-be-added

class Solution:
    def minPatches(self, c: List[int], t: int) -> int:
        c,b,r=sorted(c+[t+1]),0,0
        for v in c:
            while v > b + 1:
                b = 2 * b + 1
                r += 1
            b += v
        return r

# https://leetcode.com/problems/patching-array/discuss/351975/Complete-Insightful-Explanation-or-Recursive-and-Iterative-Solutions

class Solution:
    def minPatches(self, c: List[int], t: int) -> int:
        def f(r,s,c):
            if s>=t:
                return r
            if c[0]<=s+1:
                return f(r,s+c[0],c[1:])
            return f(r+1, s+s+1,c)
        return f(0,0,c)

class Solution:
    def minPatches(self, c: List[int], t: int) -> int:
        return(f:=lambda r,s,c:f(r,s+c[0],c[1:])if c and s+1>=c[0]else f(r+1,s+s+1,c)if s<t else r)(0,0,c)

test('''
330. Patching Array
Hard

1468

130

Add to List

Share
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.

 

Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums is sorted in ascending order.
1 <= n <= 231 - 1
Accepted
66,231
Submissions
161,222
''')

