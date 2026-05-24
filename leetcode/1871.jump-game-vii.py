from lc import *

# https://leetcode.com/problems/jump-game-vii/?envType=daily-question&envId=2026-05-25

class Solution:
    def canReach(self, s: str, a: int, b: int) -> bool:
        d = [c=='0'for c in s]
        r = 0
        for i in range(1, len(s)):
            if i >= a:
                r += d[i-a]
            if i > b:
                r -= d[i-b-1]
            d[i] &= r > 0
        return d[-1]

class Solution:
    def canReach(self, s: str, a: int, b: int) -> bool:
        d=[c=='0'for c in s];r=0;[setitem(d,i,d[i]&((r:=r+(i>=a and d[i-a])+(i>b and-d[i-b-1]))>0))for i in range(1,len(s))];return d[-1]

class Solution:
    def canReach(self, s: str, a: int, b: int) -> bool:
        d=[1];r=0;[d.append(s[i]<'1'*((r:=r+(i>=a and d[i-a])+(i>b and-d[i-b-1]))>0))for i in range(1,len(s))];return d[-1]

class Solution:
    def canReach(self, s: str, a: int, b: int) -> bool:
        n=len(s);d=[1]+n*[0];r=0;[setitem(d,i,s[i]<'1'*((r:=r+d[i-a]-d[~b+i])>0))for i in range(1,n)];return d[-2]

test('''
1871. Jump Game VII
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true

Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false


Other examples:

Input: s = "0000000000", minJump = 2, maxJump = 5
Output: true


Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
69,396/260K
Acceptance Rate
26.7%
Topics
Staff
String
Dynamic Programming
Sliding Window
Prefix Sum
Weekly Contest 242
icon
Companies
Hint 1
Consider for each reachable index i the interval [i + a, i + b].
Hint 2
Use partial sums to mark the intervals as reachable.
Similar Questions
Jump Game II
Medium
Jump Game
Medium
Jump Game III
Medium
Jump Game IV
Hard
Jump Game V
Hard
Jump Game VI
Medium
Jump Game VII
Medium
Jump Game VIII
Medium
Count Vowel Strings in Ranges
Medium
Maximum Number of Jumps to Reach the Last Index
Medium
''')
