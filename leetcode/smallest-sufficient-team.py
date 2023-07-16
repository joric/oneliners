from lc import *

# https://leetcode.com/problems/smallest-sufficient-team/discuss/691327/Bit-masking-solution-in-python-explained-line-by-line-in-greatest-depth-possible

class Solution:
    def smallestSufficientTeam(self, r: List[str], p: List[List[str]]) -> List[int]:
        d,m={0:[]},{r[i]:i for i in range(len(r))}
        for i in range(len(p)):
            c=0
            for s in p[i]:
                c |= 1<<(m[s])
            for j,v in dict(d).items():
                k = j | c
                if k not in d or len(d[k])>len(v)+1:
                   d[k]=v+[i]
        return d[(1<<len(m))-1]

class Solution:
    def smallestSufficientTeam(self, r: List[str], p: List[List[str]]) -> List[int]:
        d,m={0:[]},{r[i]:i for i in range(len(r))};[(c:=0,[(c:=c|1<<m[s])for s in p[i]],[(k:=j|c,(k not in d or len(d[k])>len(v)+1)and setitem(d,k,v+[i]))for j,v in dict(d).items()])for i in range(len(p))];return d[(1<<len(m))-1]

class Solution:
    def smallestSufficientTeam(self, r: List[str], p: List[List[str]]) -> List[int]:
        l=len;d,m={0:[]},{r[i]:i for i in range(l(r))};[(c:=0,[(c:=c|1<<m[s])for s in p[i]],[(k:=j|c,(k not in d or l(d[k])>l(v)+1)and setitem(d,k,v+[i]))for j,v in dict(d).items()])for i in range(l(p))];return d[(1<<l(m))-1]

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
 
Example 3:

Input: req_skills = ["mmcmnwacnhhdd","vza","mrxyc"], people = [["mmcmnwacnhhdd"],[],[],["vza","mrxyc"]]
Output: [0,3]

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

