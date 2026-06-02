from lc import *

# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/solutions/7036614/simple-5-lines-code-by-silvia42-c2gm/?envType=daily-question&envId=2026-06-03

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        time1=min([a+b for a,b in zip(landStartTime,landDuration)])
        time1=min([max(time1,a)+b for a,b in zip(waterStartTime,waterDuration)])
        time2=min([a+b for a,b in zip(waterStartTime,waterDuration)])
        time2=min([max(time2,a)+b  for a,b in zip(landStartTime,landDuration)])
        return min(time1,time2)      

class Solution:
    def earliestFinishTime(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        return min(min(max(min(x+y for x,y in zip(a,b)),x)+y for x,y in zip(c,d)), min(max(min(x+y for x,y in zip(c,d)),x)+y for x,y in zip(a,b)))

class Solution:
    def earliestFinishTime(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        return min(min(max(min(map(sum,zip(*k[:2]))),x)+y for x,y in zip(*k[2:]))for k in((a,b,c,d),(c,d,a,b)))

class Solution:
    def earliestFinishTime(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        u,v=min(x+y for x,y in zip(a,b)),min(x+y for x,y in zip(c,d));return min(min(max(u,x)+y for x,y in zip(c,d)),min(max(v,x)+y for x,y in zip(a,b)))

class Solution:
    def earliestFinishTime(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        return min(max(t,x)+y for k in((a,b,c,d),(c,d,a,b))for t in[min(map(add,*k[:2]))]for x,y in zip(*k[2:]))

#TLE
class Solution:
    def earliestFinishTime(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        return min(y+max(min(map(add,*k[:2])),x)for k in((a,b,c,d),(c,d,a,b))for x,y in zip(*k[2:]))

class Solution:
    def earliestFinishTime(self, a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
        return min(y+max(t,x)for t,p,q in((min(map(add,a,b)),c,d),(min(map(add,c,d)),a,b))for x,y in zip(p,q))

test('''
3635. Earliest Finish Time for Land and Water Rides II
Medium
Topics
premium lock icon
Companies
Hint
You are given two categories of theme park attractions: land rides and water rides.

Land rides
landStartTime[i] – the earliest time the ith land ride can be boarded.
landDuration[i] – how long the ith land ride lasts.
Water rides
waterStartTime[j] – the earliest time the jth water ride can be boarded.
waterDuration[j] – how long the jth water ride lasts.
A tourist must experience exactly one ride from each category, in either order.

A ride may be started at its opening time or any later moment.
If a ride is started at time t, it finishes at time t + duration.
Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.
Return the earliest possible time at which the tourist can finish both rides.

 

Example 1:

Input: landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]

Output: 9

Explanation:​​​​​​​

Plan A (land ride 0 → water ride 0):
Start land ride 0 at time landStartTime[0] = 2. Finish at 2 + landDuration[0] = 6.
Water ride 0 opens at time waterStartTime[0] = 6. Start immediately at 6, finish at 6 + waterDuration[0] = 9.
Plan B (water ride 0 → land ride 1):
Start water ride 0 at time waterStartTime[0] = 6. Finish at 6 + waterDuration[0] = 9.
Land ride 1 opens at landStartTime[1] = 8. Start at time 9, finish at 9 + landDuration[1] = 10.
Plan C (land ride 1 → water ride 0):
Start land ride 1 at time landStartTime[1] = 8. Finish at 8 + landDuration[1] = 9.
Water ride 0 opened at waterStartTime[0] = 6. Start at time 9, finish at 9 + waterDuration[0] = 12.
Plan D (water ride 0 → land ride 0):
Start water ride 0 at time waterStartTime[0] = 6. Finish at 6 + waterDuration[0] = 9.
Land ride 0 opened at landStartTime[0] = 2. Start at time 9, finish at 9 + landDuration[0] = 13.
Plan A gives the earliest finish time of 9.

Example 2:

Input: landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]

Output: 14

Explanation:​​​​​​​

Plan A (water ride 0 → land ride 0):
Start water ride 0 at time waterStartTime[0] = 1. Finish at 1 + waterDuration[0] = 11.
Land ride 0 opened at landStartTime[0] = 5. Start immediately at 11 and finish at 11 + landDuration[0] = 14.
Plan B (land ride 0 → water ride 0):
Start land ride 0 at time landStartTime[0] = 5. Finish at 5 + landDuration[0] = 8.
Water ride 0 opened at waterStartTime[0] = 1. Start immediately at 8 and finish at 8 + waterDuration[0] = 18.
Plan A provides the earliest finish time of 14.​​​​​​​

 

Constraints:

1 <= n, m <= 5 * 104
landStartTime.length == landDuration.length == n
waterStartTime.length == waterDuration.length == m
1 <= landStartTime[i], landDuration[i], waterStartTime[j], waterDuration[j] <= 105
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
16,142/41.3K
Acceptance Rate
39.1%
Topics
Staff
Array
Two Pointers
Binary Search
Greedy
Sorting
Biweekly Contest 162
icon
Companies
Hint 1
Sort each ride list by opening time and build a prefix minimum of ride durations and a suffix minimum of ride finish times (start + duration).
Hint 2
Try both orders, land then water and water then land. For each ride in the first list compute finish1 = start1 + duration1.
Hint 3
Binary‑search the second list (sorted by start) to split rides into those with start <= finish1 and those with start > finish1. Use the prefix minimum duration on the early group to get an earliest finish of finish1 + minDuration and the suffix minimum finish time on the late group.
Hint 4
For each pairing take the smaller finish time and track the overall minimum.
''')
