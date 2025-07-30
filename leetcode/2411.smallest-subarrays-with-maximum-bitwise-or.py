from lc import *

# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/solutions/6998706/two-simple-lines-of-code/

class Solution:
    def smallestSubarrays(self, a: List[int]) -> List[int]:
        return [*map(lambda d:max(d.values())-d[-1]+1,accumulate(range(len(a)-1,-1,-1),lambda d,i:d|{q:i for q in range(32) if a[i]&1<<q}|{-1:i},initial={-1:0}))][:0:-1]

class Solution:
    def smallestSubarrays(self, a: List[int]) -> List[int]:
        d={};return[1-i+max([*(d:=d|{q:i for q in range(32)if a[i]&1<<q}).values(),i])for i in range(len(a)-1,-1,-1)][::-1]

class Solution:
    def smallestSubarrays(self, a: List[int]) -> List[int]:
        d={};return[1-i+max([*(d:=d|{q:i for q in range(32)if a[i]&1<<q}).values(),i])for i in range(len(a))[::-1]][::-1]

test('''
2411. Smallest Subarrays With Maximum Bitwise OR
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array nums of length n, consisting of non-negative integers. For each index i from 0 to n - 1, you must determine the size of the minimum sized non-empty subarray of nums starting at i (inclusive) that has the maximum possible bitwise OR.

In other words, let Bij be the bitwise OR of the subarray nums[i...j]. You need to find the smallest subarray starting at i, such that bitwise OR of this subarray is equal to max(Bik) where i <= k <= n - 1.
The bitwise OR of an array is the bitwise OR of all the numbers in it.

Return an integer array answer of size n where answer[i] is the length of the minimum sized subarray starting at i with maximum bitwise OR.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,0,2,1,3]
Output: [3,3,2,2,1]
Explanation:
The maximum possible bitwise OR starting at any index is 3. 
- Starting at index 0, the shortest subarray that yields it is [1,0,2].
- Starting at index 1, the shortest subarray that yields the maximum bitwise OR is [0,2,1].
- Starting at index 2, the shortest subarray that yields the maximum bitwise OR is [2,1].
- Starting at index 3, the shortest subarray that yields the maximum bitwise OR is [1,3].
- Starting at index 4, the shortest subarray that yields the maximum bitwise OR is [3].
Therefore, we return [3,3,2,2,1]. 
Example 2:

Input: nums = [1,2]
Output: [2,1]
Explanation:
Starting at index 0, the shortest subarray that yields the maximum bitwise OR is of length 2.
Starting at index 1, the shortest subarray that yields the maximum bitwise OR is of length 1.
Therefore, we return [2,1].
 

Other examples:

Input: nums = [0]
Output: [1]

Constraints:

n == nums.length
1 <= n <= 105
0 <= nums[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
15,967/35.1K
Acceptance Rate
45.6%
Topics
Array
Binary Search
Bit Manipulation
Sliding Window
Biweekly Contest 87
icon
Companies
Hint 1
Consider trying to solve the problem for each bit position separately.
Hint 2
Hint 3
Take the maximum distance to such a number, including the current number.
Hint 4
Iterate backwards to achieve a linear complexity.
Similar Questions
Merge k Sorted Lists
Hard
Bitwise ORs of Subarrays
Medium
Longest Subarray With Maximum Bitwise AND
Medium
''')
