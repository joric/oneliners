from lc import *

# Q2. biweekly-contest-120 (23 Dec 2024)
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        r = [*accumulate(nums[::-1])][::-1]
        j = n
        for i in range(n-2):
            head = nums[i]
            tail = r[i] - nums[i]
            if head < tail:
                v = [nums[j] for j in range(i,n)]
                m = sum(v)
                return m
        return -1

# numb3r5

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        s = sum(nums)
        nums.sort()
        for r in range(len(nums) - 1, -1, -1):
            if s > 2 * nums[r]:
                return s
            s -= nums[r]
        return -1

class Solution:
    def largestPerimeter(self, n: List[int]) -> int:
        s = sum(n)
        for x in sorted(n)[::-1]:
            if s > 2 * x:
                return s
            s -= x
        return -1

class Solution:
    def largestPerimeter(self, n: List[int]) -> int:
        s=sum(n);return next((s for x in sorted(n)[::-1]if s>2*x or(s:=s-x)<0),-1)

# updated 2024-02-15
# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/discuss/4730895/One-Line-Solution

class Solution:
    def largestPerimeter(self, n: List[int]) -> int:
        s=sum(n);return next((s+x for x in sorted(n)[::-1]if(s:=s-x)>x),-1)

class Solution:
    def largestPerimeter(self, n: List[int]) -> int:
        s=0;return max(2*x<(s:=s+x)and s or-1for x in sorted(n))

class Solution:
    def largestPerimeter(self, n: List[int]) -> int:
        s=0;return max((-1,s:=s+x)[x+x<s]for x in sorted(n))

test('''
100180. Find Polygon With the Largest Perimeter
User Accepted:0
User Tried:0
Total Accepted:0
Total Submissions:0
Difficulty:Medium
You are given an array of positive integers nums of length n.

A polygon is a closed plane figure that has at least 3 sides. The longest side of a polygon is smaller than the sum of its other sides.

Conversely, if you have k (k >= 3) positive real numbers a1, a2, a3, ..., ak where a1 <= a2 <= a3 <= ... <= ak and a1 + a2 + a3 + ... + ak-1 > ak, then there always exists a polygon with k sides whose lengths are a1, a2, a3, ..., ak.

The perimeter of a polygon is the sum of lengths of its sides.

Return the largest possible perimeter of a polygon whose sides can be formed from nums, or -1 if it is not possible to create a polygon.

 

Example 1:

Input: nums = [5,5,5]
Output: 15
Explanation: The only possible polygon that can be made from nums has 3 sides: 5, 5, and 5. The perimeter is 5 + 5 + 5 = 15.
Example 2:

Input: nums = [1,12,1,2,5,50,3]
Output: 12
Explanation: The polygon with the largest perimeter which can be made from nums has 5 sides: 1, 1, 2, 3, and 5. The perimeter is 1 + 1 + 2 + 3 + 5 = 12.
We cannot have a polygon with either 12 or 50 as the longest side because it is not possible to include 2 or more smaller sides that have a greater sum than either of them.
It can be shown that the largest possible perimeter is 12.
Example 3:

Input: nums = [5,5,50]
Output: -1
Explanation: There is no possible way to form a polygon from nums, as a polygon has at least 3 sides and 50 > 5 + 5.
 

Constraints:

3 <= n <= 10^5
1 <= nums[i] <= 10^9
''')
