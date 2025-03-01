from lc import *

# https://leetcode.com/problems/apply-operations-to-an-array/solutions/2784689/python3-simple-solution-list-comprehension/?envType=daily-question&envId=2025-03-01

class Solution:
    def applyOperations(self, a: List[int]) -> List[int]:
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                a[i] *= 2
                a[i+1] = 0
        return sorted(a,key=not_)

# https://leetcode.com/problems/apply-operations-to-an-array/solutions/6479212/python-one-liner-code-golf/?envType=dail

# class Solution:applyOperations=lambda _,n:sorted(sum(((l:=len([*g]))//2*[k*2,0]+l%2*[k]for k,g in groupby(n)),[]),key=not_)

class Solution:
    def applyOperations(self, a: List[int]) -> List[int]:
        return sorted(sum(((l:=len([*g]))//2*[k*2,0]+l%2*[k]for k,g in groupby(a)),[]),key=not_)

class Solution:
    def applyOperations(self, a: List[int]) -> List[int]:
        return sorted(chain(*((l:=len([*g]))//2*[k*2,0]+l%2*[k]for k,g in groupby(a))),key=not_)

class Solution:
    def applyOperations(self, a: List[int]) -> List[int]:
        [a[i-1]-a[i]or exec('a[i-1]*=2;a[i]=0')for i in range(len(a))];return sorted(a,key=not_)


test('''
2460. Apply Operations to an Array
Easy
Topics
Companies
Hint
You are given a 0-indexed array nums of size n consisting of non-negative integers.

You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
After performing all the operations, shift all the 0's to the end of the array.

For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
Return the resulting array.

Note that the operations are applied sequentially, not all at once.

 

Example 1:

Input: nums = [1,2,2,1,1,0]
Output: [1,4,2,0,0,0]
Explanation: We do the following operations:
- i = 0: nums[0] and nums[1] are not equal, so we skip this operation.
- i = 1: nums[1] and nums[2] are equal, we multiply nums[1] by 2 and change nums[2] to 0. The array becomes [1,4,0,1,1,0].
- i = 2: nums[2] and nums[3] are not equal, so we skip this operation.
- i = 3: nums[3] and nums[4] are equal, we multiply nums[3] by 2 and change nums[4] to 0. The array becomes [1,4,0,2,0,0].
- i = 4: nums[4] and nums[5] are equal, we multiply nums[4] by 2 and change nums[5] to 0. The array becomes [1,4,0,2,0,0].
After that, we shift the 0's to the end, which gives the array [1,4,2,0,0,0].
Example 2:

Input: nums = [0,1]
Output: [1,0]
Explanation: No operation can be applied, we just shift the 0 to the end.
 

Constraints:

2 <= nums.length <= 2000
0 <= nums[i] <= 1000
Seen this question in a real interview before?
1/5
Yes
No
Accepted
81.1K
Submissions
118.1K
Acceptance Rate
68.7%
Topics
Array
Two Pointers
Simulation
Companies
Hint 1
Iterate over the array and simulate the described process.
Similar Questions
Remove Duplicates from Sorted Array
Easy
Move Zeroes
Easy
''')
