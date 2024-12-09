from lc import *

# https://leetcode.com/problems/special-array-ii/discuss/5177657/Python-3-oror-3-lines-pairwise-prefix-oror-TS-%3A-99-11

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        pairs = map(lambda x: x[0]%2 == x[1]%2, pairwise(nums))
        pref = list(accumulate(pairs,initial = 0))
        return map(lambda x: pref[x[0]]==pref[x[1]], queries)

class Solution:
    def isArraySpecial(self, a: List[int], q: List[List[int]]) -> List[bool]:
        p=[*accumulate(map(lambda x:x[0]%2==x[1]%2,pairwise(a)),initial=0)];return map(lambda x:p[x[0]]==p[x[1]],q)

class Solution:
    def isArraySpecial(self, a: List[int], q: List[List[int]]) -> List[bool]:
        p=[*accumulate(starmap(eq,pairwise(map((1).__and__,a))),initial=0)];return map(lambda x:p[x[0]]==p[x[1]],q)

class Solution:
    def isArraySpecial(self, a: List[int], q: List[List[int]]) -> List[bool]:
        p=[*accumulate(starmap(eq,pairwise(map((1).__and__,a))),initial=0)];return[p[i]==p[j] for i,j in q]

class Solution:
    def isArraySpecial(self, a: List[int], q: List[List[int]]) -> List[bool]:
        p=[*accumulate(starmap(eq,pairwise(x&1 for x in a)),initial=0)];return[p[i]==p[j] for i,j in q]

test('''
3152. Special Array II
Medium

202

13

Add to List

Share
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that subarray nums[fromi..toi] is special or not.

Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.

 

Example 1:

Input: nums = [3,4,1,2,6], queries = [[0,4]]

Output: [false]

Explanation:

The subarray is [3,4,1,2,6]. 2 and 6 are both even.

Example 2:

Input: nums = [4,3,1,6], queries = [[0,2],[2,3]]

Output: [false,true]

Explanation:

The subarray is [4,3,1]. 3 and 1 are both odd. So the answer to this query is false.
The subarray is [1,6]. There is only one pair: (1,6) and it contains numbers with different parity. So the answer to this query is true.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= queries.length <= 105
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] <= nums.length - 1
Accepted
32,823
Submissions
108,065
''')
