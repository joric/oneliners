from lc import *

# https://leetcode.com/problems/closest-equal-element-queries/solutions/6544562/python3-14-lines-bisect-ts-321-ms-54-mb-dk8jy/?envType=daily-question&envId=2026-04-16

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        d, ans = defaultdict(list), []
        for i, num in enumerate(nums):
            d[num].append(i)
        for q in queries:
            idx = d[nums[q]]
            m = len(idx)
            if m == 1: 
                ans.append(-1)
                continue
            j = bisect_left(idx, q)
            mn, mx = sorted([abs(q-idx[j - 1]), abs(q - idx[(j + 1)%m])])
            ans.append(min(mn, n - mx))
        return ans

class Solution:
    def solveQueries(self, a: List[int], q: List[int]) -> List[int]:
        d=defaultdict(list);
        for i,v in enumerate(a):
            d[v].append(i)
        r = []
        for x in q:
            p = d[a[x]]
            if len(p)<2:
                r.append(-1)
                continue
            j = bisect_right(p,x)%len(p)
            r.append(min((p[j]-x)%len(a),(x-p[j-2])%len(a)))
        return r

class Solution:
    def solveQueries(self, a: List[int], q: List[int]) -> List[int]:
        m=len(a);d={};[d.setdefault(v,[]).append(i)for i,v in enumerate(a)];return[2>len(p:=d[a[x]])and-1or min((p[j:=bisect_right(p,x)%len(p)]-x)%m,(x-p[j-2])%m)for x in q]

test('''
3488. Closest Equal Element Queries
Medium
Topics
premium lock icon
Companies
Hint
You are given a circular array nums and an array queries.

For each query i, you have to find the following:

The minimum distance between the element at index queries[i] and any other index j in the circular array, where nums[j] == nums[queries[i]]. If no such index exists, the answer for that query should be -1.
Return an array answer of the same size as queries, where answer[i] represents the result for query i.

 

Example 1:

Input: nums = [1,3,1,4,1,3,2], queries = [0,3,5]

Output: [2,-1,3]

Explanation:

Query 0: The element at queries[0] = 0 is nums[0] = 1. The nearest index with the same value is 2, and the distance between them is 2.
Query 1: The element at queries[1] = 3 is nums[3] = 4. No other index contains 4, so the result is -1.
Query 2: The element at queries[2] = 5 is nums[5] = 3. The nearest index with the same value is 1, and the distance between them is 3 (following the circular path: 5 -> 6 -> 0 -> 1).
Example 2:

Input: nums = [1,2,3,4], queries = [0,1,2,3]

Output: [-1,-1,-1,-1]

Explanation:

Each value in nums is unique, so no index shares the same value as the queried element. This results in -1 for all queries.

 

Constraints:

1 <= queries.length <= nums.length <= 105
1 <= nums[i] <= 106
0 <= queries[i] < nums.length
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
21,965/66.5K
Acceptance Rate
33.0%
Topics
Senior
Array
Hash Table
Binary Search
Weekly Contest 441
icon
Companies
Hint 1
Use a dictionary that maps each unique value in the array to a sorted list of its indices.
Hint 2
For each query, use binary search on the sorted indices list to find the nearest occurrences of the target value.
''')
