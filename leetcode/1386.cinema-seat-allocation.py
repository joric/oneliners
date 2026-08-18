from lc import *

# https://leetcode.com/problems/cinema-seat-allocation/solutions/797309/3-lines-of-code-by-talkingraisin-6vto/?envType=daily-question&envId=2026-08-19

class Solution:
  def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    g = defaultdict(int)
    for r, s in reservedSeats: g[r] |= {0: 0, 1: 4, 2: 5, 3: 3, 4: 2, 5: 0}[s >> 1]
    return sum(2 if s == 0 else 1 if s < 7 else 0 for r, s in g.items()) + (n - len(g)) * 2

# https://leetcode.com/problems/cinema-seat-allocation/solutions/8466400/three-simple-lines-of-code-by-mikposp-5s7a/?envType=daily-question&envId=2026-08-19

class Solution:
    def maxNumberOfFamilies(self, n: int, a: List[List[int]]) -> int:
        l,m,r,d = 0b0111100000,0b0001111000,0b0000011110,Counter()
        for row,seat in a: d[row] |= 1<<seat-1
        return n*2-sum(2-((q&l<1)+(q&r<1) or q&m<1) for q in d.values())

class Solution:
    def maxNumberOfFamilies(self, n: int, a: List[List[int]]) -> int:
        d={};[setitem(d,r,d.get(r,0)|1<<c)for r,c in a];return n*2-sum(2-((q&60<1)+(q&960<1)or q&240<1)for q in d.values())

class Solution:
    def maxNumberOfFamilies(self, n: int, a: List[List[int]]) -> int:
        d=Counter();[d.update({r:1<<c})for r,c in a];return n*2-sum(2-((q&60<1)+(q&960<1)or q&240<1)for q in d.values())

test('''
1386. Cinema Seat Allocation
Solved
Medium
Topics
premium lock icon
Companies
Hint


A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.

You are given a 2D integer array reservedSeats, where reservedSeats[i] = [rowi, seati] means that seat seati in row rowi is already reserved.

A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:

seats 2, 3, 4, 5
seats 4, 5, 6, 7
seats 6, 7, 8, 9
A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.

Return an integer denoting the maximum number of four-person groups that can be assigned.

 

Example 1:



Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
Output: 4
Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.
Example 2:

Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
Output: 2
Example 3:

Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
Output: 4
 

Constraints:

1 <= n <= 109
1 <= reservedSeats.length <= min(10 * n, 104)
reservedSeats[i] == [rowi, seati]
1 <= rowi <= n
1 <= seati <= 10
All reservedSeats[i] are distinct.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
68,428/152.2K
Acceptance Rate
45.0%
Topics
Senior
Array
Hash Table
Greedy
Bit Manipulation
Biweekly Contest 22
icon
Companies
Hint 1
Note you can allocate at most two four-person groups in one row.
Hint 2
Greedily check if you can allocate seats for two groups, one group or none.
Hint 3
Process only rows that appear in the input, for other rows you can always allocate seats for two groups.
Similar Questions
Booking Concert Tickets in Groups
Hard
''')
