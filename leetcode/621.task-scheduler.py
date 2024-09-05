from lc import *

# https://leetcode.com/problems/task-scheduler/discuss/4894988/One-line-solution

class Solution:
    def leastInterval(self, t: List[str], n: int) -> int:
        v=Counter(t).values();return max(len(t),[*v].count(m:=max(v))+(m-1)*(n+1))

class Solution:
    def leastInterval(self, t: List[str], n: int) -> int:
        m=max(v:=Counter(t).values());return max(len(t),[*v].count(m)+~-m*-~n)

# https://leetcode.com/problems/task-scheduler/discuss/4894970/Python-3-oror-3-lines-Counter-oror-TS%3A-99-93

class Solution:
    def leastInterval(self, t: List[str], n: int) -> int:
        v=Counter(t).values();c=Counter(v)[m:=max(v)];return max(len(t),c+(m-1)*(n+1))

class Solution:
    def leastInterval(self, t: List[str], n: int) -> int:
        return max(len(t),(f:=Counter)(v:=f(t).values())[m:=max(v)]-~-m*~n)

test('''
621. Task Scheduler
Medium

9447

1963

Add to List

Share
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
Accepted
519,849
Submissions
890,280
''')