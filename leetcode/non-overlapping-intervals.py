from lc import *

# https://leetcode.com/problems/non-overlapping-intervals/discuss/91721/Short-Ruby-and-Python

class Solution:
    def eraseOverlapIntervals(self, v: List[List[int]]) -> int:
        e = -inf
        r = 0
        for i in sorted(v,key=itemgetter(1)):
            if i[0] >= e:
                e = i[1]
            else:
                r += 1
        return r

class Solution:
    def eraseOverlapIntervals(self, v: List[List[int]]) -> int:
        return len(v)-reduce(lambda r,i:i[0]<r[1]and r or(r[0]+1,i[1]),sorted(v,key=itemgetter(1)),(0,-inf))[0]

class Solution:
    def eraseOverlapIntervals(self, v: List[List[int]]) -> int:
        e,r=-inf,0;[a<e and(r:=r+1)or(e:=b)for a,b in sorted(v,key=itemgetter(1))];return r

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

