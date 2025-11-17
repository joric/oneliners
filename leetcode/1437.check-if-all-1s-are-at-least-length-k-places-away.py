from lc import *

# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/?envType=daily-question&envId=2025-11-17

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        distance = k
        for num in nums:
            if num == 0:
                distance += 1
            else:
                if distance < k:
                    return False
                distance = 0
        return True

# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/solutions/610040/python-easy-solution-one-pass-by-foos-xia5/?envType=daily-question&envId=2025-11-17

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = None
        for i, val in enumerate(nums):
            if val == 1:
                if  last is not None and i - last - 1< k:
                    return False
                last = i
        return True

class Solution:
    def kLengthApart(self, a: List[int], k: int) -> bool:
        t=~k
        for i,x in enumerate(a):
            if x:
                if i-t<=k:
                    return False
                t = i
        return True

# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/solutions/5634564/python-one-line-solution-by-snah0902-i1qu/?envType=daily-question&envId=2025-11-17

class Solution:
    def kLengthApart(self, a: List[int], k: int) -> bool:
        return reduce(lambda x,y:(x[0]and y[0]-x[1]>k,y[0]),filter(lambda x:x[1]==1,enumerate(a)),(True,-k-1))[0]

# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/solutions/7202756/1-line-angry-solution-javascript-python-iqeli/?envType=daily-question&envId=2025-11-17

Solution=type('',(),{"kLengthApart":lambda s,n,k:(_:=-k-1)and not any(x and(i-_<=k or(_:=i)*0)for i,x in enumerate(n))})

class Solution:
    def kLengthApart(self, n: List[int], k: int) -> bool:
        t=~k;return not any(x and(i-t<=k or(t:=i)*0)for i,x in enumerate(n))

test('''
1437. Check If All 1's Are at Least Length K Places Away
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

 

Example 1:


Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:


Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
 

Constraints:

1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
113,145/186.7K
Acceptance Rate
60.6%
Topics
Array
Weekly Contest 187
icon
Companies
Hint 1
Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.
Similar Questions
Task Scheduler II
Medium
''')
