from lc import *

# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/730973/Python3-priority-queue

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        h = [(x, i) for i, x in enumerate(nums)] #min-heap 
        heapify(h)
        ans = 0
        for k in range(1, right+1): #1-indexed
            x, i = heappop(h)
            if k >= left: ans += x
            if i+1 < len(nums): 
                heappush(h, (x + nums[i+1], i+1))
                
        return ans % 1_000_000_007

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ans = []
        for i in range(len(nums)):
            prefix = 0
            for ii in range(i, len(nums)):
                prefix += nums[ii]
                ans.append(prefix)
        ans.sort()
        return sum(ans[left-1:right]) % 1_000_000_007

class Solution:
    def rangeSum(self, a: List[int], n: int, l: int, r: int) -> int:
        p,n=0,len(a);return sum(sorted(p:=(0,p)[i<j]+a[j]for i in range(n)for j in range(i,n))[l-1:r])%(10**9+7)

# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/4831099/One-Liner-Easy-Python-Solution-using-List-Comprehension
# very slow, 8s

class Solution:
    def rangeSum(self, a: List[int], n: int, l: int, r: int) -> int:
        n=len(a);return sum(sorted([sum([x for x in a[i:j]])for i in range(n)for j in range(i+1,n+1)])[l-1:r])%(10**9+7)

# https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/discuss/732802/Python-1-Liner-Simulation-solution

class Solution:
    def rangeSum(self, a: List[int], n: int, l: int, r: int) -> int:
        return sum(sorted(chain(*[accumulate(a[i:])for i in range(n)]))[l-1:r])%(10**9+7)

test('''
1508. Range Sum of Sorted Subarray Sums
Medium

932

156

Add to List

Share
You are given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous subarrays from the array and then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the answer can be a huge number return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13 
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2 + 3 + 3 + 4 = 13. 
Example 2:

Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
Output: 6
Explanation: The given array is the same as example 1. We have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to ri = 4 is 3 + 3 = 6.
Example 3:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
Output: 50
 

Constraints:

n == nums.length
1 <= nums.length <= 1000
1 <= nums[i] <= 100
1 <= left <= right <= n * (n + 1) / 2
''')
