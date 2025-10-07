from lc import *

# https://leetcode.com/problems/avoid-flood-in-the-city/solutions/7246588/avoid-flood-in-the-city-union-find-optimal-solution/

class Solution:
    def avoidFlood(self, rain: List[int]) -> List[int]:
        n = len(rain)
        uf = UnionFind(n + 1)
        map_lake = {}
        res = [1] * n

        for i, lake in enumerate(rain):
            if lake != 0:
                res[i] = -1
                uf.unite(i)
                
                if lake in map_lake:
                    prev = map_lake[lake]
                    dry = uf.find(prev + 1)
                    
                    if dry >= i:
                        return []

                    res[dry] = lake
                    uf.unite(dry)
                    map_lake[lake] = i
                else:
                    map_lake[lake] = i

        return res

class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size + 1))

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i: int):
        self.parent[i] = self.find(i + 1)

# unicode find

class Solution:
    def avoidFlood(self, rain: List[int]) -> List[int]:
        t = ''.join(map(chr, range(len(rain))))
        m = {}
        r = [1] * len(rain)
        
        for i, lake in enumerate(rain):
            if lake:
                r[i] = -1
                t = t[:i] + chr(len(rain)) + t[i+1:]
                
                if lake in m:
                    p = m[lake]
                    d = next((j for j in range(p+1, i) if t[j] < chr(len(rain))), -1)
                    
                    if d == -1:
                        return []
                    
                    r[d] = lake
                    t = t[:d] + chr(len(rain)) + t[d+1:]
                
                m[lake] = i
        
        return r


# https://leetcode.com/problems/avoid-flood-in-the-city/solutions/699309/ten-lines-of-codes/

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        visited, empty, ret={}, [], [-1]*len(rains)
        for i, lake in enumerate(rains):
            if lake==0: empty.append(i); ret[i]=1; continue
            if lake in visited:
                ind = bisect.bisect(empty, visited[lake])
                if ind>=len(empty):
                    return []
                ret[empty[ind]]=lake
                del empty[ind]
            visited[lake]=i
        return ret

class Solution:
    def avoidFlood(self,r:List[int])->List[int]:
        v,e,t,s={},[],[-1]*len(r),setitem
        for i,x in enumerate(r):
            if x==0:
                e.append(i)
                s(t,i,1)
            elif x in v:
                if(j:=bisect_left(e,v[x]))>=len(e):
                    return[]
                s(t,e[j],x)
                e.pop(j)
            s(v,x,i)
        return t

class Solution:
    def avoidFlood(self,r:List[int])->List[int]:
        v,e,t,s={},[],[-1]*len(r),setitem
        for i,x in enumerate(r):
            if x:
                if x in v:
                    if(j:=bisect_left(e,v[x]))>=len(e):
                        return[]
                    s(t,e[j],x)
                    e.pop(j)
                s(v,x,i)
            else:
                e.append(i)
                s(t,i,1)
        return t

class Solution:
    def avoidFlood(self,r:List[int])->List[int]:
        v,e,t,s,z={},[],[-1]*len(r),setitem,1
        for i,x in enumerate(r):
            if x:
                if x in v:
                    z=(j:=bisect_left(e,v[x]))<len(e)
                    z and (s(t,e.pop(j),x))
                (s(v,x,i),s(t,i,-1))
            else:
                (e.append(i),s(t,i,1))
            if not z:
                break
        return t*z

class Solution:
    def avoidFlood(self,r:List[int])->List[int]:
        v,e,t,s,z={},[],[-1]*len(r),setitem,1;[x and(x in v and(z:=(j:=bisect_left(e,v[x]))<len(e))and(s(t,e.pop(j),x)),s(v,x,i),s(t,i,-1))or(e.append(i),s(t,i,1))for i,x in enumerate(r)if z];return t*z

test('''
1488. Avoid Flood in The City
Medium
Topics
premium lock icon
Companies
Hint
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.

Given an integer array rains where:

rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:

ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.

 

Example 1:

Input: rains = [1,2,3,4]
Output: [-1,-1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day full lakes are [1,2,3]
After the fourth day full lakes are [1,2,3,4]
There's no day to dry any lake and there is no flood in any lake.
Example 2:

Input: rains = [1,2,0,0,2,1]
Output: [-1,-1,2,1,-1,-1]
Explanation: After the first day full lakes are [1]
After the second day full lakes are [1,2]
After the third day, we dry lake 2. Full lakes are [1]
After the fourth day, we dry lake 1. There is no full lakes.
After the fifth day, full lakes are [2].
After the sixth day, full lakes are [1,2].
It is easy that this scenario is flood-free. [-1,-1,1,2,-1,-1] is another acceptable scenario.
Example 3:

Input: rains = [1,2,0,1,2]
Output: []
Explanation: After the second day, full lakes are  [1,2]. We have to dry one lake in the third day.
After that, it will rain over lakes [1,2]. It's easy to prove that no matter which lake you choose to dry in the 3rd day, the other one will flood.

Other examples

Input: rains = [0,0,0,0,0,0,0,0,0,0,0,0,0,56438,0,0,76913,0,0,53492,0,50824,0,0,0,0,0,0,0,0,79212,0,0,0,0,0,0,36713,62045,79212,36713,56438,0,0,0,62045,0,76913,50824,0,0,0,0,0,53492,0]
Output: []

Constraints:

1 <= rains.length <= 105
0 <= rains[i] <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
42,309/153.1K
Acceptance Rate
27.6%
Topics
Array
Hash Table
Binary Search
Greedy
Heap (Priority Queue)
Weekly Contest 194
icon
Companies
Hint 1
Keep An array of the last day there was rains over each city.
Hint 2
Keep an array of the days you can dry a lake when you face one.
Hint 3
When it rains over a lake, check the first possible day you can dry this lake and assign this day to this lake.
''')
