from lc import *

# Q2. https://leetcode.com/contest/weekly-contest-393/
# https://leetcode.com/problems/maximum-prime-difference/

class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97}
        for i in range(len(nums)):
            if nums[i] in primes:
                for j in reversed(range(len(nums))):
                    if nums[j] in primes:
                        return j-i

class Solution:
    def maximumPrimeDifference(self, a: List[int]) -> int:
        r,g=range(len(a)),range(2,101);g=reduce(lambda r,x:r-set(range(x**2,101,x))if x in r else r,g,set(g))
        for i in r:
            if a[i] in g:
                for j in r[::-1]:
                    if a[j] in g:
                        return j-i

class Solution:
    def maximumPrimeDifference(self, a: List[int]) -> int:
        r=range(len(a));return next(j-i for i in r for j in r[::-1]if{a[i],a[j]}<={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97})

test('''
3115. Maximum Prime Difference
Medium

5

3

Add to List

Share
You are given an integer array nums.

Return an integer that is the maximum distance between the indices of two (not necessarily different) prime numbers in nums.

 

Example 1:

Input: nums = [4,2,9,5,3]

Output: 3

Explanation: nums[1], nums[3], and nums[4] are prime. So the answer is |4 - 1| = 3.

Example 2:

Input: nums = [4,8,2,8]

Output: 0

Explanation: nums[2] is prime. Because there is just one prime number, the answer is |2 - 2| = 0.

 

Constraints:

1 <= nums.length <= 3 * 105
1 <= nums[i] <= 100
The input is generated such that the number of prime numbers in the nums is at least one.
Accepted
17,536
Submissions
31,502
''')
