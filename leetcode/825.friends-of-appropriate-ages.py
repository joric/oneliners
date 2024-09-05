from lc import *

# https://leetcode.com/problems/friends-of-appropriate-ages/discuss/127029/C%2B%2BJavaPython-Easy-and-Straight-Forward

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)
        c = Counter(ages)
        return sum(request(a, b) * c[a] * (c[b] - (a == b)) for a in c for b in c)

class Solution:
    def numFriendRequests(self, c: List[int]) -> int:
        c=Counter(c);return sum(c[x]*(c[y]-(x==y))*(x>=y>x/2+7)for x in c for y in c)

test('''
825. Friends Of Appropriate Ages
Medium

715

1186

Add to List

Share
There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

Return the total number of friend requests made.

 

Example 1:

Input: ages = [16,16]
Output: 2
Explanation: 2 people friend request each other.
Example 2:

Input: ages = [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: ages = [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.
 

Example 4:
Input: ages = [16,16]
Output: 2

Constraints:

n == ages.length
1 <= n <= 2 * 10^4
1 <= ages[i] <= 120
Accepted
80,263
Submissions
171,006
''')
