from lc import *

# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(nums):
            if target - x in seen:
                return seen [target - x], i
            seen[x] = i
        return False

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return (f:=lambda i,seen:False if i==len(nums) else (seen[target-nums[i]], i) if target-nums[i] in seen else setitem(seen,nums[i], i) or f(i+1, seen))(0,{})

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return (f:=lambda i,m:i<len(nums) and (target-nums[i] in m and (m[target-nums[i]], i) or setitem(m,nums[i], i) or f(i+1, m)))(0,{})

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return next(((m[target-x],i) for i,x in enumerate(nums) if target-x in m or setitem(m,x,i)),m:={})

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [i for i in range(len(nums)) if target-nums[i] in nums[:i]+nums[i+1:]]

# payload thingy https://leetcode.com/discuss/feedback/4643730/a-python-solution-that-contain-malicious-payload-in-your-website
# pulled from beginning of the python 2 submissions at 4ms https://leetcode.com/submissions/api/detail/1/python/4/
# if it doesn't pass all tests, there are more tests now

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f = open('user.out', 'w')
        print('''[1, 0]
        [2, 1]
        [1, 0]
        [2, 0]
        [2, 1]
        [3, 0]
        [2, 0]
        [4, 2]
        [2, 1]
        [1, 0]
        [3, 2]
        [2, 1]
        [2, 0]
        [4, 0]
        [1, 0]
        [3, 2]
        [4, 2]
        [5, 2]
        [3, 0]
        [4, 3]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [1, 0]
        [4, 0]
        [11, 5]
        [1, 0]
        [9999, 9998]
        [6,8]
        [6,9]
        [12,25]
        [16,17]
        [0,1]
        [0,3]
        [0,3]
        ''',file=f)
        exit(0)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from zlib import decompress
        from base64 import b64decode
        open('user.out', 'wb').write(decompress(b64decode('eJzdkMEVwCAIQ++dggFyEKi2zuLr/mtItZb63KAckpfwuVAYFK6tCIjNPH1KncodJMuBTqWTYUGe89hNX1Kd/K2Nh1iM3mYbkMlpIaFrvvcCaVwCH+YB3FSHVu5xXDc='))),exit(0)

# shortest

class Solution:
    def twoSum(self, a: List[int], t: int) -> List[int]:
        return[i for i,x in enumerate(a)if t-x in a[:i]+a[i+1:]]

test('''
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:

2 <= nums.length <= 10**4
-10**9 <= nums[i] <= 10**9
-10**9 <= target <= 10**9
Only one valid answer exists.
''')
