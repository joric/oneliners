from lc import *

# https://leetcode.com/problems/maximum-gap/solutions/1240543/python-bucket-sort-explained/

class Solution:
    def maximumGap(self, nums):
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo: return hi - lo
        B = defaultdict(list)
        for num in nums:
            ind = n-2 if num == hi else (num - lo)*(n-1)//(hi-lo)
            B[ind].append(num)
        cands = [[min(B[i]), max(B[i])] for i in range(n-1) if B[i]]
        return max(y[0]-x[1] for x,y in zip(cands, cands[1:]))

# https://leetcode.com/problems/maximum-gap/description/

class Solution:
    def maximumGap(self, a: List[int]) -> int:
        a.sort();return max((a[i]-a[i-1] for i in range(1,len(a))),default=0)

class Solution:
    def maximumGap(self, a: List[int]) -> int:
        return max([0]+[y-x for x,y in zip(sorted(a),sorted(a)[1:])])

class Solution:
    def maximumGap(self, a: List[int]) -> int:
        a.sort();return max([0]+[y-x for x,y in pairwise(a)])

test('''
164. Maximum Gap
Solved
Medium
Topics
Companies
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

 

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
272.6K
Submissions
554.8K
Acceptance Rate
49.1%
Topics
Array
Sorting
Bucket Sort
Radix Sort
Companies
Similar Questions
Widest Vertical Area Between Two Points Containing No Points
Easy
Maximum Consecutive Floors Without Special Floors
Medium
''')
