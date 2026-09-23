from lc import *

# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/solutions/7434163/one-line-by-khaled-alomari-rkxo/?envType=daily-question&envId=2026-09-24

# typescript: const smallestIndex=(a: number[])=>a.findIndex((v,i)=>i===`${v}`.split('').reduce((a,b) => a + +b,0));

class Solution:
    def smallestIndex(self, a: List[int]) -> int:
        return next((i for i,x in enumerate(a)if i==sum(map(int,str(x)))),-1)

class Solution:
    def smallestIndex(self, a: List[int]) -> int:
        return[*(i for i,c in enumerate(a)if i==sum(map(int,str(c)))),-1][0]

class Solution:
    def smallestIndex(self, a: List[int]) -> int:
        i=-1;return[*(i for x in a if(i:=i+1)==sum(map(int,str(x)))),-1][0]

class Solution:
    def smallestIndex(self, a: List[int]) -> int:
        i=-1;return[*(i for x in a if(i:=i+1)==sum(b'%d'%x)%48),-1][0]

class Solution:
    def smallestIndex(self, a: List[int]) -> int:
        i=-1;return bytes(sum(b'%d'%x)%48^(i:=i+1)for x in a).find(0)

class Solution:
    def smallestIndex(self, a: List[int]) -> int:
        i=1;return bytes(sum(b'%04d'%x,i:=i-1)for x in a).find(192)

test('''
3550. Smallest Index With Digit Sum Equal to Index
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums.

Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

If no such index exists, return -1.

 

Example 1:

Input: nums = [1,3,2]

Output: 2

Explanation:

For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.
Example 2:

Input: nums = [1,10,11]

Output: 1

Explanation:

For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.
For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.
Since index 1 is the smallest, the output is 1.
Example 3:

Input: nums = [1,2,3]

Output: -1

Explanation:

Since no index satisfies the condition, the output is -1.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
62,297/78.3K
Acceptance Rate
79.6%
Topics
Mid Level
Array
Math
Weekly Contest 450
icon
Companies
Hint 1
Simulate as described
''')
