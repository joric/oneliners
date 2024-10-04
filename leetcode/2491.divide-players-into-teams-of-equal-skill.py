from lc import *

# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/discuss/2881355/Python-or-Video-Walkthrough-or-Easy-or-5-Line-Solution

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        s, matched, gratitude, HT = 2 * sum(skill) // (len(skill)),0,0, defaultdict(lambda: 0)
        for sk in skill: 
            if HT[s - sk] > 0: gratitude,  HT[s - sk],matched  = gratitude +  (sk) * (s - sk), HT[s - sk] - 1, matched + 1
            else: HT[sk] += 1
        return gratitude if (matched == len(skill) //2) else -1

class Solution:
    def dividePlayers(self, s: List[int]) -> int:
        c = Counter()
        m = g = 0
        a = 2*sum(s)//len(s)
        for i in s:
            j = a - i
            if c[j] > 0:
                c[j] -= 1
                g += i*j
                m += 1
            else:
                c[i] += 1
        return(-1,g)[m==len(s)//2]

# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/discuss/2875011/PythonC%2B%2B-O(N)-counting-and-pair-matching-(explained)

class Solution:
    def dividePlayers(self, s: List[int]) -> int:
        s.sort()
        r = 0
        t = s[0]+s[-1]
        for i in range(len(s)//2):
            if s[i]+s[~i]==t:
                r += s[i] * s[~i]
            else:
                return -1
        return r

class Solution:
    def dividePlayers(self, s: List[int]) -> int:
        s.sort()
        r = range(len(s)//2)
        for i in r:
            if s[i]+s[~i]!=s[0]+s[-1]:
                return -1
        return sum(s[i]*s[~i]for i in r)

class Solution:
    def dividePlayers(self, s: List[int]) -> int:
        s.sort();r=range(len(s)//2);return(sum(s[i]*s[~i]for i in r),-1)[any(s[i]+s[~i]!=s[0]+s[-1]for i in r)]

class Solution:
    def dividePlayers(self, s: List[int]) -> int:
        s.sort();return(-1,r:=sum((inf,s[i]*s[~i])[s[i]+s[~i]==s[0]+s[-1]]for i in range(len(s)//2)))[r<inf]

# updated 2024-10-04 (POTD)

class Solution:
    def dividePlayers(self, s: List[int]) -> int:
        s.sort();return(-1,sum(map(mul,s,t:=s[::-1]))//2)[len({*map(add,s,t)})<2]

test('''
2491. Divide Players Into Teams of Equal Skill
Medium

484

12

Add to List

Share
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

 

Example 1:

Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
Example 2:

Input: skill = [3,4]
Output: 12
Explanation: 
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.
Example 3:

Input: skill = [1,1,2,3]
Output: -1
Explanation: 
There is no way to divide the players into teams such that the total skill of each team is equal.
 

Constraints:

2 <= skill.length <= 105
skill.length is even.
1 <= skill[i] <= 1000
Accepted
38,591
Submissions
64,002
''')
