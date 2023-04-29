from lc import *

# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/discuss/981266/6-lines-with-Unicode-Find

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        s = ''.join(map(chr, range(n)))
        [*map(list.append, queries, count())]
        for u, v, d, *j in sorted(queries + edgeList, key=itemgetter(2)):
            if j: queries[j[0]] = s[u] == s[v]
            else: s = s.replace(s[u], s[v])
        return queries

class Solution:
    def distanceLimitedPathsExist(self, n: int, e: List[List[int]], q: List[List[int]]) -> List[bool]:
        s = ''.join(map(chr, range(n)))
        [*map(list.append, q, count())]
        for u, v, d, *j in sorted(q + e, key=itemgetter(2)):
            if j: q[j[0]] = s[u] == s[v]
            else: s = s.replace(s[u], s[v])
        return q

class Solution:
    def distanceLimitedPathsExist(self, n: int, e: List[List[int]], q: List[List[int]]) -> List[bool]:
        return (s:=''.join(map(chr,range(n))),[*map(list.append,q,count())],all(j and [setitem(q,j[0],s[u]==s[v])] or (s:=s.replace(s[u],s[v])) for u,v,d,*j in sorted(q+e,key=itemgetter(2))),q)[3]

test('''
1697. Checking Existence of Edge Length Limited Paths
Hard

824

16

Add to List

Share
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

 

Example 1:


Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
Example 2:


Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.
 

Constraints:

2 <= n <= 105
1 <= edgeList.length, queries.length <= 105
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 109
There may be multiple edges between two nodes.
Accepted
14,929
Submissions
28,202
Seen this question in a real interview before?

Yes

No
Checking Existence of Edge Length Limited Paths II
Hard
Number of Good Paths
Hard
Minimum Score of a Path Between Two Cities
Medium
All the queries are given in advance. Is there a way you can reorder the queries to avoid repeated computations?
''')

