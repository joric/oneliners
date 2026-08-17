from lc import *

# https://leetcode.com/problems/find-the-largest-almost-missing-integer/solutions/6510507/python-one-liner-by-knatti-8idy/?envType=daily-question&envId=2026-08-18

class Solution:
    def largestInteger(self, n: List[int], k: int) -> int:
        return max([x for x,c in Counter(x for i in range(len(n)-k+1)for x in set(n[i:i+k])).items()if c<2]+[-1])

class Solution:
    def largestInteger(self, n: List[int], k: int) -> int:
        return max(n) if k==len(n) else max([x for x in (n if k<2 else(n[0],n[-1])) if n.count(x)<2]+[-1])

class Solution:
    def largestInteger(self, n: List[int], k: int) -> int:
        return  max(n)if k==len(n)else max([x for x in(n if k<2 else(n[0],n[-1]))if n.count(x)<2]+[-1])

class Solution:
    def largestInteger(self, n: List[int], k: int) -> int:
        l=len(n);return max(n if k==l else[x for x in n[::(k>1)*l-1]if n.count(x)<2]+[-1])

class Solution:
    def largestInteger(self, n: List[int], k: int) -> int:
        return max([-1]+[x for x in n[::(k>1)*len(n)-1]if n.count(x)<2]if n[k:]else n)

test('''
3471. Find the Largest Almost Missing Integer
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

A subarray is a contiguous sequence of elements within an array.
 

Example 1:

Input: nums = [3,9,2,1,7], k = 3

Output: 7

Explanation:

1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
3 appears in 1 subarray of size 3: [3, 9, 2].
7 appears in 1 subarray of size 3: [2, 1, 7].
9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
We return 7 since it is the largest integer that appears in exactly one subarray of size k.

Example 2:

Input: nums = [3,9,7,2,1,7], k = 4

Output: 3

Explanation:

1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
3 appears in 1 subarray of size 4: [3, 9, 7, 2].
7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

Example 3:

Input: nums = [0,0], k = 1

Output: -1

Explanation:

There is no integer that appears in only one subarray of size 1.

 

Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 50
1 <= k <= nums.length
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
38,027/101.4K
Acceptance Rate
37.5%
Topics
Mid Level
Array
Hash Table
Weekly Contest 439
icon
Companies
Hint 1
Solve the problem for three different cases: k = 1, k = n, and 1 < k < n
Hint 2
If k = 1, return the largest element that occurs exactly once in nums
Hint 3
If k = n, return the largest element in nums
Hint 4
If 1 < k < n, all elements different from nums[0] and nums[n - 1] will occur in more than one subarray of size k. Hence, the answer is the largest of nums[0] and nums[n - 1] if they both occur exactly once in the array. If one of them occurs more than once, return the other. If both of them occur more than once, return -1.
Similar Questions
Missing Number
Easy
''')
