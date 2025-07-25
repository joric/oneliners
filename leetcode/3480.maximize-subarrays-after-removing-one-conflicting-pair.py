from lc import *

# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/solutions/6515832/python-greedy/

class Solution:
    def maxSubarrays(self, N: int, A: List[List[int]]) -> int:
        right = [[] for _ in range(N + 1)]
        for a, b in A:
            right[max(a, b)].append(min(a, b))
        ans = 0
        left = [0, 0]
        imp = [0] * (N + 1)
        for r in range(1, N + 1):
            for l in right[r]:
                left = max(left, [l, left[0]], [left[0], l])
            ans += r - left[0]
            imp[left[0]] += left[0] - left[1]
        return ans + max(imp)

class Solution:
    def maxSubarrays(self, n: int, p: List[List[int]]) -> int:
        r = defaultdict(list)
        [r[max(a,b)].append(min(a,b))for a,b in p]
        s = 0
        c = [0]*(n+1)
        l = [0,0]
        for i in range(1,n+1):
            for j in r[i]:
                l = max(l,[j,l[0]],[l[0],j])
            s += i - l[0]
            c[l[0]] += l[0]-l[1]
        return s + max(c)

class Solution:
    def maxSubarrays(self, n: int, p: List[List[int]]) -> int:
        r,c,l,s=defaultdict(list),[0]*(n+1),[0,0],0;[r[max(a,b)].append(min(a,b))for a,b in p];[([l:=max(l,[j,l[0]],[l[0],j])for j in r[i]],s:=s+i-l[0],setitem(c,l[0],c[l[0]]+l[0]-l[1]))for i in range(1,n+1)];return s+max(c)

test('''
3480. Maximize Subarrays After Removing One Conflicting Pair
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer n which represents an array nums containing the numbers from 1 to n in order. Additionally, you are given a 2D array conflictingPairs, where conflictingPairs[i] = [a, b] indicates that a and b form a conflicting pair.

Remove exactly one element from conflictingPairs. Afterward, count the number of non-empty subarrays of nums which do not contain both a and b for any remaining conflicting pair [a, b].

Return the maximum number of subarrays possible after removing exactly one conflicting pair.

 

Example 1:

Input: n = 4, conflictingPairs = [[2,3],[1,4]]

Output: 9

Explanation:

Remove [2, 3] from conflictingPairs. Now, conflictingPairs = [[1, 4]].
There are 9 subarrays in nums where [1, 4] do not appear together. They are [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3] and [2, 3, 4].
The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 9.
Example 2:

Input: n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]

Output: 12

Explanation:

Remove [1, 2] from conflictingPairs. Now, conflictingPairs = [[2, 5], [3, 5]].
There are 12 subarrays in nums where [2, 5] and [3, 5] do not appear together.
The maximum number of subarrays we can achieve after removing one element from conflictingPairs is 12.
 

Constraints:

2 <= n <= 105
1 <= conflictingPairs.length <= 2 * n
conflictingPairs[i].length == 2
1 <= conflictingPairs[i][j] <= n
conflictingPairs[i][0] != conflictingPairs[i][1]
Seen this question in a real interview before?
1/5
Yes
No
Accepted
2,791/8.7K
Acceptance Rate
32.1%
Topics
Array
Segment Tree
Enumeration
Prefix Sum
Weekly Contest 440
icon
Companies
Hint 1
Let f[i] (where i = 1, 2, 3, ..., n) be the end index of the longest valid subarray (without any conflicting pair) starting at index i.
Hint 2
The answer is: sigma(f[i] - i + 1) for i in [1..n], which simplifies to: sigma(f[i]) - n * (n + 1) / 2 + n.
Hint 3
Focus on maintaining f[i].
Hint 4
If we have a conflicting pair (x, y) with x < y: 1. Sort the conflicting pairs by y values in non-increasing order. 2. Update each prefix of the f array accordingly.
Hint 5
Use a segment tree or another suitable data structure to maintain the range update and sum query efficiently.
''')
