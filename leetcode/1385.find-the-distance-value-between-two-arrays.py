from lc import *

# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/solutions/844558/python-one-line-by-mokar2001-sqia/?envType=daily-question&envId=2026-11-05

# scala: a.count(x=>b.forall(y=>(y-x).abs>d))

class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        return sum(d<min(abs(x-__import__('numpy').r_[b]))for x in a)

class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        import numpy as p;return sum(d<min(abs(x-p.r_[b]))for x in a)

class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        return sum(1-any(abs(i-j)<=d for j in b)for i in a)

class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        return sum(d<min(abs(x-y)for y in b)for x in a)

class Solution:
    def findTheDistanceValue(self, a: list[int], b: list[int], d: int) -> int:
        return sum(all(d<abs(x-y)for y in b)for x in a)

test('''
1385. Find the Distance Value Between Two Arrays
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
Example 2:

Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2
Example 3:

Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1
 

Constraints:

1 <= arr1.length, arr2.length <= 500
-1000 <= arr1[i], arr2[j] <= 1000
0 <= d <= 100
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
162,685/224.2K
Acceptance Rate
72.6%
Topics
Mid Level
Array
Two Pointers
Binary Search
Sorting
Biweekly Contest 22
icon
Companies
Hint 1
Sort 'arr2' and use binary search to get the closest element for each 'arr1[i]', it gives a time complexity of O(nlogn).
''')
