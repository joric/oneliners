from lc import *

# https://leetcode.com/problems/find-the-town-judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        c = [0]*(n+1)
        for a,b in trust:
            c[a] -= 1
            c[b] += 1
        for i in range(1, n+1):
            if c[i]==n-1:
                return i
        return -1

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        return (c:=Counter(),[c.update({a:-1,b:1}) for a,b in trust]) and next((i for i in range(1,n+1) if c[i]==n-1),-1)

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [x[0] for x in trust]
        b = [x[1] for x in trust]
        for i in range(1,n+1):
            if a.count(i)==0 and b.count(i)==n-1:
                return i
        return -1

class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        return next((i for i in range(1,n+1) if p[0].count(i)==0 and p[1].count(i)==n-1),(p:=[*zip(*t)]or[[]]*2)and -1)

# updated 2024-02-22

class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        p=[*zip(*t)]or[[]]*2;return next((i for i in range(1,n+1)if p[0].count(i)<1 and p[1].count(i)==n-1),-1)

class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        p=[*zip(*t)]or[[]]*2;
        for i in range(1,n+1):
            if[t.count(i)for t in p]==[0,n-1]:
                return i
        return -1;

class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        p=[*zip(*t)]or[[]]*2;return next((i for i in range(1,n+1)if[t.count(i)for t in p]==[0,n-1]),-1)

class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        c=Counter();[c.update({a:-1,b:1})for a,b in t];return next((i for i in range(1,n+1)if c[i]>n-2),-1)

class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        c=Counter;a,b=zip(*t+[[-1]*2]);c=c(b)-c(a);return next((i for i in range(1,n+1)if c[i]>n-2),-1)

class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        a,b=map(Counter,zip(*t+[[0]*2]));c=b-a;return next((i for i in range(1,n+1)if c[i]>n-2),-1)

class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        a,b=map(Counter,zip(*t+[[0]*2]));c=b-a;return next((i for i in c if c[i]>n-2),(-1,1)[n<2])

test('''

997. Find the Town Judge
Easy

4266

315

Add to List

Share
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Example 4:

Input: n=1, trust = []
Output: 1

Example 5:

Input: n=2, trust = []
Output: -1

Constraints:

1 <= n <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
''')