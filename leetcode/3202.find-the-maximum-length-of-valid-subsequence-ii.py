from lc import *

# https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/solutions/5389350/java-c-python-1d-dp/

class Solution:
    def maximumLength(self, a: List[int], k: int) -> int:
        c = defaultdict(Counter)
        for a in a:
            for b in range(k):
                c[b][a%k] = c[a%k][b] + 1
        return max(max(c[a].values())for a in range(k))

class Solution:
    def maximumLength(self, a: List[int], k: int) -> int:
        c=defaultdict(Counter);[setitem(c[b],a%k,c[a%k][b]+1)for a in a for b in range(k)];return max(max(c[a].values())for a in range(k))

class Solution:
    def maximumLength(self, a: List[int], k: int) -> int:
        c=defaultdict(Counter);[setitem(c[b],a%k,c[a%k][b]+1)for a in a for b in range(k)];return max(max(c[a].values())for a in c)

test('''
3202. Find the Maximum Length of Valid Subsequence II
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.
 

Example 1:

Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:

The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:

Input: nums = [1,4,2,3,1,4], k = 3

Output: 4

Explanation:

The longest valid subsequence is [1, 4, 1, 4].

 

Constraints:

2 <= nums.length <= 103
1 <= nums[i] <= 107
1 <= k <= 103
Seen this question in a real interview before?
1/5
Yes
No
Accepted
20,900/52K
Acceptance Rate
40.2%
Topics
Array
Dynamic Programming
icon
Companies
Hint 1
Fix the value of (subs[0] + subs[1]) % k from the k possible values. Let it be val.
Hint 2
Let dp[i] store the maximum length of a subsequence with its last element x such that x % k == i.
Hint 3
Answer for a subsequence ending at index y is dp[(k + val - (y % k)) % k] + 1.
Similar Questions
Longest Increasing Subsequence
Medium
Length of the Longest Subsequence That Sums to Target
Medium
''')
