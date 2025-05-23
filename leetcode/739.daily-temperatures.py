from lc import *

class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        r,s = [0]*len(t), []
        for i,x in enumerate(t):
            while s and x>t[s[-1]]:
                j = s.pop()
                r[j] = i-j
            s.append(i)
        return r

class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        return (r:=[0]*len(t),s:=[]) and any(next(1 for _ in count() if not(s and x>t[s[-1]] and not setitem(r,j:=s.pop(),i-j))) and s.append(i) for i,x in enumerate(t)) or r

# # https://leetcode.com/problems/daily-temperatures/discuss/436705/5-line-Python-numpy-solution

import numpy as np
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        t,r = np.array(t), []
        for i, x in enumerate(t):
            r.append(np.argmax(t[i:]>x))
        return r

# TLE
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        p,r=__import__('numpy'),[];t=p.array(t);return[p.argmax(t[i:]>x)for i,x in enumerate(t)]

# updated 2024-01-31

class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        l=len(t)
        r=[0]*l
        s=[]
        for i in range(l-1,-1,-1):
            c=t[i]
            while s and t[s[-1]]<=c:
                s.pop()
            r[i]=s[-1]-i if s else 0
            s.append(i)
        return r

class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        l,x=len(t),[0]*102;return[setitem(x,c:=t[l-i],i)or(i-max(x[c+1:]))%i for i in range(1,l+1)][::-1]

test('''

739. Daily Temperatures
Medium

8808

203

Add to List

Share
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100

''')
