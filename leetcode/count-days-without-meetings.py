from lc import *

# Q2 https://leetcode.com/contest/weekly-contest-400/
# https://leetcode.com/problems/count-days-without-meetings/

# https://leetcode.com/problems/count-days-without-meetings/discuss/5245937/Python-one-line

class Solution:
    def countDays(self, d: int, m: List[List[int]]) -> int:
        return d-sum(b-a+1 for a,b in reduce(lambda m,c:m[:-1]+[[m[-1][0],max(m[-1][1],c[1])]]if m and m[-1][0]<=c[0]<=m[-1][1]else m+[c],sorted(m),[]))

test('''
3169. Count Days Without Meetings
Medium

153

4

Add to List

Share
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

 

Example 1:

Input: days = 10, meetings = [[5,7],[1,3],[9,10]]

Output: 2

Explanation:

There is no meeting scheduled on the 4th and 8th days.

Example 2:

Input: days = 5, meetings = [[2,4],[1,3]]

Output: 1

Explanation:

There is no meeting scheduled on the 5th day.

Example 3:

Input: days = 6, meetings = [[1,6]]

Output: 0

Explanation:

Meetings are scheduled for all working days.

 

Constraints:

1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days
Accepted
31,314
Submissions
95,602
''')
