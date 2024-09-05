from lc import *

# https://leetcode.com/problems/find-the-duplicate-number

# Joma Tech - If Programming Was An Anime https://youtu.be/pKO9UjSeLew

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        return hare

class Solution:
    def findDuplicate(self, n: List[int]) -> int:
        return Counter(n).most_common(1)[0][0]

class Solution:
    def findDuplicate(self, n: List[int]) -> int:
        return mode(n)

test('''
287. Find the Duplicate Number
Medium

20894

3446

Add to List

Share
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
 

Constraints:

1 <= n <= 10^5
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
''')
