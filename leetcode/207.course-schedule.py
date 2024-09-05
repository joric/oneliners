from lc import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for x, y in prerequisites:
            pre[x].append(y)
        status = [0] * numCourses
        def canTake(i):
            if status[i] in {1, -1}:
                return status[i] == 1
            status[i] = -1
            if any(not canTake(j) for j in pre[i]):
                return False
            status[i] = 1
            return True
        return all(canTake(i) for i in range(numCourses))

# https://leetcode.com/problems/course-schedule/discuss/1763763/python-5-lines-solution

class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        g,c=defaultdict(list),Counter()
        [(c.update({b:1}),g[a].append(b))for a,b in p]
        t=[k for k in range(n)if c[k]<1]
        [c.update({k:-1})or c[k]==0 and t.append(k)for o in t for k in g[o]]
        return len(t)==n

class Solution:
    def canFinish(self, n: int, p: List[List[int]]) -> bool:
        g,c=defaultdict(list),Counter();[(c.update({b:1}),g[a].append(b))for a,b in p];t=[k for k in range(n)if c[k]<1];[c.update({k:-1})or c[k]==0 and t.append(k)for o in t for k in g[o]];return len(t)==n

test('''
207. Course Schedule
Medium

13950

556

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
''')