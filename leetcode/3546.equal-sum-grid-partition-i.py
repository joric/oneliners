from lc import *

# https://leetcode.com/problems/equal-sum-grid-partition-i/?envType=daily-question&envId=2026-03-25

class Solution:
    def canPartitionGrid(self, g: List[List[int]]) -> bool:
        d=[*chain(*[*map(accumulate,(map(sum,g),map(sum,zip(*g))))])];return any(x+x==d[-1]for x in d)

class Solution:
    def canPartitionGrid(self, g: List[List[int]]) -> bool:
        a=list(chain(*(accumulate(map(sum,g))for g in(g,zip(*g)))));return any(x+x==a[-1]for x in a)

class Solution:
    def canPartitionGrid(self, g: List[List[int]]) -> bool:
        a=accumulate;return any(map(eq,[sum(sum(g,[]))//2],[*a(map(sum,g)),*a(map(sum,zip(*g)))]))

class Solution:
    def canPartitionGrid(self, g: List[List[int]]) -> bool:
        d=[x for i in(g,zip(*g))for x in accumulate(map(sum,i))];return any(x+x==d[-1]for x in d)

class Solution:
    def canPartitionGrid(self, g: List[List[int]]) -> bool:
        s=sum(sum(g,[]));return any(x+x==s for d in(g,zip(*g))for x in accumulate(map(sum,d)))

class Solution:
    def canPartitionGrid(self, g: List[List[int]]) -> bool:
        a=accumulate;d=[*a(map(sum,g)),*a(map(sum,zip(*g)))];return any(x+x==d[-1]for x in d)

test('''
3546. Equal Sum Grid Partition I
Medium
Topics
premium lock icon
Companies
Hint
You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

Each of the two resulting sections formed by the cut is non-empty.
The sum of the elements in both sections is equal.
Return true if such a partition exists; otherwise return false.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:



A horizontal cut between row 0 and row 1 results in two non-empty sections, each with a sum of 5. Thus, the answer is true.

Example 2:

Input: grid = [[1,3],[2,4]]

Output: false

Explanation:

No horizontal or vertical cut results in two non-empty sections with equal sums. Thus, the answer is false.

 

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
25,854/61.1K
Acceptance Rate
42.3%
Topics
Senior
Array
Matrix
Enumeration
Prefix Sum
Weekly Contest 449
icon
Companies
Hint 1
There are two types of cuts: a horizontal cut or a vertical cut.
Hint 2
For a horizontal cut at row r (0 <= r grid into rows 0...r vs. r+1...m-1 and compare their sums.
Hint 3
For a vertical cut at column c (0 <= c < n - 1), split grid into columns 0...c vs. c+1...n-1 and compare their sums.
Hint 4
Brute‑force all possible r and c cuts; if any yields equal section sums, return true.
''')
