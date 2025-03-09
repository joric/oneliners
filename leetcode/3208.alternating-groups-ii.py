from lc import *

# https://leetcode.com/problems/alternating-groups-ii/solutions/5443075/python-3-one-line-fast-and-short/?envType=daily-question&envId=2025-03-09

class Solution:
    def numberOfAlternatingGroups(self, a: List[int], k: int) -> int:
       return sum(max(0,sum(g)-k+2)for x,g in groupby(starmap(ne,pairwise(a+a[:k-1])))if x)

class Solution:
    def numberOfAlternatingGroups(self, a: List[int], k: int) -> int:
        c=1;return sum(k<=(c:=c*(a[i]!=a[i-1])+1)for i in range(-k+2,len(a)))

test('''
3208. Alternating Groups II
Medium
Topics
Companies
Hint
There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [0,1,0,1,0], k = 3

Output: 3

Explanation:



Alternating groups:



Example 2:

Input: colors = [0,1,0,0,1,0,1], k = 6

Output: 2

Explanation:



Alternating groups:



Example 3:

Input: colors = [1,1,0,1], k = 4

Output: 0

Explanation:



 

Constraints:

3 <= colors.length <= 10^5
0 <= colors[i] <= 1
3 <= k <= colors.length

Seen this question in a real interview before?
1/5
Yes
No
Accepted
28.1K
Submissions
64.9K
Acceptance Rate
43.3%
Topics
Array
Sliding Window
Companies
Hint 1
Try to find a tile that has the same color as its next tile (if it exists).
Hint 2
Then try to find maximal alternating groups by starting a single for loop from that tile.
''')
