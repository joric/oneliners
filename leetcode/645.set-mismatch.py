from lc import *

# https://leetcode.com/problems/set-mismatch/discuss/1089475/python-o-n-time-o-1-space-math-solution-explained

class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        a = -sum(nums) + n*(n+1)//2
        b = -sum(i*i for i in nums) + n*(n+1)*(2*n+1)//6
        return [(b-a*a)//2//a, (b+a*a)//2//a]

# https://leetcode.com/problems/set-mismatch/discuss/105558/Oneliner-Python

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return sum(nums) - sum(set(nums)), sum(range(1, len(nums)+1)) - sum(set(nums))

class Solution:
    def findErrorNums(self, n: List[int]) -> List[int]:
        t=sum({*n});return[sum(n)-t,sum(range(1,len(n)+1))-t]

class Solution:
    def findErrorNums(self, n: List[int]) -> List[int]:
        t,c=sum({*n}),len(n);return[sum(n)-t,c*-~c//2-t]

class Solution:
    def findErrorNums(self, n: List[int]) -> List[int]:
        t=sum({*n});return sum(n)-t,comb(len(n)+1,2)-t

# https://leetcode.com/problems/set-mismatch/discuss/4608368/one-line-solution

class Solution:
    def findErrorNums(self, n: List[int]) -> List[int]:
        return mode(n),comb(len(n)+1,2)-sum({*n})

test('''
645. Set Mismatch
Easy

You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:

Input: nums = [1,1]
Output: [1,2]

Constraints:

2 <= nums.length <= 10^4
1 <= nums[i] <= 10^4
''')