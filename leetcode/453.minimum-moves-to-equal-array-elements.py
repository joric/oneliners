from lc import *

# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/solutions/6711789/one-line-solution-by-mikposp-pvjx/

class Solution:
    def minMoves(self, a: List[int]) -> int:
        return sum(a)-len(a)*min(a)

class Solution:
    def minMoves(self, a: List[int]) -> int:
        return sum(map(sub,a,repeat(min(a))))

test('''
453. Minimum Moves to Equal Array Elements
Medium
Topics
Companies
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment n - 1 elements of the array by 1.

 

Example 1:

Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
Example 2:

Input: nums = [1,1,1]
Output: 0
 

Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
The answer is guaranteed to fit in a 32-bit integer.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
194.9K
Submissions
338.2K
Acceptance Rate
57.6%
Topics
Array
Math
Companies
Similar Questions
Minimum Moves to Equal Array Elements II
Medium
Maximum Running Time of N Computers
Hard
Pour Water Between Buckets to Make Water Levels Equal
Medium
Divide Players Into Teams of Equal Skill
Medium
Find Minimum Operations to Make All Elements Divisible by Three
Easy
''')
