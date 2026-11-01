from lc import *

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/solutions/293885/one-line-python-two-line-java-zhuangb-as-bph9/?envType=daily-question&envId=2026-11-02

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        return sum([abs(num-m) for m in (sorted(nums)[len(nums)//2],) for num in nums])

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/solutions/5668758/one-line-solution-by-mikposp-un0a/?envType=daily-question&envId=2026-11-02

class Solution:
    def minMoves2(self, a: List[int]) -> int:
        a.sort();return sum(a[len(a)//2:])-sum(a[:len(a)+1>>1])

class Solution:
    def minMoves2(self, a: List[int]) -> int:
        return sum(map(abs,map(sub,a,repeat(median_low(a)))))

test('''
462. Minimum Moves to Equal Array Elements II
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Test cases are designed so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16
 

Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
243,382/388.7K
Acceptance Rate
62.6%
Topics
Principal
Array
Math
Sorting
icon
Companies
Similar Questions
Best Meeting Point
Hard
Minimum Moves to Equal Array Elements
Medium
Minimum Operations to Make a Uni-Value Grid
Medium
Removing Minimum Number of Magic Beans
Medium
Minimum Cost to Make Array Equal
Hard
Minimum Operations to Make All Array Elements Equal
Medium
Minimum Cost to Make Array Equalindromic
Medium
Minimum Operations to Make Subarray Elements Equal
Medium
Minimum Operations to Make Elements Within K Subarrays Equal
Hard
''')
