from lc import *

# https://leetcode.com/problems/jump-game-iii/solutions/954194/python-iterative-7-lines-clean-no-visite-q4e7/?envType=daily-question&envId=2026-05-17

class Solution:
    def canReach(self, a: List[int], s: int) -> bool:
        n,p=len(a),{s}
        while p:
            if 0 <= (i:=p.pop()) < n and a[i] is not None:
                if a[i] is 0: return True
                p |= {i+a[i],i-a[i]}
                a[i] = None
        return False

# http://leetcode.com/problems/jump-game-iii/solutions/4754165/awesome-python-solution-with-recursion-b-39ra/?envType=daily-question&envId=2026-05-17

class Solution:
    def canReach(self, a: List[int], s: int) -> bool:
        v=set()
        def f(i):
            if i>=len(a) or i<0 or i in v:
                return False
            if a[i]==0:
                return True
            v.add(i)
            return f(i+a[i]) or f(i-a[i])
        return f(s)

class Solution:
    def canReach(self, a: List[int], s: int) -> bool:
        return(f:=lambda i,v={-1}:0<=i<len(a)and{i}-v and(1>(x:=a[i])or v.add(i)or f(i+x)or f(i-x)))(s)

test('''
1306. Jump Game III
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
 

Constraints:

1 <= arr.length <= 5 * 104
0 <= arr[i] < arr.length
0 <= start < arr.length
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
302,331/452K
Acceptance Rate
66.9%
Topics
Staff
Array
Depth-First Search
Breadth-First Search
Weekly Contest 169
icon
Companies
Hint 1
Think of BFS to solve the problem.
Hint 2
When you reach a position with a value = 0 then return true.
Similar Questions
Jump Game II
Medium
Jump Game
Medium
Jump Game VII
Medium
Jump Game VIII
Medium
Maximum Number of Jumps to Reach the Last Index
Medium
''')
