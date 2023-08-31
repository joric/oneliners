from lc import *

# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/1386524/2-solutions-DP-and-Greedy-with-how-you-behave-when-being-asked-during-interviews

class Solution:
    def minTaps(self, n: int, r: List[int]) -> int:
        v = sorted((max(0,i-x),min(n,i+x))for i,x in enumerate(r))
        @cache
        def f(i,j):
            if i==len(r) or j==n:
                return 0
            c = inf
            for i in range(i,len(r)):
                if v[i][0]<=j:
                    c = min(c,f(i+1,v[i][1])+1)
                else:
                    break
            return c
        if v[0][0] > 0:
            return -1
        c = f(0, 0)
        return -1 if c==inf else c

# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484235/JavaC%2B%2BPython-Similar-to-LC1024

class Solution:
    def minTaps(self, n: int, r: List[int]) -> int:
        d = [0]+[n+2]*n
        for i,x in enumerate(r):
            for j in range(max(i-x+1,0), min(i+x,n)+1):
                d[j] = min(d[j], d[max(0,i-x)]+1)
        return d[n] if d[n]<n+2 else -1

class Solution:
    def minTaps(self, n: int, r: List[int]) -> int:
        d=[0]+[n+2]*n;[setitem(d,j,min(d[j],d[max(0,i-x)]+1))for i,x in enumerate(r)for j in range(max(i-x+1,0),min(i+x,n)+1)];return d[n]<n+2 and d[n]or-1

# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/3508593/Minimum-Number-of-Taps-to-Open-to-Water-a-Garden-(C)

class Solution:
    def minTaps(self, n: int, r: List[int]) -> int:
        @cache
        def f(i):
            if i<=0:
                return 0
            c = inf
            for j in range(i,-1,-1):
                if r[j]>0 and r[j]+j>=i:
                    c = min(c,1+f(j-r[j]))
            return c
        c = f(n)
        return -1 if c>=inf else c

class Solution:
    def minTaps(self, n: int, r: List[int]) -> int:
        return(-1,c:=(f:=cache(lambda i:i>0and min((1+f(j-r[j])for j in range(i,-1,-1)if 0<r[j]>=i-j),default=inf)))(n))[c<inf]

test('''
1326. Minimum Number of Taps to Open to Water a Garden
Hard

2076

122

Add to List

Share
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

 

Example 1:


Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
 

Constraints:

1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100
''')

