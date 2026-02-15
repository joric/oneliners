from lc import *

# https://leetcode.com/problems/rank-transform-of-an-array/discuss/489824/Python-set%2Bsorted%2Bdict-(and-SciPy)

class Solution:
    def arrayRankTransform(self, a: List[int]) -> List[int]:
        return map({x:i+1 for i,x in enumerate(sorted(set(a)))}.get,a)

class Solution:
    def arrayRankTransform(self, a: List[int]) -> List[int]:
        return __import__('scipy').stats.rankdata(a,'dense')

class Solution:
    def arrayRankTransform(self, a: List[int]) -> List[int]:
        return map(dict(zip(sorted({*a}),count(1))).get,a)

test('''
1331. Rank Transform of an Array
Easy

1710

90

Add to List

Share
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
 

Constraints:

0 <= arr.length <= 105
-109 <= arr[i] <= 109
Accepted
124,609
Submissions
198,633
''')
