from lc import *

# https://leetcode.com/problems/maximum-running-time-of-n-computers/discuss/1692939/JavaC%2B%2BPython-Sort-Solution-with-Explanation-O(mlogm)

class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        b.sort()
        s = sum(b)
        while b[-1]>s/n:
            n -= 1
            s -= b.pop()
        return s//n

# POTD 2025-12-01

class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        b.sort();s=sum(b);return next(s//n for _ in[0]*n if not(s/n<b[-1]and(n:=n-1,s:=s-b.pop())))

class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        b.sort();s=sum(b);return next(s//n for _ in[0]*n if s/n>=b[-1]or(n:=n-1,s:=s-b.pop())==0)

# https://leetcode.com/problems/maximum-running-time-of-n-computers/solutions/7384390/swift1liner-by-orchidhunter-nex5/

class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        return bisect_left(range(1,10**15),1,key=lambda m:sum(min(x,m)for x in b)<n*m)

class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        return~-bisect_left(range(9**15),1,key=lambda m:sum(min(x,m)for x in b)<n*m)

test('''
2141. Maximum Running Time of N Computers
Hard

804

21

Add to List

Share
You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.

 

Example 1:


Input: n = 2, batteries = [3,3,3]
Output: 4
Explanation: 
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

Example 2:


Input: n = 2, batteries = [1,1,1,1]
Output: 2
Explanation: 
Initially, insert battery 0 into the first computer and battery 2 into the second computer. 
After one minute, battery 0 and battery 2 are drained so you need to remove them and insert battery 1 into the first computer and battery 3 into the second computer. 
After another minute, battery 1 and battery 3 are also drained so the first and second computers are no longer running.
We can run the two computers simultaneously for at most 2 minutes, so we return 2.

Example 3:

Input: n = 3, batteries = [10,10,3,5]
Output: 8

Other examples:

Input: n = 1, batteries = [1]
Output: 1

Constraints:

1 <= n <= batteries.length <= 10^5
1 <= batteries[i] <= 10^9
''')
