from lc import *

# https://leetcode.com/problems/zero-array-transformation-i/solutions/6740654/two-simple-lines-of-code-by-mikposp/

class Solution:
    def isZeroArray(self, a: List[int], q: List[List[int]]) -> bool:
        b = [0]*(len(a)+1)
        for l,r in q:
            b[l] += 1
            b[r+1] -= 1
        return all(map(le,a,accumulate(b)))

class Solution:
    def isZeroArray(self, a: List[int], q: List[List[int]]) -> bool:
        (z:=Counter(l for l,r in q)).subtract(Counter(r+1 for l,r in q))
        return all(map(le,a,accumulate(itemgetter(*range(len(a)+1))(z))))

class Solution:
    def isZeroArray(self, a: List[int], q: List[List[int]]) -> bool:
        (z:=Counter(l for l,r in q)).subtract(Counter(r+1 for l,r in q));return all(map(le,a,accumulate(itemgetter(*range(len(a)+1))(z))))

test('''
3355. Zero Array Transformation I
Solved
Medium
Topics
Companies
Hint
You are given an integer array nums of length n and a 2D array queries, where queries[i] = [li, ri].

For each queries[i]:

Select a subset of indices within the range [li, ri] in nums.
Decrement the values at the selected indices by 1.
A Zero Array is an array where all elements are equal to 0.

Return true if it is possible to transform nums into a Zero Array after processing all the queries sequentially, otherwise return false.

 

Example 1:

Input: nums = [1,0,1], queries = [[0,2]]

Output: true

Explanation:

For i = 0:
Select the subset of indices as [0, 2] and decrement the values at these indices by 1.
The array will become [0, 0, 0], which is a Zero Array.
Example 2:

Input: nums = [4,3,2,1], queries = [[1,3],[0,2]]

Output: false

Explanation:

For i = 0:
Select the subset of indices as [1, 2, 3] and decrement the values at these indices by 1.
The array will become [4, 2, 1, 0].
For i = 1:
Select the subset of indices as [0, 1, 2] and decrement the values at these indices by 1.
The array will become [3, 1, 0, 0], which is not a Zero Array.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= li <= ri < nums.length
Seen this question in a real interview before?
1/5
Yes
No
Accepted
44.2K
Submissions
95.2K
Acceptance Rate
46.4%
Topics
Array
Prefix Sum
Companies
Hint 1
Can we use difference array and prefix sum to check if an index can be made zero?
Similar Questions
Zero Array Transformation IV
Medium
''')
