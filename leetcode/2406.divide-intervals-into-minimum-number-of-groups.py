from lc import *

# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/discuss/2560101/JavaC%2B%2BPython-Meeting-Room

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        r = []
        for a,b in intervals:
            r.append([a, 1])
            r.append([b + 1, -1])
        res = cur = 0
        for a, diff in sorted(r):
            cur += diff
            res = max(res, cur)
        return res

# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/discuss/2581298/Python3-oror-5-lines-dict-accumulate-oror-TS%3A-62-21

class Solution:
    def minGroups(self, v: List[List[int]]) -> int:
        c = Counter()
        for a,b in v:
            c[a] += 1
            c[b+1] -= 1
        return max(accumulate(c[n]for n in sorted(c)))

class Solution:
    def minGroups(self, v: List[List[int]]) -> int:
        c=Counter();[c.update([a])or c.update({b+1:-1})for a,b in v];return max(accumulate(c[n]for n in sorted(c)))

# updated 2024-10-12 (POTD)

class Solution:
    def minGroups(self, v: List[List[int]]) -> int:
        c=Counter();[c.update({a:1,b+1:-1})for a,b in v];return max(accumulate(c[k]for k in sorted(c)))

class Solution:
    def minGroups(self, v: List[List[int]]) -> int:
        c,a=Counter(),0;[c.update({a:1,b+1:-1})for a,b in v];return max(a:=a+c[k]for k in sorted(c))

# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/discuss/3900475/Min-heap-very-short-code

class Solution:
    def minGroups(self, v: List[List[int]]) -> int:
        v.sort()
        h = []
        for a,b in v:
            if h and a > h[0]:
                heappop(h)
            heappush(h,b)
        return len(h)

class Solution:
    def minGroups(self, v: List[List[int]]) -> int:
        v.sort();h=[];[(h and a>h[0]and heappop(h),heappush(h,b))for a,b in v];return len(h)

class Solution:
    def minGroups(self, v: List[List[int]]) -> int:
        v.sort();h=[];[heappush(h,b)or h and a>h[0]and heappop(h)for a,b in v];return len(h)

class Solution:
    def minGroups(self, v: List[List[int]]) -> int:
        v.sort();h=[];[heappush(h,b)or[a]>h[:1]and heappop(h)for a,b in v];return len(h)

test('''
2406. Divide Intervals Into Minimum Number of Groups
Medium

791

11

Add to List

Share
You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.

 

Example 1:

Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
Example 2:

Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
Explanation: None of the intervals overlap, so we can put all of them in one group.
 

Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 106
Accepted
28,871
Submissions
60,389
''')
