from lc import *

# 

# unicode find attempt (TLE)
class Solution:
    def findAllPeople(self, n: int, m: List[List[int]], p: int) -> List[int]:
        t = ''.join(map(chr,range(n)))
        g = defaultdict(list)
        for u,v,w in m:
            g[w].append((u,v))
        t = t.replace(t[0],t[p])
        for w in sorted(g):
            while True:
                changed = False
                for u, v in g[w]:
                    if (t[u] == t[0]) != (t[v] == t[0]):
                        t = t.replace(t[u], t[v])
                        changed = True
                if not changed:
                    break
        return [i for i in range(n) if t[i] == t[0]]

# union find

class Solution:
    def findAllPeople(self, n: int, m: List[List[int]], x: int) -> List[int]:
        a,r,p,r[x],f,s=[],[*range(n)],0,0,lambda v:r[v]-v and s(r,v,f(r[v]))or r[v],setitem;l=a.append;[[t-p and([f(g)-f(0)and s(r,g,g)for g in a],a.clear()),p:=t,s(r,f(c),f(v)),l(c),l(v)]for c,v,t in sorted(m,key=lambda o:o[2])];return{i*(f(i)==f(0))for i in range(n)}

# https://leetcode.com/problems/find-all-people-with-secret/discuss/1600466/Python3-12-line-solution-(2140ms)

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knows = {0, firstPerson}
        meetings.sort(key=lambda x: x[2])
        for _, group in groupby(meetings, lambda x: x[2]):
            people = defaultdict(set)
            for x, y, _ in group:
                people[x].add(y)
                people[y].add(x)
            to_know = knows & people.keys()
            while to_know:
                to_know = reduce(set.union, ((people[x] - knows) for x in to_know), set())
                knows.update(to_know)
        return list(knows)

class Solution:
    def findAllPeople(self, n: int, m: List[List[int]], p: int) -> List[int]:
        k = {0,p}
        m.sort(key=itemgetter(2))
        for _,g in groupby(m,itemgetter(2)):
            s = defaultdict(set)
            for x,y, _ in g:
                s[x].add(y)
                s[y].add(x)
            t = k&s.keys()
            while t:
                t = reduce(set.union,(s[x]-k for x in t),set())
                k.update(t)
        return k

class Solution:
    def findAllPeople(self, n: int, m: List[List[int]], p: int) -> List[int]:
        k,r={0,p},itemgetter(2);m.sort(key=r);[(s:=defaultdict(set),[s[x].add(y)or s[y].add(x)for x,y,_ in g],t:=k&s.keys(),all(k.update(t:=reduce(set.union,(s[x]-k for x in t),set()))or t for _ in m))for _,g in groupby(m,r)];return[*k]

test('''
2092. Find All People With Secret
Hard

806

29

Add to List

Share
You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.

Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.

The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.

Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.

 

Example 1:

Input: n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
Output: [0,1,2,3,5]
Explanation:
At time 0, person 0 shares the secret with person 1.
At time 5, person 1 shares the secret with person 2.
At time 8, person 2 shares the secret with person 3.
At time 10, person 1 shares the secret with person 5.​​​​
Thus, people 0, 1, 2, 3, and 5 know the secret after all the meetings.
Example 2:

Input: n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
Output: [0,1,3]
Explanation:
At time 0, person 0 shares the secret with person 3.
At time 2, neither person 1 nor person 2 know the secret.
At time 3, person 3 shares the secret with person 0 and person 1.
Thus, people 0, 1, and 3 know the secret after all the meetings.
Example 3:

Input: n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
Output: [0,1,2,3,4]
Explanation:
At time 0, person 0 shares the secret with person 1.
At time 1, person 1 shares the secret with person 2, and person 2 shares the secret with person 3.
Note that person 2 can share the secret at the same time as receiving it.
At time 2, person 3 shares the secret with person 4.
Thus, people 0, 1, 2, 3, and 4 know the secret after all the meetings.


Other examples:

Input: n = 5, meetings = [[1,4,3],[0,4,3]], firstPerson = 3
Output: [0,1,3,4]

Constraints:

2 <= n <= 10^5
1 <= meetings.length <= 10^5
meetings[i].length == 3
0 <= xi, yi <= n - 1
xi != yi
1 <= timei <= 10^5
1 <= firstPerson <= n - 1
Accepted
24,378
Submissions
71,217
''')