from lc import *

# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/discuss/1390162/JavaC%2B%2BPython-Mono-Increasing-Stack

class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        d, r = [], []
        for e in o:
            i = bisect_right(d,e)
            r.append(i + 1)
            if i == len(d):
                d.append(0)
            d[i] = e
        return r

class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        return (d:=[],r:=[],[(i:=bisect_right(d,e),r.append(i+1),i==len(d) and d.append(0),setitem(d,i,e)) for e in o],r)[3]

# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/discuss/1390172/Python-6-lines-Use-Longest-Increasing-Subsequence-explained

class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        d, r = [10**10] * (len(o)+1), []
        for e in o:
            i = bisect_right(d,e)
            r += [i + 1]
            d[i] = e
        return r

class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        return (d:=[inf]*(len(o)+1),r:=[],[(i:=bisect_right(d,e),r.append(i+1),setitem(d,i,e)) for e in o],r)[3]

class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        d = []
        for e in o:
            i = bisect_right(d,e)
            d[i:i+1] = [e]
            yield i + 1

class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        return (d:=[])or[setitem(d,slice(i:=bisect_right(d,e),i+1),[e])or i+1 for e in o]

class Solution:
    def longestObstacleCourseAtEachPosition(self, o: List[int]) -> List[int]:
        d=[];return [setitem(d,slice(i:=bisect_right(d,e),i+1),[e])or i+1 for e in o]

test('''
1964. Find the Longest Valid Obstacle Course at Each Position
Hard

1082

38

Add to List

Share
You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n, where obstacles[i] describes the height of the ith obstacle.

For every index i between 0 and n - 1 (inclusive), find the length of the longest obstacle course in obstacles such that:

You choose any number of obstacles between 0 and i inclusive.
You must include the ith obstacle in the course.
You must put the chosen obstacles in the same order as they appear in obstacles.
Every obstacle (except the first) is taller than or the same height as the obstacle immediately before it.
Return an array ans of length n, where ans[i] is the length of the longest obstacle course for index i as described above.

 

Example 1:

Input: obstacles = [1,2,3,2]
Output: [1,2,3,3]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [1], [1] has length 1.
- i = 1: [1,2], [1,2] has length 2.
- i = 2: [1,2,3], [1,2,3] has length 3.
- i = 3: [1,2,3,2], [1,2,2] has length 3.
Example 2:

Input: obstacles = [2,2,1]
Output: [1,2,1]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [2], [2] has length 1.
- i = 1: [2,2], [2,2] has length 2.
- i = 2: [2,2,1], [1] has length 1.
Example 3:

Input: obstacles = [3,1,5,6,4,2]
Output: [1,1,2,3,2,2]
Explanation: The longest valid obstacle course at each position is:
- i = 0: [3], [3] has length 1.
- i = 1: [3,1], [1] has length 1.
- i = 2: [3,1,5], [3,5] has length 2. [1,5] is also valid.
- i = 3: [3,1,5,6], [3,5,6] has length 3. [1,5,6] is also valid.
- i = 4: [3,1,5,6,4], [3,4] has length 2. [1,4] is also valid.
- i = 5: [3,1,5,6,4,2], [1,2] has length 2.
 

Constraints:

n == obstacles.length
1 <= n <= 105
1 <= obstacles[i] <= 107
Accepted
28,926
Submissions
48,448
Seen this question in a real interview before?

Yes

No
Can you keep track of the minimum height for each obstacle course length?
You can use binary search to find the longest previous obstacle course length that satisfies the conditions.
''')

