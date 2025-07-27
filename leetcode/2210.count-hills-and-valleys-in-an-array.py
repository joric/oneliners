from lc import *

# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/solutions/6994740/two-simple-lines-of-code/?envType=daily-question&envId=2025-07-27

class Solution:
    def countHillValley(self, a: List[int]) -> int:
        d=[v for v,_ in groupby(a)];return sum(l>m<r or l<m>r for l,m,r in zip(d,d[1:],d[2:]))

class Solution:
    def countHillValley(self, a: List[int]) -> int:
        d=[x-y for x,y in zip(a,a[1:])if x!=y];return sum(x*y<0 for x,y in zip(d,d[1:]))

class Solution:
    def countHillValley(self, a: List[int]) -> int:
        d=[*filter(None,map(sub,a,a[1:]))];return sum(x*y<0 for x,y in zip(d,d[1:]))

class Solution:
    def countHillValley(self, a: List[int]) -> int:
        d=[*filter(None,map(sub,a,a[1:]))];return sum(x*y<0 for x,y in pairwise(d))

class Solution:
    def countHillValley(self, a: List[int]) -> int:
        return sum(x*y<0for x,y in pairwise(filter(None,map(sub,a,a[1:]))))

test('''
2210. Count Hills and Valleys in an Array
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.

 

Example 1:

Input: nums = [2,4,1,1,6,5]
Output: 3
Explanation:
At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a valley.
At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a hill. 
At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a valley.
At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a valley, but note that it is part of the same valley as index 2.
At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a hill.
At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a valley. 
There are 3 hills and valleys so we return 3.
Example 2:

Input: nums = [6,6,5,5,4,1]
Output: 0
Explanation:
At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill nor a valley.
At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill nor a valley.
At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 2 is neither a hill nor a valley.
At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 3 is neither a hill nor a valley.
At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index 4 is neither a hill nor a valley.
At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill nor a valley.
There are 0 hills and valleys so we return 0.
 

Constraints:

3 <= nums.length <= 100
1 <= nums[i] <= 100
Seen this question in a real interview before?
1/5
Yes
No
Accepted
61,762/100.1K
Acceptance Rate
61.7%
Topics
Array
Weekly Contest 285
icon
Companies
Hint 1
For each index, could you find the closest non-equal neighbors?
Hint 2
Ensure that adjacent indices that are part of the same hill or valley are not double-counted.
Similar Questions
Find Peak Element
Medium
Monotonic Array
Easy
Minimum Subsequence in Non-Increasing Order
Easy
''')
