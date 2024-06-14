from lc import *

# https://leetcode.com/problems/minimum-increment-to-make-array-unique/discuss/197687/JavaC%2B%2BPython-Straight-Forward

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = need = 0
        for i in sorted(nums):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res

class Solution:
    def minIncrementForUnique(self, n: List[int]) -> int:
        p=0;return sum((max(p-x,0),p:=max(p+1,x+1))[0]for x in sorted(n))

class Solution:
    def minIncrementForUnique(self, n: List[int]) -> int:
        p=0;return sum(~x+(p:=max(p,x)+1)for x in sorted(n))

test('''
945. Minimum Increment to Make Array Unique
Medium

1834

58

Add to List

Share
You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
Accepted
93,452
Submissions
175,917
''')
