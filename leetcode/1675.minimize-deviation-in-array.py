from lc import *

# https://leetcode.com/problems/minimize-deviation-in-array

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        r,q = inf,[]
        for a in nums:
            heappush(q,a%2 and -a*2 or -a)
        m = -max(q)
        while len(q) == len(nums):
            a = -heappop(q)
            r = min(r, a - m)
            if a%2==0:
                m = min(m, a//2)
                heappush(q, -a//2)
        return r

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        return next((r for _ in count() if not(len(q)==len(nums) and (a:=-heappop(q),r:=min(r,a-m),a%2==0 and (m:=min(m,a//2),heappush(q,-a//2))))),(r:=inf,q:=[],[heappush(q,a%2 and -a*2 or -a) for a in nums],m:=-max(q)))

from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        s,r = SortedList(i*2 if i & 1 else i for i in nums), 10**9
        while True:
            r = min(r,s[-1]-s[0])
            if 1&s[-1]: break
            s.add(s.pop()//2)
        return r

class Solution:
    def minimumDeviation(self, a: List[int]) -> int:
        s,r=__import__('sortedcontainers').SortedList(i*(1+i%2)for i in a),inf;return next(r for _ in count()if[r:=min(r,s[-1]-s[0])]and 1&s[-1]or s.add(s.pop()//2))

test('''
1675. Minimize Deviation in Array
Hard

1708

88

Add to List

Share
You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

If the element is even, divide it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].
If the element is odd, multiply it by 2.
For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].
The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 1
Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2], then the deviation will be 3 - 2 = 1.
Example 2:

Input: nums = [4,1,5,20,3]
Output: 3
Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
Example 3:

Input: nums = [2,10,8]
Output: 3
 

Constraints:

n == nums.length
2 <= n <= 5 * 10^4
1 <= nums[i] <= 10^9
''')
