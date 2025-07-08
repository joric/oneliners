from lc import *

# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/discuss/2204293/Python.-Recursion-%2B-LRU-Cache-%2B-Binary-Search...-3-lines-only...

# POTD 2025-07-08

class Solution:
    def maxValue(self, e: List[List[int]], k: int) -> int:
        e.sort();return(f:=cache(lambda i,k:i<len(e)and k and max(f(i+1,k),e[i][2]+f(bisect_left(e,[e[i][1]+1]),k-1))))(0,k)

test('''
1751. Maximum Number of Events That Can Be Attended II
Hard

871

14

Add to List

Share
You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

 

Example 1:



Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:



Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
Example 3:



Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
 

Example 4:
Input: events = [[1,3,4],[2,4,1],[1,1,4],[3,5,1],[2,5,5]], k = 3
Output: 9

Constraints:

1 <= k <= events.length
1 <= k * events.length <= 10^6
1 <= startDayi <= endDayi <= 10^9
1 <= valuei <= 10^6
''')
