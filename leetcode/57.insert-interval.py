from lc import *

class Solution:
    def insert(self, a: List[List[int]], x: List[int]) -> List[List[int]]:
        i, j, found = 0, -1, False
        for i, y in enumerate(a):
            if y[1] < x[0]:
                j = i
            elif y[0] > x[1]:
                found = True
                break
            else:
                x = [min(x[0], y[0]), max(x[1], y[1])]
        return a[:j+1] + [x] + (a[i:] if found else [])

# https://leetcode.com/problems/insert-interval/discuss/2544360/Python%3A-Just-add-one-line-to-the-solution-of-Merge-Interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval) # just 1 extra line different from 56. merge intervals
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])
        return output

class Solution:
    def insert(self, v: List[List[int]], w: List[int]) -> List[List[int]]:
        return (v.append(w),v.sort(key=lambda x: x[0]),o:=[v[0]],[setitem(o[-1],1,max(o[-1][1], v[i][1])) if v[i][0]<=o[-1][1] else o.append(v[i]) for i in range(1,len(v))]) and o


class Solution:
    def insert(self, v: List[List[int]], w: List[int]) -> List[List[int]]:
        v.append(w)
        res = []
        v.sort()
        for x in v:
            if res and x[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], x[1])
            else:
                res.append(x)
        return res

# updated 2024-03-17

class Solution:
    def insert(self, v: List[List[int]], w: List[int]) -> List[List[int]]:
        return(v.append(w),v.sort(),o:=[],[setitem(o[-1],1,max(o[-1][1], x[1]))if o and x[0]<=o[-1][1]else o.append(x)for x in v])and o

# https://leetcode.com/problems/insert-interval/discuss/3056513/Python-One-Line

class Solution:
    def insert(self, v: List[List[int]], w: List[int]) -> List[List[int]]:
        return reduce(lambda r,x:r[:-1]+[[r[-1][0],max(r[-1][1],x[1])]]if r and x[0]<=r[-1][1]else r+[x],sorted(v+[w]),[])

class Solution:
    def insert(self, v: List[List[int]], w: List[int]) -> List[List[int]]:
        r = []
        for s,e in sorted(v+[w]):
            if r and r[-1][1] >= s:
                r[-1][1]=max(r[-1][1],e)
            else:
                r.append([s,e])
        return r

class Solution:
    def insert(self, v: List[List[int]], w: List[int]) -> List[List[int]]:
        r=[];[setitem(r[-1],1,max(r[-1][1],e))if r and s<=r[-1][1]else r.append([s,e])for s,e in sorted(v+[w])];return r

class Solution:
    def insert(self, v: List[List[int]], w: List[int]) -> List[List[int]]:
        r=[];[setitem(r[-1],1,max(r[-1][1],e))if r and s<=r[-1][1]else r.append([s,e])for s,e in sorted(v+[w])];return r

class Solution:
    def insert(self, v: List[List[int]], w: List[int]) -> List[List[int]]:
        r=[];[setitem(r[-1],1,max(r[-1][1],e))if r and s<=r[-1][1]else(r:=r+[[s,e]])for s,e in sorted(v+[w])];return r

test('''
57. Insert Interval
Medium

6587

469

Add to List

Share
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5

''')
