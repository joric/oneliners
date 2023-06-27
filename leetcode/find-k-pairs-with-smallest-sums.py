from lc import *

# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84550/Slow-1-liner-to-Fast-solutions

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs

# TLE
class Solution:
    def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
        return nsmallest(k,product(a,b),key=sum)

# MLE
class Solution:
    def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
        return sorted(product(a,b),key=sum)[:k]

class Solution:
    def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
        streams = map(lambda u:((u+v,u,v)for v in b),a)
        stream = merge(*streams)
        return [x[1:] for x in islice(stream, k)]

class Solution:
    def kSmallestPairs(self, a: List[int], b: List[int], k: int) -> List[List[int]]:
        return [s[1:]for s in islice(merge(*map(lambda u:((u+v,u,v)for v in b),a)),k)]

test('''
373. Find K Pairs with Smallest Sums
Medium

4425

266

Add to List

Share
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
 

Constraints:

1 <= nums1.length, nums2.length <= 10^5
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1 and nums2 both are sorted in ascending order.
1 <= k <= 10^4
''')

