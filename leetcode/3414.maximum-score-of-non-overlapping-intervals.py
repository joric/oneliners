from lc import *

# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/solutions/6235677/happy-to-learn-the-cache-method-by-leoka-6ywo/?envType=daily-question&envId=2026-09-12

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        sorted_intervals = sorted((interval[1], interval[0], interval[2], i) for i, interval in enumerate(intervals))
        @cache
        def recursion(idx, k):
            if k == 0 or idx < 0:
                return 0, []
            end, start, weight, i = sorted_intervals[idx]
            prev_w, prev_picks = recursion(bisect.bisect_left(sorted_intervals, (start,)) - 1, k - 1)
            return max(recursion(idx-1, k), (weight + prev_w, sorted([-i] + prev_picks, reverse=True)))
        return [-i for i in recursion(len(sorted_intervals)-1, 4)[1]]

class Solution:
    def maximumWeight(self, a: List[List[int]]) -> List[int]:
        d=sorted([e,s,w,i]for i,(s,e,w)in enumerate(a));f=cache(lambda i,k:i*k>0and min(f(i-1,k),((t:=f(bisect_left(d,[(x:=d[i-1])[1]]),k-1))[0]-x[2],sorted([x[3]]+t[1])))or(0,[]));return f(len(a),4)[1]

class Solution:
    def maximumWeight(self, a: List[List[int]]) -> List[int]:
        n=0;d=sorted(v+[n:=n-1]for v in a);f=cache(lambda i,k:i*k and min(f(i+1,k),sorted([(t:=f(bisect_left(d,[(x:=d[i])[1]+1])+n,k-1))[0]-x[2],~x[3]]+t[1:]))or[0]);return f(n,4)[1:]

test('''
3414. Maximum Score of Non-overlapping Intervals
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array intervals, where intervals[i] = [li, ri, weighti]. Interval i starts at position li and ends at ri, and has a weight of weighti. You can choose up to 4 non-overlapping intervals. The score of the chosen intervals is defined as the total sum of their weights.

Return the lexicographically smallest array of at most 4 indices from intervals with maximum score, representing your choice of non-overlapping intervals.

Two intervals are said to be non-overlapping if they do not share any points. In particular, intervals sharing a left or right boundary are considered overlapping.

 

Example 1:

Input: intervals = [[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]]

Output: [2,3]

Explanation:

You can choose the intervals with indices 2, and 3 with respective weights of 5, and 3.

Example 2:

Input: intervals = [[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]]

Output: [1,3,5,6]

Explanation:

You can choose the intervals with indices 1, 3, 5, and 6 with respective weights of 7, 6, 3, and 5.

 

Constraints:

1 <= intevals.length <= 5 * 104
intervals[i].length == 3
intervals[i] = [li, ri, weighti]
1 <= li <= ri <= 109
1 <= weighti <= 109
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
14,397/28K
Acceptance Rate
51.4%
Topics
Senior Staff
Array
Binary Search
Dynamic Programming
Sorting
Weekly Contest 431
icon
Companies
Hint 1
Use Dynamic Programming.
Hint 2
Sort intervals by right boundary.
Hint 3
Let dp[r][i] denote the maximum score having picked r intervals from the prefix of intervals ending at index i.
Hint 4
dp[r][i] = max(dp[r][i - 1], intervals[i][2] + dp[r][j]) where j is the largest index such that intervals[j][1] < intervals[i][0].
Hint 5
Since intervals is sorted by right boundary, we can find index j using binary search.
Similar Questions
Two Best Non-Overlapping Events
Medium
''')
