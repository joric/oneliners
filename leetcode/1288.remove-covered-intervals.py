from lc import *

# https://leetcode.com/problems/remove-covered-intervals/solutions/452956/python-3-six-lines-by-junaidmansuri-dh5r/?envType=daily-question&envId=2026-07-06

class Solution:
    def removeCoveredIntervals(self, v: List[List[int]]) -> int:
        t = 0
        for a,b in v:
            for x,y in v:
                if x<=a and b<=y and(a,b)!=(x,y):
                    break
            else:
                t += 1
        return t

# https://leetcode.com/problems/remove-covered-intervals

class Solution:
    def removeCoveredIntervals(self, v: List[List[int]]) -> int:
        r = t = 0
        for i,j in sorted(v,key=lambda p:(p[0],-p[1])):
            r += j>t
            t = max(t,j)
        return r

# https://leetcode.com/problems/remove-covered-intervals/solutions/1784520/python3-sorting-explained-by-artod-7wsm/?envType=daily-question&envId=2026-07-06

class Solution:
    def removeCoveredIntervals(self, v: List[List[int]]) -> int:
        r, t = len(v), 0
        for _,e in sorted(v, key=lambda p:(p[0],-p[1])):
            if e <= t:
                r -= 1
            else:
                t = e
        return r

class Solution:
    def removeCoveredIntervals(self, v: List[List[int]]) -> int:
        return sum(all(y[0]>x[0]or x[1]>y[1]or x==y for y in v)for x in v)

class Solution:
    def removeCoveredIntervals(self, v: List[List[int]]) -> int:
        return sum(all(a<c or d<b or(a,b)==(c,d)for c,d in v)for a,b in v)

class Solution:
    def removeCoveredIntervals(self, v: List[List[int]]) -> int:
        return sum(2>sum(c<=a<=b<=d for c,d in v)for a,b in v)

test('''
1288. Remove Covered Intervals
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1

Other examples:

Input: intervals = [[3,10],[4,10],[5,11]]
Output: 2

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li < ri <= 105
All the given intervals are unique.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
145,965/260.4K
Acceptance Rate
56.0%
Topics
Senior
Array
Sorting
Biweekly Contest 15
icon
Companies
Hint 1
How to check if an interval is covered by another?
Hint 2
Compare each interval to all others and check if it is covered by any interval.
''')
