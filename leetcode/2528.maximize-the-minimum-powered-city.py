from lc import *

# https://leetcode.com/problems/maximize-the-minimum-powered-city/solutions/6146907/python3-binary-search-line-sweep-by-0icy-stai/

# TODO

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        temp = 0
        orig = []
        for i in range(min(r+1,len(stations))):
            temp += stations[i]
        orig.append(temp)
        for i in range(1,len(stations)):
            if i+r < len(stations):
                temp += stations[i+r]
            if i-r-1 >= 0:
                temp -= stations[i-r-1]
            orig.append(temp)

        def pos(n):
            count = [0 for x in range(len(stations)+1)]
            kk = k
            temp = 0
            for i in range(len(stations)):
                temp += count[i]
                if temp+orig[i] < n:
                    req = n-(temp+orig[i])
                    if req > kk:
                        return False
                    kk-=req
                    temp += req
                    count[min(i+2*r+1,len(stations))]-=req
            return True
        
        low = 0
        high = int(1e11)
        while low <= high:
            middle = (low+high)//2
            if pos(middle):
                low = middle+1
            else:
                high = middle-1
        return low-1

class Solution:
    def maxPower(self, s: List[int], r: int, k: int) -> int:
        n=len(s)
        p=[w:=sum(s[:r+1]),*[0]*(n-1)]
        [setitem(p,i,w:=w+(i+r<n and s[i+r])-(i-r-1>=0 and s[i-r-1]))for i in range(1,n)]
        def f(x):
            d = [0] * (n + 1)
            c, m = 0, k
            for i in range(n):
                c += d[i]
                if p[i] + c < x:
                    t = x-p[i]-c
                    if t>m:
                        return False
                    m -= t
                    c += t
                    b = min(n,i+2*r+1)
                    d[b] -= t
            return True
        return bisect_right(range(sum(s)+k+1), False, key=lambda x: not f(x)) - 1

test('''
2528. Maximize the Minimum Powered City
Hard
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.

Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.

Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
The power of a city is the total number of power stations it is being provided power from.

The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.

Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.

Note that you can build the k power stations in multiple cities.

 

Example 1:

Input: stations = [1,2,4,5,0], r = 1, k = 2
Output: 5
Explanation: 
One of the optimal ways is to install both the power stations at city 1. 
So stations will become [1,4,4,5,0].
- City 0 is provided by 1 + 4 = 5 power stations.
- City 1 is provided by 1 + 4 + 4 = 9 power stations.
- City 2 is provided by 4 + 4 + 5 = 13 power stations.
- City 3 is provided by 5 + 4 = 9 power stations.
- City 4 is provided by 5 + 0 = 5 power stations.
So the minimum power of a city is 5.
Since it is not possible to obtain a larger power, we return 5.
Example 2:

Input: stations = [4,4,4,4], r = 0, k = 3
Output: 4
Explanation: 
It can be proved that we cannot make the minimum power of a city greater than 4.
 

Constraints:

n == stations.length
1 <= n <= 105
0 <= stations[i] <= 105
0 <= r <= n - 1
0 <= k <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
9,930/29.1K
Acceptance Rate
34.1%
Topics
Array
Binary Search
Greedy
Queue
Sliding Window
Prefix Sum
Biweekly Contest 95
icon
Companies
Hint 1
Pre calculate the number of stations on each city using Line Sweep.
Hint 2
Use binary search to maximize the minimum.
Similar Questions
Maximum Number of Tasks You Can Assign
Hard
''')
