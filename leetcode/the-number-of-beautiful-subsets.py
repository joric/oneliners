from lc import *

# https://leetcode.com/problems/the-number-of-beautiful-subsets/discuss/3314361/Python-House-Robber-O(n)

class Solution:
    def beautifulSubsets(self, n: List[int], k: int) -> int:
        c = Counter(n)
        def f(x):
            a,b = f(x-k) if x-k in c else(1,0)
            return a+b,a*~-(1<<c[x])
        return reduce(mul,(sum(f(x))for x in c if not c[x+k]))-1

class Solution:
    def beautifulSubsets(self, n: List[int], k: int) -> int:
        c=Counter(n);f=lambda x:(sum(p:=f(x-k)if x-k in c else(1,0)),p[0]*~-(1<<c[x]));return reduce(mul,(sum(f(x))for x in c if not c[x+k]))-1

test('''
2597. The Number of Beautiful Subsets
Medium

532

112

Add to List

Share
You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

 

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].
 

Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000
Accepted
24,185
Submissions
69,996
''')
