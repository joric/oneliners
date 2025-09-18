from lc import *

# https://leetcode.com/problems/design-task-manager/solutions/7202690/19-lines-of-python-code-beats-100-0ms-o-n-log-n/?envType=daily-question&envId=2025-09-18

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.heap, self.taskPriority, self.taskOwner = [], {}, {}
        for u, t, p in tasks: self.add(u, t, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.heap, (-priority, -taskId))
        self.taskPriority[taskId], self.taskOwner[taskId] = priority, userId

    def edit(self, taskId: int, newPriority: int) -> None:
        heapq.heappush(self.heap, (-newPriority, -taskId))
        self.taskPriority[taskId] = newPriority

    def rmv(self, taskId: int) -> None:
        self.taskPriority[taskId] = -1

    def execTop(self) -> int:
        while self.heap:
            p, tid = map(lambda x: -x, heapq.heappop(self.heap))
            if self.taskPriority.get(tid, -2) == p:
                self.taskPriority[tid] = -1
                return self.taskOwner.get(tid, -1)
        return -1

class TaskManager:
    def __init__(s, t: List[List[int]]):
        s.h, s.p, s.o = [], {}, {}
        [s.add(u,i,r)for u,i,r in t]

    def add(s, u: int, i: int, r: int) -> None:
        heappush(s.h,(-r,-i))or setitem(s.p,i,r)or setitem(s.o,i,u)

    def edit(s, i: int, r: int) -> None:
        heappush(s.h,(-r,-i))or setitem(s.p,i,r)

    def rmv(s, i: int) -> None:
        s.p[i] = -1

    def execTop(s) -> int:
        return next((s.o.get(i,-1)for r, i in iter(lambda:tuple(map(lambda x:-x,heappop(s.h)))if s.h else 0,0)if s.p.get(i,-2)==r and not setitem(s.p,i,-1)),-1)

class TaskManager:
    def __init__(s, t: List[List[int]]):
        setattr(s,'h',[])or setattr(s,'p',{})or setattr(s,'o',{})or[s.add(u,i,r)for u,i,r in t]

    def add(s, u: int, i: int, r: int) -> None:
        heappush(s.h,(-r,-i))or setitem(s.p,i,r)or setitem(s.o,i,u)

    def edit(s, i: int, r: int) -> None:
        heappush(s.h,(-r,-i))or setitem(s.p,i,r)

    def rmv(s, i: int) -> None:
        s.p[i] = -1

    def execTop(s) -> int:
        return next((s.o.get(i,-1)for r, i in iter(lambda:tuple(map(lambda x:-x,heappop(s.h)))if s.h else 0,0)if s.p.get(i,-2)==r and not setitem(s.p,i,-1)),-1)

TaskManager=type('',(),{
    '__init__':lambda s,t:setattr(s,'h',[])or setattr(s,'p',{})or setattr(s,'o',{})or[s.add(u,i,r)for u,i,r in t]and None, 
    'add':lambda s,u,i,r:heappush(s.h,(-r,-i))or setitem(s.p,i,r)or setitem(s.o,i,u),
    'edit':lambda s,i,r:heappush(s.h,(-r,-i))or setitem(s.p,i,r),
    'rmv':lambda s,i:setitem(s.p,i,-1),
    'execTop':lambda s:next((s.o.get(i,-1)for r,i in iter(lambda:tuple(map(lambda x:-x,heappop(s.h)))if s.h else 0,0)if r==s.p.get(i,-2)and not setitem(s.p,i,-1)),-1)
})

test('''
3408. Design Task Manager
Solved
Medium
Topics
premium lock icon
Companies
There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

Implement the TaskManager class:

TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

Note that a user may be assigned multiple tasks.

 

Example 1:

Input:
["TaskManager", "add", "edit", "execTop", "rmv", "add", "execTop"]
[[[[1, 101, 10], [2, 102, 20], [3, 103, 15]]], [4, 104, 5], [102, 8], [], [101], [5, 105, 15], []]

Output:
[null, null, null, 3, null, null, 5]

Explanation

TaskManager taskManager = new TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]]); // Initializes with three tasks for Users 1, 2, and 3.
taskManager.add(4, 104, 5); // Adds task 104 with priority 5 for User 4.
taskManager.edit(102, 8); // Updates priority of task 102 to 8.
taskManager.execTop(); // return 3. Executes task 103 for User 3.
taskManager.rmv(101); // Removes task 101 from the system.
taskManager.add(5, 105, 15); // Adds task 105 with priority 15 for User 5.
taskManager.execTop(); // return 5. Executes task 105 for User 5.
 

Constraints:

1 <= tasks.length <= 105
0 <= userId <= 105
0 <= taskId <= 105
0 <= priority <= 109
0 <= newPriority <= 109
At most 2 * 105 calls will be made in total to add, edit, rmv, and execTop methods.
The input is generated such that taskId will be valid.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
58,460/123.5K
Acceptance Rate
47.3%
Topics
Hash Table
Design
Heap (Priority Queue)
Ordered Set
Biweekly Contest 147
icon
Companies
''',TaskManager)
