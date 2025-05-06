from lc import *

# https://leetcode.com/problems/4sum-ii/solutions/6713875/one-line-solution-by-mikposp-fk6h/

class Solution:
    def fourSumCount(self, a: List[int], b: List[int], w: List[int], o: List[int]) -> int:
        return (z:=Counter(v+u for v in a for u in b)) and sum(z[-p-q] for p in w for q in o)

class Solution:
    def fourSumCount(self, a: List[int], b: List[int], w: List[int], o: List[int]) -> int:
        return (z:=Counter(map(sum,product(a,b)))) and sum(z[-p-q] for p in w for q in o)

test('''
454. 4Sum II
Solved
Medium
Topics
Companies
Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
Example 2:

Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
Output: 1
 

Constraints:

n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
Seen this question in a real interview before?
1/5
Yes
No
Accepted
355.4K
Submissions
617.7K
Acceptance Rate
57.5%
Topics
Array
Hash Table
Companies
Similar Questions
4Sum
''')
