from lc import *

# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/

class Solution:
    def minNumberOperations(self, a: List[int]) -> int:
        return a[0]+sum(max(a[i]-a[i-1],0) for i in range(1,len(a)))

# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/solutions/5076333/python-1-line/

class Solution:
    def minNumberOperations(self, a: List[int]) -> int:
        return sum(a)-sum(min(a[i],a[i+1])for i in range(len(a)-1))

class Solution:
    def minNumberOperations(self, a: List[int]) -> int:
        return sum(a)-sum(min(p)for p in pairwise(a))

# POTD 2025-10-30

class Solution:
    def minNumberOperations(self, a: List[int]) -> int:
        return sum(a)-sum(map(min,pairwise(a)))

test('''
1526. Minimum Number of Increments on Subarrays to Form a Target Array
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.

In one operation you can choose any subarray from initial and increment each value by one.

Return the minimum number of operations to form a target array from initial.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.
Example 2:

Input: target = [3,1,1,2]
Output: 4
Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]
Example 3:

Input: target = [3,1,5,4,2]
Output: 7
Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2].
 

Constraints:

1 <= target.length <= 105
1 <= target[i] <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
66,450/91.2K
Acceptance Rate
72.9%
Topics
Array
Dynamic Programming
Stack
Greedy
Monotonic Stack
Biweekly Contest 31
icon
Companies
Hint 1
For a given range of values in target, an optimal strategy is to increment the entire range by the minimum value. The minimum in a range could be obtained with Range minimum query or Segment trees algorithm.
''')
