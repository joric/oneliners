from lc import *

# https://leetcode.com/problems/left-and-right-sum-differences/solutions/7102184/one-line-solution-by-dmi3ev1987-1p6d/?envType=daily-question&envId=2026-06-06

class Solution:
    def leftRightDifference(self, a: list[int]) -> list[int]:
        return map(abs,[s-x-l*2 for l,x,s in zip([0,*accumulate(a)],a,[sum(a)]*len(a))])

class Solution:
    def leftRightDifference(self, a: list[int]) -> list[int]:
        return[abs(sum(a)-2*l-x) for l,x in zip([0,*accumulate(a)],a)]

class Solution:
    def leftRightDifference(self, a: list[int]) -> list[int]:
        return[abs(sum(a[i+1:])-sum(a[:i]))for i in range(len(a))]

class Solution:
    def leftRightDifference(self, a: list[int]) -> list[int]:
        s=sum(a);t=0;return[abs(s-2*(t:=t+x)+x)for x in a]

class Solution:
    def leftRightDifference(self, a: list[int]) -> list[int]:
        s=sum(a);t=0;return[abs(s-t-(t:=t+x))for x in a]

class Solution:
    def leftRightDifference(self, a: list[int]) -> list[int]:
        t=0;return[abs(sum(a)-t-(t:=t+x))for x in a]

test('''
2574. Left and Right Sum Differences
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums of size n.

Define two arrays leftSum and rightSum where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

 

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].
Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
231,050/262.2K
Acceptance Rate
88.1%
Topics
Mid Level
Array
Prefix Sum
Weekly Contest 334
icon
Companies
Hint 1
For each index i, maintain two variables leftSum and rightSum.
Hint 2
Iterate on the range j: [0 … i - 1] and add nums[j] to the leftSum and similarly iterate on the range j: [i + 1 … nums.length - 1] and add nums[j] to the rightSum.
Similar Questions
Find Pivot Index
Easy
Find the Middle Index in Array
Easy
Find the Distinct Difference Array
Easy
Find the N-th Value After K Seconds
Medium
''')
