from lc import *

# https://leetcode.com/problems/minimum-genetic-mutation/discuss/2097023/Python-3.10%3A-DFS-BFS.-VERY-SHORT.

class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        bank = set(bank) | {start}
        def dfs(v, n):
            if v == end:
                return n
            bank.remove(v)
            for i, a in enumerate(v):
                for c in 'ACGT':
                    if (a!=c and (t:=v[:i]+c+v[i+1:]) in bank and (r:=dfs(t,n+1))!=-1):
                        return r
            return -1
        return dfs(start, 0)

class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        return (bank:=set(bank)|{start}) and (f:=lambda v,n:n if v==end else bank.remove(v) or next((r for i,a in
            enumerate(v) for c in 'ACGT' if (a!=c and (t:=v[:i]+c+v[i+1:]) in bank and (r:=f(t,n+1))!=-1)), -1))(start, 0)

class Solution:
    def minMutation(self, s: str, e: str, b: list[str]) -> int:
         b={*b}|{s};return(f:=lambda v,n:v==e and n or b.remove(v)or next((r for i,a in enumerate(v)for c in'ACGT'if(a!=c and(t:=v[:i]+c+v[i+1:])in b and(r:=f(t,n+1))!=-1)),-1))(s,0)

test('''

433. Minimum Genetic Mutation
Medium

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.


Example 1:

Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1

Example 2:

Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2

Example 3:

Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3

Constraints:

start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].

''')
