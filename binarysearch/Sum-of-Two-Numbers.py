from bs import *

class Solution:
    def solve(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(nums):
            if target - x in seen:
                return True
            seen[x] = i
        return False

class Solution:
    def solve(self, n: List[int], t: int) -> List[int]:
        return any(t-n[i] in n[:i]+n[i+1:]for i in range(len(n)))

test('''
Given a list of numbers nums and a number k, return whether any two elements from the list add up
to k. You may not use the same element twice.

Note: Numbers can be negative or 0.

Constraints
n ≤ 100,000 where n is the length of nums

Example 1
Input: nums = [35, 8, 18, 3, 22], k = 11
Output: true
Explanation
8 + 3 = 11

Example 2
Input: nums = [10, 36, 22, 14], k = 4
Output: false
Explanation
No two numbers in this list add up to 4.

Example 3
Input: nums = [24, 10, 11, 4], k = 15
Output: true
Explanation
11 + 4 = 15

Example 4
Input: nums = [-22, 22, -11, 11], k = 0
Output: true
Explanation
-11 + 11 = 0

Example 5
Input: nums = [15, 0, 3, 2], k = 15
Output: true
Explanation
15 + 0 = 15
''')

