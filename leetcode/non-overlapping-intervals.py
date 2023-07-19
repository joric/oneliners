from lc import *

# https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        r,e = 0,-inf
        for a,b in sorted(intervals,key=itemgetter(1)):
            if a<e:
                r += 1
            else:
                e = b
        return r

class Solution:
    def eraseOverlapIntervals(self, i: List[List[int]]) -> int:
        r,e=0,-inf;[a<e and(r:=r+1)or(e:=b)for a,b in sorted(i,key=itemgetter(1))];return r

test('''
435. Non-overlapping Intervals
Medium

6088

164

Add to List

Share
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4
''')

