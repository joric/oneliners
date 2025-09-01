from lc import *

# https://leetcode.com/problems/maximum-average-pass-ratio/description/?envType=daily-question&envId=2025-09-01

class Solution:
    def maxAverageRatio(self, c: List[List[int]], e: int) -> float:
        return (pq:=[((p/t)-(p+1)/(t+1),p,t) for p,t in c], 
                heapify(pq), 
                [(p:=pq[0][1],t:=pq[0][2],heappop(pq),
                    heappush(pq,((p+1)/(t+1)-(p+2)/(t+2),p+1,t+1)))
                    for _ in range(e)][0],
                sum(p/t for _,p,t in pq)/len(pq))[-1]

class Solution:
    def maxAverageRatio(self, c: List[List[int]], e: int) -> float:
        return(q:=[((p/t)-(p+1)/(t+1),p,t)for p,t in c],heapify(q),[(p:=q[0][1],t:=q[0][2],heappop(q),heappush(q,((p+1)/(t+1)-(p+2)/(t+2),p+1,t+1)))for _ in range(e)][0],sum(p/t for _,p,t in q)/len(q))[-1]

class Solution:
    def maxAverageRatio(self, c: List[List[int]], e: int) -> float:
        return(q:=[((p/t)+~p/-~t,p,t)for p,t in c],heapify(q),[(p:=q[0][1],t:=q[0][2],heappop(q),heappush(q,(~p/~t-(p+2)/(t+2),p+1,t+1)))for _ in range(e)][0],sum(p/t for _,p,t in q)/len(q))[-1]

test('''
1792. Maximum Average Pass Ratio
Solved
Medium
Topics
premium lock icon
Companies
Hint
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.
Example 2:

Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
 

Constraints:

1 <= classes.length <= 105
classes[i].length == 2
1 <= passi <= totali <= 105
1 <= extraStudents <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
107,880/150.7K
Acceptance Rate
71.6%
Topics
Array
Greedy
Heap (Priority Queue)
Weekly Contest 232
icon
Companies
Hint 1
Pay attention to how much the pass ratio changes when you add a student to the class. If you keep adding students, what happens to the change in pass ratio? The more students you add to a class, the smaller the change in pass ratio becomes.
Hint 2
Since the change in the pass ratio is always decreasing with the more students you add, then the very first student you add to each class is the one that makes the biggest change in the pass ratio.
Hint 3
Because each class's pass ratio is weighted equally, it's always optimal to put the student in the class that makes the biggest change among all the other classes.
Hint 4
Keep a max heap of the current class sizes and order them by the change in pass ratio. For each extra student, take the top of the heap, update the class size, and put it back in the heap.
''')
