from lc import *

# https://leetcode.com/problems/two-best-non-overlapping-events/discuss/4185733/One-Line-Solution

class Solution:
    def maxTwoEvents(self, a: List[List[int]]) -> int:
        return max((M:=[*accumulate(map(itemgetter(2),(a:=sorted(a))[::-1]),max)][::-1])+[(j:=bisect_right(a,e,key=itemgetter(0)))<len(a) and v+M[j] for s,e,v in a])

class Solution:
    def maxTwoEvents(self, A: List[List[int]]) -> int:
        S,E,V=zip(*(A:=sorted(A)));M=[*accumulate(V[::-1],max)][::-1];return max(M[:1]+[(j:=bisect_right(S,e))<len(A) and v+M[j] for s,e,v in A])

class Solution:
    def maxTwoEvents(self, a: List[List[int]]) -> int:
        a.sort();b,_,t=zip(*a);t=[*accumulate(t[::-1],max)][::-1];return max(t[:1]+[(j:=bisect_right(b,e))<len(a)and v+t[j]for _,e,v in a])

test('''
2054. Two Best Non-Overlapping Events
Medium

913

35

Add to List

Share
You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

 

Example 1:


Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
Example 2:

Example 1 Diagram
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.
Example 3:


Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 

Constraints:

2 <= events.length <= 105
events[i].length == 3
1 <= startTimei <= endTimei <= 109
1 <= valuei <= 106
Accepted
28,687
Submissions
55,948
''')
