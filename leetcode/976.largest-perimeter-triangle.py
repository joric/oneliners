from lc import *

# https://leetcode.com/problems/largest-perimeter-triangle/description/?envType=daily-question&envId=2025-09-28

class Solution:
    def largestPerimeter(self, a: List[int]) -> int:
        a=sorted(a)[::-1];return max((a<b+c)*(a+b+c)for a,b,c in zip(a,a[1:],a[2:]))

class Solution:
    def largestPerimeter(self, a: List[int]) -> int:
        a.sort();return max((p[2]<sum(p[:-1]))*sum(p)for p in zip(a,a[1:],a[2:]))

class Solution:
    def largestPerimeter(self, a: List[int]) -> int:
        a.sort();return max((c<a+b)*(a+b+c)for a,b,c in zip(a,a[1:],a[2:]))

test('''
976. Largest Perimeter Triangle
Solved
Easy
Topics
premium lock icon
Companies
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.
Example 2:

Input: nums = [1,2,1,10]
Output: 0
Explanation: 
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
287,850/498.2K
Acceptance Rate
57.8%
Topics
Array
Math
Greedy
Sorting
Weekly Contest 119
icon
Companies
Similar Questions
Largest Triangle Area
Easy
''')
