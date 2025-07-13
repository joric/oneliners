from lc import *

# https://leetcode.com/problems/maximum-matching-of-players-with-trainers/solutions/2599208/python-3-one-line/

class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        heapify(p);return sum(bool(p and x>=p[0]and heappop(p))for x in sorted(t))

class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        heapify(p);return sum(p>[]and x>=p[0]and 0<heappop(p)for x in sorted(t))

class Solution:
    def matchPlayersAndTrainers(self, p: List[int], t: List[int]) -> int:
        heapify(p);return sum([x]>=p[:1]>[]!=heappop(p)for x in sorted(t))

test('''
2410. Maximum Matching of Players With Trainers
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array players, where players[i] represents the ability of the ith player. You are also given a 0-indexed integer array trainers, where trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less than or equal to the trainer's training capacity. Additionally, the ith player can be matched with at most one trainer, and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions.

 

Example 1:

Input: players = [4,7,9], trainers = [8,2,5,8]
Output: 2
Explanation:
One of the ways we can form two matchings is as follows:
- players[0] can be matched with trainers[0] since 4 <= 8.
- players[1] can be matched with trainers[3] since 7 <= 8.
It can be proven that 2 is the maximum number of matchings that can be formed.
Example 2:

Input: players = [1,1,1], trainers = [10]
Output: 1
Explanation:
The trainer can be matched with any of the 3 players.
Each player can only be matched with one trainer, so the maximum answer is 1.

Other examples:

Input: players = [1,1000000000], trainers = [1000000000,1]
Output: 2

Input: players = [4,2], trainers = [4,4,3]
Output: 2

Constraints:

1 <= players.length, trainers.length <= 105
1 <= players[i], trainers[j] <= 109
 

Note: This question is the same as 445: Assign Cookies.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
56,698/83.4K
Acceptance Rate
68.0%
Topics
Array
Two Pointers
Greedy
Sorting
icon
Companies
Hint 1
Sort both the arrays.
Hint 2
Construct the matching greedily.
Similar Questions
Most Profit Assigning Work
Medium
Long Pressed Name
Easy
Interval List Intersections
Medium
Largest Merge Of Two Strings
Medium
Maximum Number of Tasks You Can Assign
Hard
Successful Pairs of Spells and Potions
Medium
The Latest Time to Catch a Bus
Medium
Maximize Greatness of an Array
Medium
''')
