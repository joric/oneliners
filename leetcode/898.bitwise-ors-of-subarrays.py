from lc import *

# https://leetcode.com/problems/bitwise-ors-of-subarrays/solutions/327075/python3-5-line-concise-solution/?envType=daily-question&envId=2025-07-31

class Solution:
    def subarrayBitwiseORs(self, a: List[int]) -> int:
        c,r=set(),set()
        for i in a:
            r|=(c:={i|j for j in c}|{i})
        return len(r)

class Solution: # TLE
    def subarrayBitwiseORs(self, a: List[int]) -> int:
        return len(set(chain.from_iterable(accumulate(a[i:],or_)for i in range(len(a)))))

class Solution:
    def subarrayBitwiseORs(self, a: List[int]) -> int:
        return len((r:=set(),c:=set(),[r.update(c:={i|j for j in c}|{i})for i in a])[0]);

class Solution:
    def subarrayBitwiseORs(self, a: List[int]) -> int:
        c,r=set(),set();[r.update(c:={i|j for j in c}|{i})for i in a];return len(r)

test('''
898. Bitwise ORs of Subarrays
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.

The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: arr = [0]
Output: 1
Explanation: There is only one possible result: 0.
Example 2:

Input: arr = [1,1,2]
Output: 3
Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
Example 3:

Input: arr = [1,2,4]
Output: 6
Explanation: The possible results are 1, 2, 3, 4, 6, and 7.
 

Constraints:

1 <= arr.length <= 5 * 104
0 <= arr[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
44,218/107.6K
Acceptance Rate
41.1%
Topics
Array
Dynamic Programming
Bit Manipulation
Weekly Contest 100
icon
Companies
Similar Questions
Longest Nice Subarray
Medium
Smallest Subarrays With Maximum Bitwise OR
Medium
Bitwise OR of All Subsequence Sums
Medium
Find the Maximum Sequence Value of Array
Hard
''')
