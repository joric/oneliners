from lc import *

# https://leetcode.com/problems/best-sightseeing-pair/discuss/260850/JavaC%2B%2BPython-One-Pass-O(1)-space

class Solution:
    def maxScoreSightseeingPair(self, v: List[int]) -> int:
        return reduce(lambda p,a:[max(p[0],p[1]+a),max(p[1],a)-1],v,[0,0])[0]

class Solution:
    def maxScoreSightseeingPair(self, v: List[int]) -> int:
        c=r=0
        for a in v:
            r=max(r,c+a)
            c=max(c,a)-1
        return r

class Solution:
    def maxScoreSightseeingPair(self, v: List[int]) -> int:
        c=r=0;[(r:=max(r,c+a),c:=max(c,a)-1)for a in v];return r

test('''
1014. Best Sightseeing Pair
Medium

2613

61

Add to List

Share
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:

Input: values = [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11
Example 2:

Input: values = [1,2]
Output: 2
 

Constraints:

2 <= values.length <= 5 * 104
1 <= values[i] <= 1000
Accepted
102,354
Submissions
172,206
''')
