from lc import *

# https://leetcode.com/problems/first-missing-positive

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Use cycle sort to place positive elements smaller than n
        # at the correct index
        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                # swap
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        # Iterate through nums
        # return smallest missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all elements are at the correct index
        # the smallest missing positive number is n + 1
        return n + 1

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # "opportunistic cyclic sort": assuming all 1 <= i <= k are present in
        # array once, put them to cell they belong to in sorted subarray [1:k]
        # time = O(n)
        n=len(nums)
        all(any((t:=nums[i]) <= 0 or t >= n or t == (v:=nums[t]) or  setitem(nums,i,v) or setitem(nums,t,t) for _ in range(n)) for i in range(n))
        # here either nums[i] == i, or i != nums[j] for all j in [0:n)
        # (so i is first missing positive number)
        r=0
        return any(nums[i] != i and (r:=i) for i in range(1,n)) and r or (nums[0] + 1 if nums[0] == n else n)
        # nums[i] = i for all 1 <= i <= n;
        # nums[0] is either n (then it should be skipped too),
        # or any other number (then first missing positive number is n)

class Solution:
    def firstMissingPositive(self, n: List[int]) -> int:
        return min({*range(1,len(n)+2)}-{*n})

class Solution:
    def firstMissingPositive(self, n: List[int]) -> int:
        return min({*range(1,9**6)}-{*n})

test('''
41. First Missing Positive
Hard

15878

1788

Add to List

Share
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
Accepted
1,057,631
Submissions
2,785,357
''')