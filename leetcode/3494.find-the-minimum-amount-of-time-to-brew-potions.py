from lc import *

# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/description/?envType=daily-question&envId=2025-10-09

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        curTime = 0
        for i in range(1, len(mana)):
            timeShift = 0
            cur = 0
            for j, s in enumerate(skill):
                timeShift = max(timeShift, (cur + s) * mana[i - 1] - cur * mana[i])
                cur += s
            curTime += timeShift
        return curTime + sum(skill) * mana[-1]

class Solution:
    def minTime(self, s: List[int], m: List[int]) -> int:
        t=0
        for i in range(1,len(m)):
            d=0
            c=0
            for v in s:
                d=max(d,(c+v)*m[i-1]-c*m[i])
                c+=v
            t+=d
        return t+sum(s)*m[-1]

# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/solutions/6603130/prefix-sum-two-lines-time-o-m-n/?envType=daily-question&envId=2025-10-09

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        p = [*accumulate(skill, initial = 0)];return p[-1]*mana[-1]+sum(max(p2*m1-p1*m2 for p1, p2 in pairwise(p)) for m1, m2 in pairwise(mana))

class Solution:
    def minTime(self, s: List[int], m: List[int]) -> int:
        p=[0,*accumulate(s)];return p[-1]*m[-1]+sum(max(b*c-a*d for a,b in pairwise(p)) for c,d in pairwise(m))

class Solution:
    def minTime(self, s: List[int], m: List[int]) -> int:
        p,t=pairwise,[0,*accumulate(s)];return t[-1]*m[-1]+sum(max(b*c-a*d for a,b in p(t))for c,d in p(m))

test('''
3494. Find the Minimum Amount of Time to Brew Potions
Medium
Topics
premium lock icon
Companies
Hint
You are given two integer arrays, skill and mana, of length n and m, respectively.

In a laboratory, n wizards must brew m potions in order. Each potion has a mana capacity mana[j] and must pass through all the wizards sequentially to be brewed properly. The time taken by the ith wizard on the jth potion is timeij = skill[i] * mana[j].

Since the brewing process is delicate, a potion must be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be synchronized so that each wizard begins working on a potion exactly when it arrives. ​

Return the minimum amount of time required for the potions to be brewed properly.

 

Example 1:

Input: skill = [1,5,2,4], mana = [5,1,4,2]

Output: 110

Explanation:

Potion Number   Start time  Wizard 0 done by    Wizard 1 done by    Wizard 2 done by    Wizard 3 done by
0   0   5   30  40  60
1   52  53  58  60  64
2   54  58  78  86  102
3   86  88  98  102 110
As an example for why wizard 0 cannot start working on the 1st potion before time t = 52, consider the case where the wizards started preparing the 1st potion at time t = 50. At time t = 58, wizard 2 is done with the 1st potion, but wizard 3 will still be working on the 0th potion till time t = 60.

Example 2:

Input: skill = [1,1,1], mana = [1,1,1]

Output: 5

Explanation:

Preparation of the 0th potion begins at time t = 0, and is completed by time t = 3.
Preparation of the 1st potion begins at time t = 1, and is completed by time t = 4.
Preparation of the 2nd potion begins at time t = 2, and is completed by time t = 5.
Example 3:

Input: skill = [1,2,3,4], mana = [1,2]

Output: 21

 

Constraints:

n == skill.length
m == mana.length
1 <= n, m <= 5000
1 <= mana[i], skill[i] <= 5000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
11,933/32.9K
Acceptance Rate
36.3%
Topics
icon
Companies
Hint 1
Maintain each wizard's earliest free time (for the last potion) as f[i].
Hint 2
Let x be the current mana value. Starting from now = f[0], update now = max(now + skill[i - 1] * x, f[i]) for i in [1..n]. Then, the final f[n - 1] = now + skill[n - 1] * x for this potion.
Hint 3
Update all other f values by f[i] = f[i + 1] - skill[i + 1] * x for i in [0..n - 2] (in reverse order).
''')

