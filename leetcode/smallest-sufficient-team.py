from lc import *

# https://leetcode.com/problems/smallest-sufficient-team/discuss/334572/JavaC%2B%2BPython-DP-Solution

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m = len(req_skills), len(people)
        skill_index = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            cur_skill = 0
            for skill in p:
                if skill in skill_index:
                    cur_skill |= 1 << skill_index[skill]
            for prev, need in dict(dp).items():
                comb = prev | cur_skill
                if comb == prev: continue
                if comb not in dp or len(dp[comb]) > len(need) + 1:
                    dp[comb] = need + [i]
        return dp[(1 << n) - 1]

class Solution:
    def smallestSufficientTeam(self, r: List[str], p: List[List[str]]) -> List[int]:
        n,m = len(r),len(p)
        b = {v:i for i,v in enumerate(r)}
        d = {0:[]}
        for i,v in enumerate(p):
            c=0
            for s in v:
                if s in b:
                    c |= 1<<b[s]
            for j,w in dict(d).items():
                k = j|c
                if k==j:
                    continue
                if k not in d or len(d[k])>len(w)+1:
                    d[k] = w + [i]
        return d[(1<<n)-1]

class Solution:
    def smallestSufficientTeam(self, r: List[str], p: List[List[str]]) -> List[int]:
        n,m,b,d=len(r),len(p),{v:i for i,v in enumerate(r)},{0:[]}
        for i,v in enumerate(p):
            c = 0
            for s in v:
                if s in b:
                    c |= 1 << b[s]
            [(k:=j|c,(k!=j and k not in d or len(d[k])>len(w)+1)and setitem(d,k,w+[i]))for j,w in dict(d).items()]
        return d[(1<<n)-1]

class Solution:
    def smallestSufficientTeam(self, r: List[str], p: List[List[str]]) -> List[int]:
        n,m,b,d=len(r),len(p),{v:i for i,v in enumerate(r)},{0:[]};[(c:=0,[(c:=c|1<<b[s])for s in v if s in b],[(k:=j|c,(k!=j and k not in d or len(d[k])>len(w)+1)and setitem(d,k,w+[i]))for j,w in dict(d).items()])for i,v in enumerate(p)];return d[(1<<n)-1]

test('''
1125. Smallest Sufficient Team
Hard

1127

23

Add to List

Share
In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.

 

Example 1:

Input: req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]
Example 2:

Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]
 

Constraints:

1 <= req_skills.length <= 16
1 <= req_skills[i].length <= 16
req_skills[i] consists of lowercase English letters.
All the strings of req_skills are unique.
1 <= people.length <= 60
0 <= people[i].length <= 16
1 <= people[i][j].length <= 16
people[i][j] consists of lowercase English letters.
All the strings of people[i] are unique.
Every skill in people[i] is a skill in req_skills.
It is guaranteed a sufficient team exists.
''')

