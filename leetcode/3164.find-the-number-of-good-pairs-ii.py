from lc import *

# https://leetcode.com/problems/find-the-number-of-good-pairs-ii/discuss/5209770/Python-3-oror-8-lines-filter-Counters-oror-TS%3A-93-12

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums1 = list(map(lambda x: x//k, filter(lambda x: x%k == 0, nums1)))
        mx1 = max(nums1, default = 0) + 1
        ctr1 = defaultdict(int)
        ctr2 = Counter(nums2)
        for n2 in ctr2:
            for i in range(n2, mx1, n2):
                ctr1[i]+= ctr2[n2]
        return sum(map(lambda x: ctr1[x], nums1))

class Solution:
    def numberOfPairs(self, a: List[int], b: List[int], k: int) -> int:
        a,c,d,m=[*map(lambda x:x//k,filter(lambda x:x%k==0,a))],Counter(b),defaultdict(int),max([0,*a])+1;[setitem(d,i,d[i]+c[j])for j in c for i in range(j,m,j)];return sum(map(lambda x:d[x],a))

test('''
3164. Find the Number of Good Pairs II
Medium

207

37

Add to List

Share
You are given 2 integer arrays nums1 and nums2 of lengths n and m respectively. You are also given a positive integer k.

A pair (i, j) is called good if nums1[i] is divisible by nums2[j] * k (0 <= i <= n - 1, 0 <= j <= m - 1).

Return the total number of good pairs.

 

Example 1:

Input: nums1 = [1,3,4], nums2 = [1,3,4], k = 1

Output: 5

Explanation:

The 5 good pairs are (0, 0), (1, 0), (1, 1), (2, 0), and (2, 2).
Example 2:

Input: nums1 = [1,2,4,12], nums2 = [2,4], k = 3

Output: 2

Explanation:

The 2 good pairs are (3, 0) and (3, 1).

 

Constraints:

1 <= n, m <= 105
1 <= nums1[i], nums2[j] <= 106
1 <= k <= 103
Accepted
24,982
Submissions
97,300
''')
