from lc import *

# https://leetcode.com/problems/ones-and-zeroes/solutions/2066242/python-cache-dp-no-tle-by-karan_8082-lg1p/?envType=daily-question&envId=2025-11-11

class Solution:
    def findMaxForm(self, s: List[str], m: int, n: int) -> int:
        c = [[*map(t.count,'01')]for t in s]
        @cache
        def f(i,m,n):
            if m<0 or n<0:
                return -inf
            if (i>=len(c)):
                return 0
            return max(f(i+1,m,n),1+f(i+1,m-c[i][0],n-c[i][1]))
        return f(0,m,n)

class Solution:
    def findMaxForm(self, s: List[str], m: int, n: int) -> int:
        return(f:=cache(lambda i,m,n:-inf if m<0 or n<0 else i<len(s)and max(f(i+1,m,n),1+f(i+1,m-s[i].count('0'),n-s[i].count('1')))))(0,m,n)

# https://leetcode.com/problems/ones-and-zeroes/solutions/1810883/python-4-lines-knapsack-by-fjm11111-63mn/?envType=daily-question&envId=2025-11-11

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {(0, m, n)}
        for s in strs:
            cm, cn = s.count("0"), s.count("1")
            memo |= {(i+1, mm-cm, nn-cn) for i, mm, nn in memo if mm-cm >=0 and nn-cn >= 0}
        return max(i for i, mm, nn in memo)

class Solution:
    def findMaxForm(self, s: List[str], m: int, n: int) -> int:
        return max(reduce(lambda c,t:c|{(i+1,x-a,y-b)for i,x,y in c for a,b in[map(t.count,'01')]if x-a>-1<y-b},s,{(0,m,n)}))[0]

class Solution:
    def findMaxForm(self, s: List[str], m: int, n: int) -> int:
        c={(0,m,n)};[c:=c|{(i+1,x-a,y-b)for i,x,y in c for a,b in[map(t.count,'01')]if x-a>-1<y-b}for t in s];return max(c)[0]

test('''
474. Ones and Zeroes
Solved
Medium
Topics
premium lock icon
Companies
You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Other solutions:

Input: strs = ["10","0001","111001","1","0"], m = 4, n = 3
Output: 3

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
255,163/515.8K
Acceptance Rate
49.5%
Topics
Array
String
Dynamic Programming
icon
Companies
Similar Questions
Count Subarrays With More Ones Than Zeros
Medium
Non-negative Integers without Consecutive Ones
Hard
All Divisions With the Highest Score of a Binary Array
Medium
''')
