from lc import *

# https://leetcode.com/problems/permutation-sequence/discuss/832365/python-itertools

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return''.join([*permutations('123456789'[:n])][k-1])

test('''
60. Permutation Sequence
Hard

6728

483

Add to List

Share
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
Accepted
421,876
Submissions
879,139
''')
