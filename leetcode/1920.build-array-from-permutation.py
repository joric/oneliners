from lc import *

# https://leetcode.com/problems/build-array-from-permutation/solutions/5357330/1-line/?envType=daily-question&envId=2025-05-06

class Solution:
    def buildArray(self, a: List[int]) -> List[int]:
        return map(a.__getitem__,map(index,a))

class Solution:
    def buildArray(self, a: List[int]) -> List[int]:
        return[a[a[a.index(i)]]for i in a]

class Solution:
    def buildArray(self, a: List[int]) -> List[int]:
        return[a[i]for i in map(index,a)]

# https://leetcode.com/problems/build-array-from-permutation/solutions/2845384/1-line/?envType=daily-question&envId=2025-05-06

class Solution:
    def buildArray(self, a: List[int]) -> List[int]:
        return[a[a[i]]for i in range(len(a))]

class Solution:
    def buildArray(self, a: List[int]) -> List[int]:
        return[*map(a.__getitem__,a)]

class Solution:
    def buildArray(self, a: List[int]) -> List[int]:
        return[a[x]for x in a]

test('''
1920. Build Array from Permutation
Solved
Easy
Topics
Companies
Hint
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).

 

Example 1:

Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
Explanation: The array ans is built as follows: 
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
Example 2:

Input: nums = [5,0,1,2,3,4]
Output: [4,5,0,1,2,3]
Explanation: The array ans is built as follows:
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < nums.length
The elements in nums are distinct.
 

Follow-up: Can you solve it without using an extra space (i.e., O(1) memory)?

Seen this question in a real interview before?
1/5
Yes
No
Accepted
628.2K
Submissions
696K
Acceptance Rate
90.3%
Topics
Array
Simulation
Companies
Hint 1
Just apply what's said in the statement.
Hint 2
Notice that you can't apply it on the same array directly since some elements will change after application
''')

