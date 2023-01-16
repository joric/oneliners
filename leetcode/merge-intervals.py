from lc import *

class Solution:
    def merge(self, v: List[List[int]]) -> List[List[int]]:
        res = []
        v.sort()
        for x in v:
            if res and x[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], x[1])
            else:
                res.append(x)
        return res


class Solution:
    def merge(self, v: List[List[int]]) -> List[List[int]]:
        return (v.sort(),o:=[],[o[-1].__setitem__(1,max(o[-1][1], x[1])) if o and x[0]<=o[-1][1] else o.append(x) for x in v]) and o


test('''
56. Merge Intervals
Medium

17646

615

Add to List

Share
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
''')
