from lc import *

# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/solutions/944473/javacpython-sort-and-some-story-by-lee21-0hjg/?envType=daily-question&envId=2026-05-12

class Solution:
    def minimumEffort(self, t: List[List[int]]) -> int:
        t.sort(key=lambda a: a[1] - a[0])
        res = 0
        for a,m in t:
            res = max(res + a, m)
        return res

# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/solutions/5031164/one-liner-by-yoongyeom-z89d/?envType=daily-question&envId=2026-05-12

class Solution:
    def minimumEffort(self, t: List[List[int]]) -> int:
        return reduce(lambda x,y:max(x,y[0])+y[1],sorted((t[i][1]-t[i][0],t[i][0]) for i in range(len(t))),0)

# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/solutions/1725589/python-1-line-solution-by-mwk0408-b48k/?envType=daily-question&envId=2026-05-12

class Solution:
    def minimumEffort(self, t: List[List[int]]) -> int:
        t.sort(key=lambda x:sub(*x));return bisect_left(range(10**10),1,key=lambda m:all(m>=b and[m:=m-a]for a,b in t))

class Solution:
    def minimumEffort(self, t: List[List[int]]) -> int:
        return[*accumulate(sorted(t,key=lambda x:(x[1]-x[0])),lambda p,x:max(p+x[0],x[1]),initial=0)][-1]

class Solution:
    def minimumEffort(self, t: List[List[int]]) -> int:
        return reduce(lambda r,x:max(r+x[0],x[1]),sorted(t,key=lambda x:x[1]-x[0]),0)

class Solution:
    def minimumEffort(self, t: List[List[int]]) -> int:
        return reduce(lambda r,x:max(r+x[0],x[1]),sorted(t,key=lambda x:-sub(*x)),0)

class Solution:
    def minimumEffort(self, t: List[List[int]]) -> int:
        r=0;[r:=max(r+a,b)for a,b in sorted(t,key=lambda x:x[1]-x[0])];return r

class Solution:
    def minimumEffort(self, t: List[List[int]]) -> int:
        r=0;[r:=max(r+a,b)for a,b in sorted(t,key=lambda x:-sub(*x))];return r

test('''
1665. Minimum Initial Energy to Finish Tasks
Hard
Topics
premium lock icon
Companies
Hint
You are given an array tasks where tasks[i] = [actuali, minimumi]:

actuali is the actual amount of energy you spend to finish the ith task.
minimumi is the minimum amount of energy you require to begin the ith task.
For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

You can finish the tasks in any order you like.

Return the minimum initial amount of energy you will need to finish all the tasks.

 

Example 1:

Input: tasks = [[1,2],[2,4],[4,8]]
Output: 8
Explanation:
Starting with 8 energy, we finish the tasks in the following order:
    - 3rd task. Now energy = 8 - 4 = 4.
    - 2nd task. Now energy = 4 - 2 = 2.
    - 1st task. Now energy = 2 - 1 = 1.
Notice that even though we have leftover energy, starting with 7 energy does not work because we cannot do the 3rd task.
Example 2:

Input: tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
Output: 32
Explanation:
Starting with 32 energy, we finish the tasks in the following order:
    - 1st task. Now energy = 32 - 1 = 31.
    - 2nd task. Now energy = 31 - 2 = 29.
    - 3rd task. Now energy = 29 - 10 = 19.
    - 4th task. Now energy = 19 - 10 = 9.
    - 5th task. Now energy = 9 - 8 = 1.
Example 3:

Input: tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
Output: 27
Explanation:
Starting with 27 energy, we finish the tasks in the following order:
    - 5th task. Now energy = 27 - 5 = 22.
    - 2nd task. Now energy = 22 - 2 = 20.
    - 3rd task. Now energy = 20 - 3 = 17.
    - 1st task. Now energy = 17 - 1 = 16.
    - 4th task. Now energy = 16 - 4 = 12.
    - 6th task. Now energy = 12 - 6 = 6.
 

Constraints:

1 <= tasks.length <= 105
1 <= actual​i <= minimumi <= 104
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
23,723/39K
Acceptance Rate
60.9%
Topics
Senior Staff
Array
Greedy
Sorting
Weekly Contest 216
icon
Companies
Hint 1
We can easily figure that the f(x) : does x solve this array is monotonic so binary Search is doable
Hint 2
Figure a sorting pattern
''')
