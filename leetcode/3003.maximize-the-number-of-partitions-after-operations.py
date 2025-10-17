from lc import *

# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/solutions/4520834/c-java-python-clean-bitmask-dp/?envType=daily-question&envId=2025-10-17

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        @cache
        def f(i, m, c):
            if i == len(s):
                return 0
            j = ord(s[i]) - ord('a')
            n = m | (1 << j)
            d = n.bit_count()
            if d > k:
                r = 1 + f(i + 1, 1 << j, c)
            else:
                r = f(i + 1, n, c)
            if c:
                for p in range(26):
                    q = m | (1 << p)
                    e = q.bit_count()

                    if e > k:
                        r = max(r, 1 + f(i + 1, 1 << p, False))
                    else:
                        r = max(r, f(i + 1, q, False))
            return r
        return f(0, 0, True) + 1

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        g=lambda t,i,p,q,c:t+f(i+1,t and 1<<p or q,c);
        f=cache(lambda i,m,c:i<len(s) and max(r:=g((n:=m|(1<<(j:=ord(s[i])-ord('a')))).bit_count()>k,i,j,n,c),c and max(g((q:=m|(1<<p)).bit_count()>k,i,p,q,0)for p in range(26))or r))
        return f(0,0,1)+1

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        g=lambda t,i,p,q,c:t+f(i+1,t and 1<<p or q,c);return(f:=cache(lambda i,m,c:i<len(s)and max(r:=g((n:=m|(1<<(j:=ord(s[i])-ord('a')))).bit_count()>k,i,j,n,c),c and max(g((q:=m|(1<<p)).bit_count()>k,i,p,q,0)for p in range(26))or r)))(0,0,1)+1

test('''
3003. Maximize the Number of Partitions After Operations
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given a string s and an integer k.

First, you are allowed to change at most one index in s to another lowercase English letter.

After that, do the following partitioning operation until s is empty:

Choose the longest prefix of s containing at most k distinct characters.
Delete the prefix from s and increase the number of partitions by one. The remaining characters (if any) in s maintain their initial order.
Return an integer denoting the maximum number of resulting partitions after the operations by optimally choosing at most one index to change.

 

Example 1:

Input: s = "accca", k = 2

Output: 3

Explanation:

The optimal way is to change s[2] to something other than a and c, for example, b. then it becomes "acbca".

Then we perform the operations:

The longest prefix containing at most 2 distinct characters is "ac", we remove it and s becomes "bca".
Now The longest prefix containing at most 2 distinct characters is "bc", so we remove it and s becomes "a".
Finally, we remove "a" and s becomes empty, so the procedure ends.
Doing the operations, the string is divided into 3 partitions, so the answer is 3.

Example 2:

Input: s = "aabaab", k = 3

Output: 1

Explanation:

Initially s contains 2 distinct characters, so whichever character we change, it will contain at most 3 distinct characters, so the longest prefix with at most 3 distinct characters would always be all of it, therefore the answer is 1.

Example 3:

Input: s = "xxyz", k = 1

Output: 4

Explanation:

The optimal way is to change s[0] or s[1] to something other than characters in s, for example, to change s[0] to w.

Then s becomes "wxyz", which consists of 4 distinct characters, so as k is 1, it will divide into 4 partitions.

Other examples:

Input: s = "qertyuiopasdfghjklzxcvbnmqertyuiopasdfghjklzxcvbnmw", k = 25
Output: 3

Constraints:

1 <= s.length <= 104
s consists only of lowercase English letters.
1 <= k <= 26
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
11,869/27.3K
Acceptance Rate
43.5%
Topics
String
Dynamic Programming
Bit Manipulation
Bitmask
Weekly Contest 379
icon
Companies
Hint 1
For each position, try to brute-force the replacements.
Hint 2
To speed up the brute-force solution, we can precompute the following (without changing any index) using prefix sums and binary search:
pref[i]: The number of resulting partitions from the operations by performing the operations on s[0:i].
suff[i]: The number of resulting partitions from the operations by performing the operations on s[i:n - 1], where n == s.length.
partition_start[i]: The start index of the partition containing the ith index after performing the operations.
Hint 3
Now, for a position i, we can try all possible 25 replacements:
For a replacement, using prefix sums and binary search, we need to find the rightmost index, r, such that the number of distinct characters in the range [partition_start[i], r] is at most k.
There are 2 cases:
r >= i: the number of resulting partitions in this case is 1 + pref[partition_start[i] - 1] + suff[r + 1].
Otherwise, we need to find the rightmost index r2 such that the number of distinct characters in the range [r:r2] is at most k. The answer in this case is 2 + pref[partition_start[i] - 1] + suff[r2 + 1]
Hint 4
The answer is the maximum among all replacements.
''')
