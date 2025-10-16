from lc import *

# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/solutions/6795180/4-lines-python/?envType=daily-question&envId=2025-10-16

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        d=Counter([abs(num%value) for num in nums])
        for i in range(len(nums)+2):
            if d[i%value]==0:return i
            else: d[i%value]-=1

class Solution:
    def findSmallestInteger(self, a: List[int], v: int) -> int:
        c=Counter(abs(x%v) for x in a)
        for i in range(len(a)+2):
            if c[i%v]==0:
                return i
            else:
                c[i%v]-=1

# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/solutions/3314573/python-5-lines-solution/?envType=daily-question&envId=2025-10-16

class Solution:
    def findSmallestInteger(self, nums: List[int], val: int) -> int:
        bucket = [0] * val
        for num in nums:
           bucket[num%val] += 1
        return min(bucket)*val + bucket.index(min(bucket))

class Solution: # TLE
    def findSmallestInteger(self, a: List[int], v: int) -> int:
        return min(c:=[sum(x%v==i for x in a)for i in range(v)])*v+c.index(min(c))

class Solution: # TLE
    def findSmallestInteger(self, a: List[int], v: int) -> int:
        return min(range(v),key=lambda i:(sum(x%v==i for x in a),i))

class Solution:
    def findSmallestInteger(self, a: List[int], v: int) -> int:
        c=[0]*v;[setitem(c,x%v,c[x%v]+1)for x in a];return min(c)*v+c.index(min(c))

class Solution:
    def findSmallestInteger(self, a: List[int], v: int) -> int:
        c=[0]*v;[setitem(c,x%v,c[x%v]+1)for x in a];return(m:=min(c))*v+c.index(m)

class Solution:
    def findSmallestInteger(self, a: List[int], v: int) -> int:
        c=[0]*v;exec('for x in a:c[x%v]+=1');return(m:=min(c))*v+c.index(m)

test('''
2598. Smallest Missing Non-negative Integer After Operations
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums and an integer value.

In one operation, you can add or subtract value from any element of nums.

For example, if nums = [1,2,3] and value = 2, you can choose to subtract value from nums[0] to make nums = [-1,2,3].
The MEX (minimum excluded) of an array is the smallest missing non-negative integer in it.

For example, the MEX of [-1,2,3] is 0 while the MEX of [1,0,3] is 2.
Return the maximum MEX of nums after applying the mentioned operation any number of times.

 

Example 1:

Input: nums = [1,-10,7,13,6,8], value = 5
Output: 4
Explanation: One can achieve this result by applying the following operations:
- Add value to nums[1] twice to make nums = [1,0,7,13,6,8]
- Subtract value from nums[2] once to make nums = [1,0,2,13,6,8]
- Subtract value from nums[3] twice to make nums = [1,0,2,3,6,8]
The MEX of nums is 4. It can be shown that 4 is the maximum MEX we can achieve.
Example 2:

Input: nums = [1,-10,7,13,6,8], value = 7
Output: 2
Explanation: One can achieve this result by applying the following operation:
- subtract value from nums[2] once to make nums = [1,-10,0,13,6,8]
The MEX of nums is 2. It can be shown that 2 is the maximum MEX we can achieve.
 

Constraints:

1 <= nums.length, value <= 105
-109 <= nums[i] <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
21,716/53.4K
Acceptance Rate
40.6%
Topics
Array
Hash Table
Math
Greedy
Weekly Contest 337
icon
Companies
Hint 1
Think about using modular arithmetic.
Hint 2
if x = nums[i] (mod value), then we can make nums[i] equal to x after some number of operations
Hint 3
How does finding the frequency of (nums[i] mod value) help?
Similar Questions
First Missing Positive
Hard
''')
