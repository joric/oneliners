from lc import *

# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/solutions/5326380/python3-4-lines/?envType=daily-question&envId=2025-10-11

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        a = b = c = x = y = 0
        for z, d in sorted(Counter(power).items(), reverse=True):
            a, x, b, y, c = max(a, z * d + (a if x > z + 2 else b if y > z + 2 else c)), z, a, x, b
        return a

class Solution:
    def maximumTotalDamage(self, p: List[int]) -> int:
        a=b=c=x=y=0
        for z,d in sorted(Counter(p).items())[::-1]:
            a,x,b,y,c=max(a,z*d+((c,b)[y>z+2],a)[x>z+2]),z,a,x,b
        return a

class Solution:
    def maximumTotalDamage(self, p: List[int]) -> int:
        t=[0]*5;[t:=(lambda a,x,b,y,c,z,d:(max(a,z*d+((c,b)[y>z+2],a)[x>z+2]),z,a,x,b))(*t,*p)for p in sorted(Counter(p).items())[::-1]];return t[0]

# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/solutions/5320392/dp-binary-search-4-lines-python/?envType=daily-question&envId=2025-10-11

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        @cache
        def calc(i):
            if i == len(power):
                return 0
            curr = power[i]*(bisect.bisect(power, power[i])-i)
            return max(calc(i+1), calc(bisect.bisect(power, power[i]+2))+curr)
        power.sort()
        return calc(0)

class Solution:
    def maximumTotalDamage(self, p: List[int]) -> int:
        p.sort();return(f:=cache(lambda i:i<len(p) and max(f(i+1),f(bisect_right(p,p[i]+2))+p[i]*(bisect_right(p,p[i])-i))))(0)

class Solution:
    def maximumTotalDamage(self, p: List[int]) -> int:
        b=bisect_right;p.sort();return(f:=cache(lambda i:i<len(p)and max(f(i+1),f(b(p,p[i]+2))+p[i]*(b(p,p[i])-i))))(0)

test('''
3186. Maximum Total Damage With Spell Casting
Solved
Medium
Topics
premium lock icon
Companies
Hint
A magician has various spells.

You are given an array power, where each element represents the damage of a spell. Multiple spells can have the same damage value.

It is a known fact that if a magician decides to cast a spell with a damage of power[i], they cannot cast any spell with a damage of power[i] - 2, power[i] - 1, power[i] + 1, or power[i] + 2.

Each spell can be cast only once.

Return the maximum possible total damage that a magician can cast.

 

Example 1:

Input: power = [1,1,3,4]

Output: 6

Explanation:

The maximum possible damage of 6 is produced by casting spells 0, 1, 3 with damage 1, 1, 4.

Example 2:

Input: power = [7,1,6,6]

Output: 13

Explanation:

The maximum possible damage of 13 is produced by casting spells 1, 2, 3 with damage 1, 6, 6.

 

Constraints:

1 <= power.length <= 105
1 <= power[i] <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
32,709/114.1K
Acceptance Rate
28.7%
Topics
Array
Hash Table
Two Pointers
Binary Search
Dynamic Programming
Sorting
Counting
Weekly Contest 402
icon
Companies
Hint 1
If we ever decide to use some spell with power x, then we will use all spells with power x.
Hint 2
Think of dynamic programming.
Hint 3
dp[i][j] represents the maximum damage considering up to the i-th unique spell and j represents the number of spells skipped (up to 3 as per constraints).
''')
