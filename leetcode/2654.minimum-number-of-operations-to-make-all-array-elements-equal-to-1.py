from lc import *

# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/solutions/6737518/three-simple-lines-of-code-by-mikposp/

class Solution:
    def minOperations(self, a: List[int]) -> int:
        n = len(a)
        if q:=a.count(1): return n-q
        return next((w+n-2 for w in range(n+1) for i in range(n-w+1) if gcd(*a[i:i+w])==1),-1)

class Solution:
    def minOperations(self, a: List[int]) -> int:
        n = len(a)
        if q:=a.count(1): return n-q
        return min((j-i+n-2 for i,j in combinations(range(n+1),2) if gcd(*a[i:j])==1),default=-1)

class Solution:
    def minOperations(self, a: List[int]) -> int:
        n,q=len(a),a.count(1);return n-q if q else min((j-i+n-2 for i,j in combinations(range(n+1),2)if gcd(*a[i:j])==1),default=-1)

class Solution:
    def minOperations(self, a: List[int]) -> int:
        n=len(a);return n-q if(q:=a.count(1))else next((w+n-2 for w in range(n+1)for i in range(n-w+1)if gcd(*a[i:i+w])==1),-1)

class Solution:
    def minOperations(self, a: List[int]) -> int:
        n=len(a);return n-q if(q:=a.count(1))else next((w+n-2 for w in range(n+1)for i in range(n-w+1)if gcd(*a[i:i+w])==1),-1)

test('''
2654. Minimum Number of Operations to Make All Array Elements Equal to 1
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array nums consisiting of positive integers. You can do the following operation on the array any number of times:

Select an index i such that 0 <= i < n - 1 and replace either of nums[i] or nums[i+1] with their gcd value.
Return the minimum number of operations to make all elements of nums equal to 1. If it is impossible, return -1.

The gcd of two integers is the greatest common divisor of the two integers.

 

Example 1:

Input: nums = [2,6,3,4]
Output: 4
Explanation: We can do the following operations:
- Choose index i = 2 and replace nums[2] with gcd(3,4) = 1. Now we have nums = [2,6,1,4].
- Choose index i = 1 and replace nums[1] with gcd(6,1) = 1. Now we have nums = [2,1,1,4].
- Choose index i = 0 and replace nums[0] with gcd(2,1) = 1. Now we have nums = [1,1,1,4].
- Choose index i = 2 and replace nums[3] with gcd(1,4) = 1. Now we have nums = [1,1,1,1].
Example 2:

Input: nums = [2,10,6,14]
Output: -1
Explanation: It can be shown that it is impossible to make all the elements equal to 1.

Other examples:

Input: nums = [1,1]
Output: 0

Constraints:

2 <= nums.length <= 50
1 <= nums[i] <= 106
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
15,185/44.5K
Acceptance Rate
34.1%
Topics
Array
Math
Number Theory
Weekly Contest 342
icon
Companies
Hint 1
Note that if you have at least one occurrence of 1 in the array, then you can make all the other elements equal to 1 with one operation each.
Hint 2
''')
