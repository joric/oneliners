from lc import *

# https://leetcode.com/problems/find-the-town-judge/discuss/242938/JavaC%2B%2BPython-Directed-Graph

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

# https://leetcode.com/problems/find-the-town-judge/discuss/242938/JavaC%2B%2BPython-Directed-Graph

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        c = Counter(b for _,b in trust)
        for a,_ in trust:
            del c[a]
        j = c.most_common(1)[0] if c else (1,0)
        return j[0] if j[1] == n-1 else -1

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        return (c:=reduce(lambda c,t:delitem(c,t[0]) or c,trust, Counter(b for _,b in trust)),j := c.most_common(1)[0] if c else (1,0),j[0] if j[1]==n-1 else -1)[-1]

# mine

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        return (c:=Counter(),[c.update({a:-1,b:1}) for a,b in trust]) and next((i for i in range(1,n+1) if c[i]==n-1),-1)

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
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
''')
