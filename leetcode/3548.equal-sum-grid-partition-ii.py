from lc import *

# https://leetcode.com/problems/equal-sum-grid-partition-ii/?envType=daily-question&envId=2026-03-26

class Solution:
    def canPartitionGrid(self, A: List[List[int]]) -> bool:
        def check(A):
            seen = set()
            top = 0
            for i, r in enumerate(A):
                seen |= set(r)
                top += sum(r)
                bot = total - top
                if top - bot in [0, A[0][0],  A[0][-1], A[i][0]]: return True
                if len(A[0]) > 1 and i > 0 and top - bot in seen: return True
            return False
        
        total = sum(sum(r) for r in A)
        if check(A) or check(A[::-1]): return True
        A = list(zip(*A))
        return check(A) or check(A[::-1])

class Solution:
    def canPartitionGrid(self, g: List[List[int]]) -> bool:
        t=sum(map(sum,g));z=[*zip(*g)]
        def c(a):
            s=set()
            p=0
            for i,r in enumerate(a[:-1]):
                s.update(r)
                p+=sum(r)
                d=2*p-t
                if d in(0,a[0][0],a[0][-1],a[i][0])or(i>0<len(a[0])-1and d in s):
                    return 1
        return any(c(m)for m in(g,g[::-1],z,z[::-1]))

class Solution:
    def canPartitionGrid(self, g: List[List[int]]) -> bool:
        t=sum(map(sum,g));z=[*zip(*g)];return any((s:=set(),p:=0,any((s.update(r),p:=p+sum(r),d:=2*p-t,d in(0,a[0][0],a[0][-1],a[i][0])or i>0<len(r)-1and d in s)[3]for i,r in enumerate(a[:-1])))[2]for a in(g,g[::-1],z,z[::-1]))

test('''
3548. Equal Sum Grid Partition II
Hard
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
If a cell is discounted, the rest of the section must remain connected.
Return true if such a partition exists; otherwise, return false.

Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:



A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.
Example 2:

Input: grid = [[1,2],[3,4]]

Output: true

Explanation:



A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.
Example 3:

Input: grid = [[1,2,4],[2,3,5]]

Output: false

Explanation:



A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.
Example 4:

Input: grid = [[4,1,8],[3,2,6]]

Output: false

Explanation:

No valid cut exists, so the answer is false.

 

Constraints:

1 <= m == grid.length <= 105
1 <= n == grid[i].length <= 105
2 <= m * n <= 105
1 <= grid[i][j] <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
6,966/31.3K
Acceptance Rate
22.3%
Topics
Principal
Array
Hash Table
Matrix
Enumeration
Prefix Sum
Weekly Contest 449
icon
Companies
Hint 1
In a grid (or any subgrid), when can a section be disconnected? Can disconnected components occur if the section spans more than one row and more than one column?
Hint 2
Handle single rows or single columns separately. For all other partitions, maintain the sums and value frequencies of each section to check whether removing at most one element from one section can make the two sums equal.
''')
