from lc import *

# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/solutions/1009406/python-concise-backtracking/?envType=daily-question&envId=2025-02-16
# TODO

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = 2*n-1
        A, V = [0] * m, [False] * (n+1)
        def dfs(i):
            if i == m:
                return all(A)
            if A[i]:
                return dfs(i+1)
            for x in range(n, 0, -1):
                j = i if x == 1 else i+x    # This is only to combine some lines of code.
                if not V[x] and j < m and not A[j]:
                    A[i], A[j], V[x] = x, x, True
                    if dfs(i+1):
                        return True
                    A[i], A[j], V[x] = 0, 0, False
            return False
        dfs(0)
        return A

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m=2*n-1;a,v,s=[0]*m,[False]*(n+1),setitem
        def f(i):
            if i == m:
                return all(a)
            if a[i]:
                return f(i+1)
            for x in range(n,0,-1):
                j=i if x==1 else i+x
                if j<m and not(v[x] or a[j]):
                    exec('a[i],a[j],v[x]=x,x,True')
                    if f(i+1):
                        return True
                    exec('a[i],a[j],v[x]=0,0,False')
        f(0)
        return a

test('''
1718. Construct the Lexicographically Largest Valid Sequence
Solved
Medium
Topics
Companies
Hint
Given an integer n, find a sequence that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

 

Example 1:

Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.
Example 2:

Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
 

Constraints:

1 <= n <= 20
Seen this question in a real interview before?
1/5
Yes
No
Accepted
15.9K
Submissions
29K
Acceptance Rate
55.0%
Topics
Array
Backtracking
Companies
Hint 1
Heuristic algorithm may work.
Similar Questions
The Number of Beautiful Subsets
Medium
Find the Lexicographically Largest String From the Box I
Medium
''')
