from lc import *

# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/solutions/1635083/pythoncjava-one-pass-dp-on-detailed-expl-usrt/

class Solution:
    def getDescentPeriods(self, p: List[int]) -> int:
        r = t = 1
        for i in range(1,len(p)):
            if p[i]==p[i-1]-1:
                t = t + 1
            else:
                t = 1
            r = r + t
        return r

# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/solutions/7406720/one-line-solution-by-mikposp-lmzf/

class Solution:
    def getDescentPeriods(self, a: List[int]) -> int:
        return sum(comb(sum(g)+1,2) for p,g in groupby(map(sub,a,a[1:])) if p==1)+len(a)

class Solution:
    def getDescentPeriods(self, a: List[int]) -> int:
        return sum(accumulate(starmap(sub,pairwise(a)),lambda q,p:q*(p==1)+1,initial=1))

class Solution:
    def getDescentPeriods(self, a: List[int]) -> int:
        return sum(accumulate([1,*map(sub,a,a[1:])],lambda q,p:q*(p==1)+1))

class Solution:
    def getDescentPeriods(self, a: List[int]) -> int:
        q=0;return sum(q:=1+q*(p==1)for p in[1,*map(sub,a,a[1:])])

class Solution:
    def getDescentPeriods(self, a: List[int]) -> int:
        q=1;return-~sum(q:=1+q*(p==1)for p in map(sub,a,a[1:]))

class Solution:
    def getDescentPeriods(self, a: List[int]) -> int:
        q=1;return-~sum(q:=1+q*(x-y==1)for x,y in pairwise(a))

test('''
2110. Number of Smooth Descent Periods of a Stock
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array prices representing the daily price history of a stock, where prices[i] is the stock price on the ith day.

A smooth descent period of a stock consists of one or more contiguous days such that the price on each day is lower than the price on the preceding day by exactly 1. The first day of the period is exempted from this rule.

Return the number of smooth descent periods.

 

Example 1:

Input: prices = [3,2,1,4]
Output: 7
Explanation: There are 7 smooth descent periods:
[3], [2], [1], [4], [3,2], [2,1], and [3,2,1]
Note that a period with one day is a smooth descent period by the definition.
Example 2:

Input: prices = [8,6,7,7]
Output: 4
Explanation: There are 4 smooth descent periods: [8], [6], [7], and [7]
Note that [8,6] is not a smooth descent period as 8 - 6 ≠ 1.
Example 3:

Input: prices = [1]
Output: 1
Explanation: There is 1 smooth descent period: [1]
 

Constraints:

1 <= prices.length <= 105
1 <= prices[i] <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
59,578/94.8K
Acceptance Rate
62.9%
Topics
Array
Math
Dynamic Programming
Weekly Contest 272
icon
Companies
Hint 1
Any array is a series of adjacent longest possible smooth descent periods. For example, [5,3,2,1,7,6] is [5] + [3,2,1] + [7,6].
Hint 2
Think of a 2-pointer approach to traverse the array and find each longest possible period.
Hint 3
Suppose you found the longest possible period with a length of k. How many periods are within that period? How can you count them quickly? Think of the formula to calculate the sum of 1, 2, 3, ..., k.
Similar Questions
Subarray Product Less Than K
Medium
Number of Valid Subarrays
Hard
Number of Zero-Filled Subarrays
Medium
''')
