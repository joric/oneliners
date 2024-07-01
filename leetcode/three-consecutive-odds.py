from lc import *

# https://leetcode.com/problems/three-consecutive-odds/discuss/825552/Python-one-line-solution

class Solution:
    def threeConsecutiveOdds(self, a: List[int]) -> bool:
        return any(1&a&b&c for a,b,c in zip(a,a[1:],a[2:]))

class Solution:
    def threeConsecutiveOdds(self, a: List[int]) -> bool:
        return'111'in''.join(str(1&x)for x in a)

test('''
1550. Three Consecutive Odds
Easy

799

71

Add to List

Share
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
Accepted
135,879
Submissions
204,217
''')
