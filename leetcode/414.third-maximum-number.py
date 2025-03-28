from lc import *

# https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l1 = l2 = l3 = -inf
        for n in nums:
            if n in (l1, l2, l3):
                continue
            l1, l2, l3 = max(l1, n), max(l2, min(n, l1)), max(l3, min(l2, n))
        return l3 if l3 != -inf else l1

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return heapq.nlargest(3,set(nums))[-1 if len(set(nums)) > 2 else 0]

class Solution:
    def thirdMax(self, a: List[int]) -> int:
        return 3>len({*a})and max(a)or sorted({*a})[-3]

# https://leetcode.com/problems/third-maximum-number/solutions/4274952/set-and-sort/

class Solution:
    def thirdMax(self, a: List[int]) -> int:
        a=sorted({*a});return 3>len(a)and a[-1]or a[-3]

class Solution:
    def thirdMax(self, a: List[int]) -> int:
        a=sorted({*a});return a[(-3,-1)[len(a)<3]]

class Solution:
    def thirdMax(self, a: List[int]) -> int:
        return sorted({*a})[(-3,-1)[len({*a})<3]]

class Solution:
    def thirdMax(self, a: List[int]) -> int:
        return sorted({*a})[(len({*a})<3)*2-3]

test('''
414. Third Maximum Number
Solved
Easy
Topics
Companies
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Can you find an O(n) solution?
Seen this question in a real interview before?
1/5
Yes
No
Accepted
626.6K
Submissions
1.7M
Acceptance Rate
36.3%
Topics
Array
Sorting
Companies
Similar Questions
Kth Largest Element in an Array
Medium
Neither Minimum nor Maximum
Easy
''')
