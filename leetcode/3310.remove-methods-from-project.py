from lc import *

# https://leetcode.com/problems/remove-methods-from-project/solutions/5875856/python-dfs-by-hogantech-96bp/?envType=daily-question&envId=2026-08-05

class Solution:
    def remainingMethods(self, n: int, k: int, i: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        r = defaultdict(list)
        for u,v in i:
            g[u].append(v)
            r[v].append(u)
        s = set()
        def f(u):
            if u in s:
                return
            s.add(u)
            for v in g[u]:
                f(v)
        f(k)
        for u in s:
            for v in r[u]:
                if v not in s:
                    return list(range(n))
        return [i for i in range(n) if i not in s]

class Solution:
    def remainingMethods(self, n: int, k: int, i: List[List[int]]) -> List[int]:
        g=defaultdict(set);[g[u].add(v)for u,v in i];s={k};(f:=lambda u:[s.add(v)or f(v)for v in g[u]-s])(k);return[*(any((v in s)>(u in s)for u,v in i)and range(n)or{*range(n)}-s)]

class Solution:
    def remainingMethods(self, n: int, k: int, i: List[List[int]]) -> List[int]:
        g=defaultdict(set);r=range(n);[g[u].add(v)for u,v in i];s={k};(f:=lambda u:[s.add(v)or f(v)for v in g[u]-s])(k);return[*(any((v in s)>(u in s)for u,v in i)and r or{*r}-s)]

test('''
3310. Remove Methods From Project
Medium
Topics
premium lock icon
Companies
Hint
You are maintaining a project that has n methods numbered from 0 to n - 1.

You are given two integers n and k, and a 2D integer array invocations, where invocations[i] = [ai, bi] indicates that method ai invokes method bi.

There is a known bug in method k. Method k, along with any method invoked by it, either directly or indirectly, are considered suspicious and we aim to remove them.

A group of methods can only be removed if no method outside the group invokes any methods within it.

Return an array containing all the remaining methods after removing all the suspicious methods. You may return the answer in any order. If it is not possible to remove all the suspicious methods, none should be removed.

 

Example 1:

Input: n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]

Output: [0,1,2,3]

Explanation:



Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.

Example 2:

Input: n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]

Output: [3,4]

Explanation:



Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.

Example 3:

Input: n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]

Output: []

Explanation:



All methods are suspicious. We can remove them.

 

Constraints:

1 <= n <= 105
0 <= k <= n - 1
0 <= invocations.length <= 2 * 105
invocations[i] == [ai, bi]
0 <= ai, bi <= n - 1
ai != bi
invocations[i] != invocations[j]
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
28,110/55.2K
Acceptance Rate
51.0%
Topics
Staff
Depth-First Search
Breadth-First Search
Graph Theory
Weekly Contest 418
icon
Companies
Hint 1
Use DFS from node k.
Hint 2
Mark all the nodes visited from node k, and then check if they can be visited from the other nodes.
''')
