from lc import *

class Solution:
    def numIdenticalPairs(self, a: List[int]) -> int:
        r,c=0,Counter();[(r:=r+c[x],c.update({x:1}))for x in a];return r

class Solution:
    def numIdenticalPairs(self, a: List[int]) -> int:
        return sum(x*(x-1)//2for x in Counter(a).values())

class Solution:
    def numIdenticalPairs(self, a: List[int]) -> int:
        return sum(comb(x,2)for x in Counter(a).values())

test('''
1512. Number of Good Pairs
Easy

4296

204

Add to List

Share
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
''')

