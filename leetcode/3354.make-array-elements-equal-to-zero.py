from lc import *

# https://leetcode.com/problems/make-array-elements-equal-to-zero/solutions/6553009/7-line-solution-using-partial-sums/

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        while 0 in nums:
            ind = nums.index(0)
            if sum(nums[:ind]) == sum(nums[ind:]):
                count += 2
            elif abs(sum(nums[:ind]) - sum(nums[ind:])) == 1:
                count += 1
            nums.remove(0)

        return count

# https://leetcode.com/problems/make-array-elements-equal-to-zero/solutions/6054243/python-one-line/

class Solution:
    def countValidSelections(self, a: List[int]) -> int:
        return (lambda ps,t: reduce(lambda p, i: p + (2 if t-ps[i] == ps[i] else abs(t-2*ps[i]) == 1), [i for i, v in enumerate(a) if v == 0], 0))(list(accumulate(a, initial=0)), sum(a))

class Solution:
    def countValidSelections(self, a: List[int]) -> int:
        p,s=[0,*accumulate(a)],sum(a);return sum(1==abs(t:=s-2*p[i])or 2*(t==0)for i,x in enumerate(a)if x==0)

# this passes

class Solution:
    def countValidSelections(self, a: List[int]) -> int:
        p,s=0,sum(a);return sum(1==abs(t:=s-2*p)or(t==0)*2for x in a if p==(p:=p+x))

test('''
3354. Make Array Elements Equal to Zero
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.

After that, you repeat the following process:

If curr is out of the range [0, n - 1], this process ends.
If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
Else if nums[curr] > 0:
Decrement nums[curr] by 1.
Reverse your movement direction (left becomes right and vice versa).
Take a step in your new direction.
A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.

Return the number of possible valid selections.

 

Example 1:

Input: nums = [1,0,2,0,3]

Output: 2

Explanation:

The only possible valid selections are the following:

Choose curr = 3, and a movement direction to the left.
[1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,1,0,3] -> [1,0,1,0,3] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,0,0,2] -> [1,0,0,0,2] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,1] -> [0,0,0,0,0].
Choose curr = 3, and a movement direction to the right.
[1,0,2,0,3] -> [1,0,2,0,3] -> [1,0,2,0,2] -> [1,0,2,0,2] -> [1,0,1,0,2] -> [1,0,1,0,2] -> [1,0,1,0,1] -> [1,0,1,0,1] -> [1,0,0,0,1] -> [1,0,0,0,1] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [1,0,0,0,0] -> [0,0,0,0,0].
Example 2:

Input: nums = [2,3,4,0,4,1,0]

Output: 0

Explanation:

There are no possible valid selections.

Other examples:

Input: nums = [16,13,10,0,0,0,10,6,7,8,7]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
There is at least one element i where nums[i] == 0.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
29,170/52.2K
Acceptance Rate
55.9%
Topics
Array
Simulation
Prefix Sum
Weekly Contest 424
icon
Companies
Hint 1
Since the constraints are very small, you can simulate the process described.
''')
